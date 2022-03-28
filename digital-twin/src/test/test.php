<?php
$output = shell_exec('python3 /usr/src/app/ServerManager.py --default');
echo "<pre>$output</pre>";
?>