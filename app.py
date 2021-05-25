
'''
Created on 
    

Course work: 18-05-2021
    

@author: 
    Ana Jessica

Source:
    
'''

from flask import Flask,render_template, jsonify, request
import json
import species


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = species.get_data()

    # result_dict = {

    #     'year'       : year,
    #     'pytorch'    : pytorch,
    #     'tensorFlow' : tensorFlow

    # }

    return jsonify(result)

'''
http://0.0.0.0:3091/api/add
http://0.0.0.0:3091/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

   # year            = request.values.get('year')
    Treespecies = request.values.get('Tree species')
    PercentageInOntario  = request.values.get('Percentage in Ontario')

    result = {
        'Tree species'       : Treespecies,
        'Percentage in Ontario'    : PercentageInOntario,

    }
    result_data = species.add_row(Treespecies,PercentageInOntario )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
