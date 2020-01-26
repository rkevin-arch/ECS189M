<?php
include 'db.php';
if(isset($_REQUEST["username"])){
    $query = "SELECT * FROM users WHERE username='".$_REQUEST["username"]."' AND password='".$_REQUEST["password"]."'";
    $result = mysqli_query($mysql_conn, $query);
    if(!$result){
        $msg="There's an error when executing the SQL query.";
    } else if(mysqli_num_rows($result)==0){
        $msg="Username and password combo incorrect.";
    } else {
        $msg="You are now logged in! Unfortunately, there's nothing here. The flag is my password. Good luck!";
    }
} else {
    $msg = "";
}
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: bsqli</title>
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
                <h3>My even better login page</h3>
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
