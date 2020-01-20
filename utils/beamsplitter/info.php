<?php
    preg_match('/[a-z]+/', $_GET['challenge'],$safevar);
    if($safevar[0]!=$_GET['challenge']){
        die("You're probably doing something naughty, please stop that. If not, please contact Kevin and tell me what you did.");
    }
    $challenge=$safevar[0];
    echo('<meta http-equiv="refresh" content="0; url=start/'.$challenge.'">');
    echo('Setting up challenge environment for '.$challenge.', please wait...<br>');
    echo('This process will take a while (~10 secs), please be patient!<br>');
    echo('Note: You can revisit this link to spin up a new container if you messed up the old one.');
?>
