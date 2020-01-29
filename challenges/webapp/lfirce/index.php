<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: lfirce</title>
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
            .output {
              white-space: pre-wrap;
            }
        </style>
    </head>
    <body class="container">
        <div class="twelve columns border boxshadow">
            <div class="row">
                <h3>Elizabeth Barrett Browning Sonnets</h3>
            </div>
            <div class="row">
                <p>Feel free to enter a number between 1 and 44 to view an Elizabeth Barrett Browning sonnet.</p>
            </div>
            <form>
                <input type="text" placeholder="file" name="file"><br>
                <button type="submit">Read</button><br>
            </form>
            <pre class="row output"><?php if(isset($_REQUEST["file"])) include("/var/www/sonnets/".$_REQUEST["file"]);?></div>
        </div>
    </body>
</html>
