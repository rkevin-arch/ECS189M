<?php
    preg_match('/[a-z]+/', $_GET['challenge'],$safevar);
    if($safevar[0]!=$_GET['challenge']){
        die("You're probably doing something naughty, please stop that. If not, please contact Kevin and tell me what you did.");
    }
    $challenge=$safevar[0];
    $sock = stream_socket_client('unix:///var/run/beamsplitter.sock');
    if(!$sock){
        die("You should never see this error! If you do, yell at Kevin and tell him that beamsplitter has died.");
    }
    fwrite($sock, 'C'.$_SERVER['REMOTE_ADDR'].'_'.$challenge);
    $resp = fgets($sock, 1024);
    fclose($sock);
    if(strlen($resp)==0){
        die("Internal error. Please contact Kevin and tell him beamsplitter broke while spinning up container.");
    }
    if($resp[0]!='S'){
        die("You're probably doing something naughty, please stop that. If not, please contact Kevin and tell me what you did.");
    }
    $cookie=substr($resp,1);
    setcookie("beamsplitter_".$challenge, $cookie, time()+3600*48, '/', 'twinpeaks.cs.ucdavis.edu', false, true) or die("Error setting cookie??? This should never happen. Contact Kevin.");
    header("Location: https://".$challenge.".webchal.twinpeaks.cs.ucdavis.edu/");
    exit();
?>
