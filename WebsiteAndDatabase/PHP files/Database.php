<?php
	$db_server = "localhost";
	$db_user = "root";
	$db_pass = "";
	$db_name = "websitelogin";
	$conn = "";

	try{
		$conn = mysqli_connect($db_server = "localhost",
							$db_user = "root",
							$db_pass = "",
							$db_name = "websitelogin");
	}

	catch(mysqli_sql_exception){
		echo"Could not connect!";
	}

	if($conn){
		echo"Could connect";
	}
?>