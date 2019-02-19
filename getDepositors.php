#!/usr/bin/php
<?php
	$file = 'Depositors.txt'; 
	file_put_contents("Depositors.txt",""); /* Clear file */
	$current = file_get_contents($file);

	$mysqli = new mysqli("localhost","root","root");

		if ($mysqli->connect_errno) {
			printf("Ошибка подключения к бд", $mysqli->connect_error);
			exit();
		}

		if ($result = $mysqli->query("SELECT * FROM pm_common.players ")) {
			printf("Select вернул \n", $result->num_rows);
		
			$result->close();
		}

	$mysqli->close();

	$current .= "\"Yo-ho-ho\",";


	file_put_contents($file,$current);
?>
