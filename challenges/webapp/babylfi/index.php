<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: babylfi</title>
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
            .flag{
              font-family: monospace;
              font-weight: bold;
            }
            .output {
              white-space: pre-wrap;
            }
        </style>
    </head>
    <body class="container">
        <div class="twelve columns border boxshadow">
            <div class="row">
                <h3>Shakespearean Sonnets</h3>
            </div>
            <div class="row">
                <p>Feel free to enter a number between 1 and 154 to view a Shakespeare sonnet.</p>
            </div>
            <form>
                <input type="text" placeholder="file" name="file"><br>
                <button type="submit">Read</button><br>
            </form>
            <pre class="row output"><?php if(isset($_REQUEST["file"])) echo file_get_contents("/var/www/sonnets/".$_REQUEST["file"]);?></div>
        </div>
    </body>
</html>
