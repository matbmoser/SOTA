<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>Chat JS</title>
<link rel="stylesheet" type="text/css" href="assets/css/main.css"/>
</head>
<script src="assets/js/RTJPClient.js"></script>
<script src="assets/js/RTJPHandler.js"></script>
<script src="assets/js/config.js"></script>
<script src="assets/js/hashFunctions.js"></script>
<script src="assets/js/printFunctions.js"></script>
<script src="assets/js/workflowFunctions.js"></script>
<script src="assets/js/createClientFunctions.js"></script>

<div id="pagewrapper" style="display: none!important;"> 
    <body>
        <header><nav> </nav></header>
        <div>
            <label id="nmess" for="name">* Please indentify yourself!</label>
            <input type="text" id="name" name="name"><br><br>
            <button type="submit" id="submit">Start</button> 
            
            <div id="config" class="hidden">
                <label for="ip">Please insert IP of server!</label>
                <input type="text" id="ip" name="ip"><br><br>
                <label for="port">Please insert PORT of server!</label>
                <input type="number" id="port" name="port"><br><br>
                <button type="submit" id="submitconf">Connect</button> 
            </div>
        </div>
    </body>
</div>
<div id="mainflow">
    <button style="position: fixed; bottom: 20px; left: 20px;" type="button" onclick="window.location.href = 'http://<?php echo $_SERVER['HTTP_HOST']; ?>/test/test.php';" id="openserver">Open Server</button> 
    <button style="position: fixed; top: 20px; right: 20px;" type="button" id="clean">Clean</button> 
    <br><br>
    <div id = "status"><span class="alert-danger">DISCONNECTED</span></div>
    <br>
    <div id="response" class="hidden">
        <button type="button" id="disconnect">Disconnect</button> 
        <br><br>
        <label for="client">* Client to Send:</label>
        <input type="text" id="client" name="client"><br><br>
        <label for="message">* Message to Send:</label>
        <input type="text" id="message" name="message"><br><br>
        <button type="submit" id="sendmessage">Send Message</button> 
    </div>
    <br>
    <div><p style="font-size:0.8em">The fields marked with * are obligatory!</p></div>
</div>
<br><br>
<div id="output"></div>

<script src="assets/js/script.js"></script>


