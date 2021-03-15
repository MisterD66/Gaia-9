<?php  
$date = date_create();
echo date_timestamp_get($date);
$fp = fopen('data.csv', 'a');//opens file in append mode  
fwrite($fp, date_timestamp_get($date) . "," . htmlspecialchars($_GET["light"]) . "," . htmlspecialchars($_GET["temp_out"]) . "," . htmlspecialchars($_GET["temp_in"]) . "," . htmlspecialchars($_GET["hum"]) . "," . htmlspecialchars($_GET["press"]) . "," . htmlspecialchars($_GET["bat"]) . ";");  
fclose($fp);  
?>  
