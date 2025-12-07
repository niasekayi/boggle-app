from flask import Flask, request, jsonify
from backend.boggle import Boggle

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve_boggle():
    data = request.get_json()

    grid = data.get("grid")
    dictionary = data.get("dictionary")

    if not grid or not dictionary:
        return jsonify({"error": "Grid and dictionary required"}), 400

    game = Boggle(grid, dictionary)
    solution = game.getSolution()

    return jsonify({"solution": solution})

if __name__ == "__main__":
    app.run(port=5000)
