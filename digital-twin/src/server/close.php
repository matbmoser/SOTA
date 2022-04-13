<?php
$pid = $_POST['pid'];
$output = shell_exec('./closeServer.sh '.$pid);
echo "<pre>$output</pre>";