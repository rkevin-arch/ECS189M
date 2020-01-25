<?php
include 'db.php';
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: searchbar</title>
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
                <h3>Inventory system</h3>
                <h5>Please use the search bar to search for items in our inventory!</h5>
            </div>
            <form>
                <input type="text" placeholder="Item to search for" name="query">
                <button type="submit">Search</button>
            </form>
            <?php
                if(isset($_REQUEST["query"])){
                    $query="SELECT item,count FROM inventory WHERE item LIKE '%".$_REQUEST["query"]."%'";
                } else {
                    $query="SELECT item,count FROM inventory";
                }
                $result = mysqli_query($mysql_conn, $query);
                if(!$result){
                    echo "<pre>".mysqli_error($mysql_conn).'</pre>';
                } else {
                    echo "<table><tr><th>Item</th><th>Count</th></tr>\n";
                    while( $row = mysqli_fetch_assoc( $result ) ) {
                        $item = $row["item"];
                        $count = $row["count"];
                        echo "<tr><td>{$item}</td><td>{$count}</td></tr>\n";
                    }
                    echo "</table>";
                }
            ?>
        </div>
    </body>
</html>
