from flask.json import jsonify
from flask import Flask, render_template, request
from interpark import EMPinter


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET"])
def basic():


    if request.method =="GET":
        return render_template('travel_index.html')
    

@app.route('/info', methods=["GET"])
def box():
    # print(x)
    
  
    return EMPinter().excl_data(request.form.get("page_num"))


@app.route('/information', methods=["POST"])
def craw():
    
    
    return EMPinter().craw_data(request.form.get("page_num"))


@app.route('/chart_info', methods=["post"])
def chart():

  
    return EMPinter().chart_data(request.form.get("chart_num"))


if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")