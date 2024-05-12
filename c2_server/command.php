<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<form action="command.php" method="post">
<type="text" name="hostname"><br>
<type="text" name="port"><br>
<type="text" name="getin"><br>
<type="text" name="username"><br>
<type="text" name="echo"><br>
</form>

</body>
</html>

<?php
try{
if ($_SERVER['REQUEST_METHOD'] != 'POST'){throw new Exception("WRONG REQUEST METHOD");}
else{
    if ($_POST['hostname'] != "" && $_POST['port'] != "" && $_POST['getin'] != ""){
        $jsonString = file_get_contents('commander.json');
        $data = json_decode($jsonString, true);
        $data['hostname'] = $_POST['hostname'];
        $data['port'] = $_POST['port'];
        $data['getin'] = $_POST['getin'];
        $data['username'] = $_POST['username'];
        $data['echo'] = $_POST['echo'];
        $newJsonString = json_encode($data);
        file_put_contents('commander.json', $newJsonString);
        }
    }
}
catch(Exception $e) {
  echo $e->getMessage();
}
?>