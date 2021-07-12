from flask import Flask
from flask import jsonify
import os
import signal
import time

app = Flask(__name__)

messages = []


@app.get("/messages")
def get_all_messages():
    return jsonify(messages)


@app.get("/createmessage/<note>")
def create_message(note: str):
    message = {'note': note, 'timestamp': time.strftime("%m/%d/%Y, %H:%M:%S")}
    messages.append(message)
    return jsonify(message)


@app.get("/shutdown")
def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
