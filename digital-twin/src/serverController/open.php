<?php
include("../assets/mod/session.php");
include("../assets/mod/token.php");
?>

<script src="../assets/js/HTTPRequest.js"></script>
<script src="../assets/js/ServerConnectionManager.js"></script>
<script src="../assets/js/printFunctions.js"></script>
<script src="../assets/js/serverFunctions.js"></script>
<?php
require "../assets/mod/HTTPRequester.php";




$output = shell_exec('./openServer.sh');
echo "<pre>$output</pre>";
preg_match('/(?<=PID=\[).*?(?=\])/', $output, $matches);
if (!empty($matches)) {
    $PID = $matches[0];
    if (!empty($PID)) {
        echo '<button style="position: fixed; bottom: 20px; left: 20px;" type="button" onclick="closeServer(' . $PID . ')" id="closeserver">Close Server on PID ' . $PID . '</button>';
    }
}
$output2 = shell_exec('ps -ef');
echo "<pre>$output2</pre>";
?>
<div id="output"></div>