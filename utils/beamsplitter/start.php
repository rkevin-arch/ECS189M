<?php
    preg_match('/[a-z]+/', $_GET['challenge'],$safevar);
    if($safevar[0]!=$_GET['challenge']){
        die("You're probably doing something naughty, please stop that. If not, please contact Kevin and tell me what you did.");
    }
    $challenge=$safevar[0];
    $sock = stream_socket_client('unix:///var/run/beamsplitter.sock');
    if(!$sock){
        die("Internal error. Please contact Kevin.");
    }
    fwrite($sock, 'C'.$challenge);
    $resp = fgets($sock, 1024);
    fclose($sock);
    if(strlen($resp)==0){
        die("Internal error. Please contact Kevin.");
    }
    if($resp[0]!='S'){
        die("You're probably doing something naughty, please stop that. If not, please contact Kevin and tell me what you did.");
    }
    $cookie=substr($resp,1);
    setcookie("beamsplitter_".$challenge, $cookie, time()+3600*48, '/webchal/') or die("Error setting cookie??? This should never happen. Contact Kevin.");
    header("Location: https://".$challenge.".webchal.twinpeaks.cs.ucdavis.edu/");
    exit();
?>
