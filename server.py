from flask import Flask
from scripts.stock_twits import 

# from scripts.stock_twits import Requests, ST_BASE_URL, ST_BASE_PARAMS

app = Flask(__name__)

@server.route('/')
def index():
    return 'Hello'




if __name__ == "__main__":
    server.run(debug=True)