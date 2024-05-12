<html>
<body>

<form action="index.php" method="post">
<type="text" name="username"><br>
</form>

</body>
</html>

<?php
try{
if ($_SERVER['REQUEST_METHOD'] != 'POST'){throw new Exception("WRONG REQUEST METHOD");}
else{
    $username = $_POST['username'];
    if ($username != ""){
        $jsonString = file_get_contents('visitors.json');
        $data = json_decode($jsonString, true);
        $data[$username]['ip'] = $_SERVER['REMOTE_ADDR'];
        $data[$username]['datetime'] = date('Y/m/d G:i:s');
        $newJsonString = json_encode($data);
        file_put_contents('visitors.json', $newJsonString);
        }
    }
}
catch(Exception $e) {
  echo $e->getMessage();
}
?>