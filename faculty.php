<?php
$db = new PDO('mysql:host=localhost;dbname=faculty_demographics;charset=utf8','root','root');
foreach($db->query('SELECT * FROM facultydata') as $row){
	print_r($row);
	echo "<br /><br />";
}
?>