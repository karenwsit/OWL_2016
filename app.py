from flask import Flask
import twitter_streaming

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'




if __name__ == "__main__":
    app.run(debug=True)