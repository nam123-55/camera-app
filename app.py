from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": now}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
