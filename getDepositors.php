#!/usr/bin/php
<?php
	$file = 'Depositors.txt'; 
	file_put_contents("Depositors.txt",""); /* Clear file */
	$current = file_get_contents($file);

	$mysqli = new mysqli("127.0.0.1","hz","anythingelse?");

		if ($mysqli->connect_errno) {
			printf("Ошибка подключения к бд", $mysqli->connect_error);
			exit();
		}

		if ($result = $mysqli->query("SELECT `players`.`login` 
FROM `table`.`deposit` dep
INNER JOIN `table`.`players` players ON `players`.`login` = dep.login
WHERE face = 'ha-ha-ha' AND blocked = 0 
GROUP BY dep.`login`; ")) {

			

			while($rows = $result->fetch_assoc()) {
	
				printf($rows["login"]);
				printf("\n");
				$current .= "\"".$rows["login"]."\"".",";

			}

			/* get and delete last , */
			$current = rtrim($current,","); 
			

			$result->close();
		}

	$mysqli->close();


	file_put_contents($file,$current);
?>
