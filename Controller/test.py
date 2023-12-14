# this file was written, in its entirety at this point, by Sayantan Datta, I (Ethan Virgil) uploaded it as he was having trouble pushing to this repo
from flask import Flask, render_template, request
from Model.CheapestFlightSearcher import CheapestFlightSearcher
from Model.adjacencymatrix import AdjacencyMatrix
matrix = AdjacencyMatrix("Model/Flight Data - Sheet1.csv")
airport_code_to_index_dict = {flight_label: index for index, flight_label in enumerate(matrix.get_vertices())}
usd_searcher = CheapestFlightSearcher(matrix.get_USD_matrix(), airport_code_to_index_dict)
ghg_searcher = CheapestFlightSearcher(matrix.get_GHG_matrix(), airport_code_to_index_dict)
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('UI.html')

@app.route('/result', methods=['GET'])
def result():
    destination = request.args.get('destination')
    origin = request.args.get('origin')
    path = usd_searcher.search(origin, destination)


    print(f"Origin: {origin}")
    print(f"Destination: {destination}")

    return render_template('result.html', origin=origin, destination=destination)

if __name__ == "__main__":
  app.run(debug=True)
