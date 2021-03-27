<?php
if($_POST["Message"]) {
mail("yzjandali@berkeley.edu", "Here is the sample subject line",
$_POST["Insert Your Message"]. "From: Insert Your Email");
}
?>
