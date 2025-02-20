from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/brent-data', methods=['GET'])
def get_brent_data():
    # This endpoint will serve processed analysis data.
    return jsonify({"message": "Brent oil price analysis data goes here"})

if __name__ == '__main__':
    app.run(debug=True)
