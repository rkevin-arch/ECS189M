from bottle import route, run, request, response

TEMPLATE="""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>ECS189M Web Challenge: adminme</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Raleway:400,300,600">
        <link rel="stylesheet" href="https://skeleton-framework.github.io/css/normalize.css">
        <link rel="stylesheet" href="https://skeleton-framework.github.io/css/skeleton.css">
    </head>
    <body>
        <h1>Flag dispenser</h1>
        <p>Welcome to the flag dispenser!</p>
        <p>%s</p>
    </body>
</html>
"""
NOFLAG=TEMPLATE%"Unfortunately, you must be an admin to get the flag. Login is currently closed."
FLAG=TEMPLATE%"Welcome back, admin! Here's your flag: <code>ECS{15_4DM1N_TRU3_9C8861B05695569D3F67382254CD170B}</code>"

@route('/')
def index():
    if request.get_cookie("is_admin","0") == "0":
        response.set_cookie("is_admin","0")
        return NOFLAG
    return FLAG

run(host='0.0.0.0',port=8080)
