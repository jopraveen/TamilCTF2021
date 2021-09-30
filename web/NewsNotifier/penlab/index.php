<?php
session_start();
$conn = mysqli_connect("localhost", "root", "testtamilctf", "sqlidb") or exit();

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
if($_SERVER["REQUEST_METHOD"] == "POST") {
  error_log(print_r($_REQUEST, true));

  $user = $_POST['user'];
  $pass = $_POST['pass'];
  
  $sql = "SELECT id FROM user WHERE user = '$user' and pass = '$pass'";
  $result = mysqli_query($conn,$sql);
  $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
  
  $count = mysqli_num_rows($result);
  	
  if($count == 1) {  
	$_SESSION['loggedin'] = true;
    $_SESSION['username'] = $user;
	header("Location: ctf.php");    
	#echo "<script>alert('Congratulations! you have logged in!')</script>";
  }else {
    echo "<h3>Your Login Name or Password is invalid</h3>";
  }
}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Tamil CTF</title>
</head>
<body>
	<style type="text/css">
	body {
		padding-top: 150px;
		background-color:#FFFF66;
	}
	h1,h2{
		text-align:center;
	}
	h3{
		text-align:center;
	}
	.form-style-6{
		font: 95% Arial, Helvetica, sans-serif;
		max-width: 400px;
		margin: 10px auto;
		padding: 16px;
		background: #F7F7F7;
	}
	.form-style-6 h1{
		background: #43D1AF;
		padding: 20px 0;
		font-size: 140%;
		font-weight: 300;
		text-align: center;
		color: black;
		margin: -16px -16px 16px -16px;
	}
	.form-style-6 input[type="text"],
	.form-style-6 input[type="password"],
	.form-style-6 input[type="date"],
	.form-style-6 input[type="datetime"],
	.form-style-6 input[type="email"],
	.form-style-6 input[type="number"],
	.form-style-6 input[type="search"],
	.form-style-6 input[type="time"],
	.form-style-6 input[type="url"],
	.form-style-6 textarea,
	.form-style-6 select 
	{
		-webkit-transition: all 0.30s ease-in-out;
		-moz-transition: all 0.30s ease-in-out;
		-ms-transition: all 0.30s ease-in-out;
		-o-transition: all 0.30s ease-in-out;
		outline: none;
		box-sizing: border-box;
		-webkit-box-sizing: border-box;
		-moz-box-sizing: border-box;
		width: 100%;
		background: #fff;
		margin-bottom: 4%;
		border: 1px solid #ccc;
		padding: 3%;
		color: black;
		font: 95% Arial, Helvetica, sans-serif;
	}
	.form-style-6 input[type="text"]:focus,
	.form-style-6 input[type="password"]:focus,
	.form-style-6 input[type="date"]:focus,
	.form-style-6 input[type="datetime"]:focus,
	.form-style-6 input[type="email"]:focus,
	.form-style-6 input[type="number"]:focus,
	.form-style-6 input[type="search"]:focus,
	.form-style-6 input[type="time"]:focus,
	.form-style-6 input[type="url"]:focus,
	.form-style-6 textarea:focus,
	.form-style-6 select:focus
	{
		box-shadow: 0 0 5px #43D1AF;
		padding: 3%;
		border: 1px solid #43D1AF;
	}

	.form-style-6 input[type="submit"],
	.form-style-6 input[type="button"]{
		box-sizing: border-box;
		-webkit-box-sizing: border-box;
		-moz-box-sizing: border-box;
		width: 100%;
		padding: 3%;
		background: #02235b;
		border-bottom: 2px solid #30C29E;
		border-top-style: none;
		border-right-style: none;
		border-left-style: none;	
		color: #fff;
	}
	.form-style-6 input[type="submit"]:hover,
	.form-style-6 input[type="button"]:hover{
		background: #02235b;
	}
	</style>
	<h1>Typical Admin Panel For Noobs</h1>
	<h2>Its really tough to break the authentication, ri8?</h2>
	<div class="form-style-6">
	<h1>Login Now</h1>
		<form action="" method="POST">
			<input type="text" name="user" placeholder="username" />
			<input type="password" name="pass" placeholder="*****" />
			<input type="submit" value="Login" />
		</form>
	</div>
</body>
</html>
