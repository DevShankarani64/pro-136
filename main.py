from flask import Flask 
app=Flask(__name__)
app.route("/")
def index():
	return"Index"
if __name__ == "__main__":
	app.run



from flask import Flask,jsonify 
from data import data 
app.route("/")
def index():
	return jsonify({
"data":data,
"message":"success"
}),200


@app.route("/planet") 
def planet(): 
	name = request.args.get("name") 
	planet_data = next(item for item in data if item["name"] == name) 
	return jsonify({ 
"data": planet_data, "message": "success" }), 200 
if __name__ == "__main__": 
	app.run()
