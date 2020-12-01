from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(err):
    return 'Oops. Page Not Found!'