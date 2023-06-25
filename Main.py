from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process_json():
    content = request.json
    print(json.dumps(content, indent=4))
    return 'OK'


if __name__ == '__main__':
    app.run(port=9500, debug=True)
