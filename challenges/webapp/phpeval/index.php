<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: phpeval</title>
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
        <div class="six columns offset-by-three border boxshadow">
            <div class="row">
                <h3>Execute PHP</h3>
            </div>
            <div class="row">
                <p>I'm very clever, so I left a backdoor on my own system below, just in case I lock myself out. Surely no one will abuse this.</p>
            </div>
            <form>
                <textarea class="u-full-width" placeholder="code" name="code" style="min-height: 200px;"></textarea>
                <button type="submit">Execute</button><br>
            </form>
            <div class="row"><?php if(isset($_REQUEST["code"])) echo eval($_REQUEST["code"])?></div>
        </div>
    </body>
</html>
