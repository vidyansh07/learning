from flask import Flask
from views import views
app = Flask(__name__)

app.register_blueprint(views, url_prefix='/')


# @app.route("/")
# def home():
#     return "Hello your are on home page." # Normaly it should be a HTML page...

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
    # debug is True for authmatically running tests and without rerunning the full project
    # port is the port that the server will run on.