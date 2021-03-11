import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration
import os

sentry_sdk.init(
    dsn="https://949082c275e845ada6919a4d7043a42f@o547461.ingest.sentry.io/5669685",
    integrations=[BottleIntegration()]
)

app = Bottle()
  
@app.route('/success') 
def success():
	html = """
<!doctype html>
<html lang="en">
  <head>
    <title>SUCCESS</title>
  </head>
  <body>
    <div class="container">
      <h1>200 it's OK!</h1>
    </div>
  </body>
</html>
	"""	
	return html

@app.route('/') 
def success():
	html = """
<!doctype html>
<html lang="en">
  <head>
    <title>HELLO!</title>
  </head>
  <body>
    <div class="container">
      <h1>HELLO WORLD!</h1>
    </div>
  </body>
</html>
	"""	
	return html

@app.route('/fail')
def fail():  
    raise RuntimeError("Status: 400.")  
    return  


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)