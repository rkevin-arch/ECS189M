<?php
include 'db.php';
if(isset($_REQUEST["username"])){
    if(stripos($_REQUEST["username"],"or")===false && stripos($_REQUEST["username"],"or")===false){
        $query = "SELECT * FROM users WHERE username='".$_REQUEST["username"]."' AND password='".$_REQUEST["password"]."'";
        $result = mysqli_query($mysql_conn, $query);
        if(!$result){
            $msg=mysqli_error($mysql_conn);
        } else if(mysqli_num_rows($result)==0){
            $msg='Username and password combo incorrect.';
        } else {
            $msg='You are now logged in! Your flag is: ECS{H1_8088Y_94C0EE1CEB1EE342665E7833C728090B}';
        }
    } else {
        $msg = 'I have added the restriction that you may not have the string "or" in your query! I heard it leads to bad stuff.';
    }
} else {
    $msg = "";
}
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: sqli</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Raleway:400,300,600">
        <link rel="stylesheet" href="https://skeleton-framework.github.io/css/normalize.css">
        <link rel="stylesheet" href="https://skeleton-framework.github.io/css/skeleton.css">
        <style>
            .border {
              padding: 2.5rem 3rem;
              border: 1px solid #E1E1E1;
              border-radius: 4px;
            }
        </style>
    </head>
    <body class="container">
        <div class="twelve columns border boxshadow">
            <div class="row">
                <h3>My login page</h3>
            </div>
            <form>
                <input type="text" placeholder="username" name="username"><br>
                <input type="password" placeholder="password" name="password"><br>
                <button type="submit">Login</button><br>
            </form>
            <div class="row"><?php echo $msg; ?></div>
        </div>
    </body>
</html>