from flask import Flask, jsonify, request
from flask_cors import CORS

from collector import callmodule

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/data')    

def get_data():
    # Get sport type
    sport = request.args.get('sport')
    league = request.args.get('league')
    data = callmodule(sport, league)
    if data is None:
        # Return a 404 error response if data is not found
        return jsonify({'error': 'Data not found'}), 404
    else:
        # Return a JSON response with the data
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
