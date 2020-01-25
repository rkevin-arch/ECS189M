from bottle import route, run, request, response

TEMPLATE="""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: adminme</title>
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
            <h3>Flag dispenser</h3>
        </div>
        <div class="row">Welcome to the flag dispenser!</div>
        <div class="row" style="overflow-wrap: break-word;">%s</div>
        </div>
    </body>
</html>
"""
NOFLAG=TEMPLATE%"Unfortunately, you must be an admin to get the flag. Login is currently closed."
FLAG=TEMPLATE%"Welcome back, admin! Here's your flag: ECS{15_4DM1N_TRU3_9C8861B05695569D3F67382254CD170B}"

@route('/')
def index():
    if request.get_cookie("is_admin","0") == "0":
        response.set_cookie("is_admin","0")
        return NOFLAG
    return FLAG

run(host='0.0.0.0',port=8080)
