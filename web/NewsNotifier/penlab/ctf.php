<?php
session_start();
if(isset($_SESSION['loggedin'])){
  include('abcd.html');
  }
else{
    echo "<h1>You can't even break this? with proper style.. :-/</h1>";
}
?>