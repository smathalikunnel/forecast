""" forecast.py starts a restful webservice using flask at port 5000"""

from flask import Flask,jsonify
import json
from InvalidUsage import InvalidUsage
app = Flask(__name__)

data = {"cod":"200","message":0.1239,"cnt":40,"list":[{"dt":1503511200,"main":{"temp":291.09,"temp_min":291.09,"temp_max":291.819,"pressure":1019.86,"sea_level":1027.26,"grnd_level":1019.86,"humidity":63,"temp_kf":-0.73},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":92},"wind":{"speed":4.71,"deg":271.001},"sys":{"pod":"d"},"dt_txt":"2017-08-23 18:00:00"},{"dt":1503522000,"main":{"temp":289.55,"temp_min":289.55,"temp_max":290.092,"pressure":1020.79,"sea_level":1028.31,"grnd_level":1020.79,"humidity":69,"temp_kf":-0.54},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":4.16,"deg":268},"sys":{"pod":"n"},"dt_txt":"2017-08-23 21:00:00"},{"dt":1503532800,"main":{"temp":288.29,"temp_min":288.29,"temp_max":288.649,"pressure":1021.38,"sea_level":1028.84,"grnd_level":1021.38,"humidity":78,"temp_kf":-0.36},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":44},"wind":{"speed":3.56,"deg":263.005},"sys":{"pod":"n"},"dt_txt":"2017-08-24 00:00:00"},{"dt":1503543600,"main":{"temp":286.46,"temp_min":286.46,"temp_max":286.639,"pressure":1021.66,"sea_level":1029.16,"grnd_level":1021.66,"humidity":91,"temp_kf":-0.18},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.01,"deg":261.5},"sys":{"pod":"n"},"dt_txt":"2017-08-24 03:00:00"},{"dt":1503554400,"main":{"temp":286.276,"temp_min":286.276,"temp_max":286.276,"pressure":1022.1,"sea_level":1029.58,"grnd_level":1022.1,"humidity":91,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":20},"wind":{"speed":2.91,"deg":248.002},"sys":{"pod":"d"},"dt_txt":"2017-08-24 06:00:00"},{"dt":1503565200,"main":{"temp":291.116,"temp_min":291.116,"temp_max":291.116,"pressure":1022.56,"sea_level":1030.07,"grnd_level":1022.56,"humidity":75,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":3.42,"deg":254.002},"sys":{"pod":"d"},"dt_txt":"2017-08-24 09:00:00"},{"dt":1503576000,"main":{"temp":292.969,"temp_min":292.969,"temp_max":292.969,"pressure":1022.55,"sea_level":1030.03,"grnd_level":1022.55,"humidity":67,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":76},"wind":{"speed":3.83,"deg":249.006},"sys":{"pod":"d"},"dt_txt":"2017-08-24 12:00:00"},{"dt":1503586800,"main":{"temp":293.139,"temp_min":293.139,"temp_max":293.139,"pressure":1022.46,"sea_level":1029.93,"grnd_level":1022.46,"humidity":64,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":24},"wind":{"speed":3.76,"deg":254.001},"rain":{"3h":0.01},"sys":{"pod":"d"},"dt_txt":"2017-08-24 15:00:00"},{"dt":1503597600,"main":{"temp":292.579,"temp_min":292.579,"temp_max":292.579,"pressure":1022.6,"sea_level":1030.13,"grnd_level":1022.6,"humidity":61,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":56},"wind":{"speed":3.66,"deg":263.503},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-24 18:00:00"},{"dt":1503608400,"main":{"temp":289.229,"temp_min":289.229,"temp_max":289.229,"pressure":1023.61,"sea_level":1031.13,"grnd_level":1023.61,"humidity":70,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":32},"wind":{"speed":2.41,"deg":272},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-24 21:00:00"},{"dt":1503619200,"main":{"temp":286.206,"temp_min":286.206,"temp_max":286.206,"pressure":1024.13,"sea_level":1031.69,"grnd_level":1024.13,"humidity":84,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":1.56,"deg":262},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-25 00:00:00"},{"dt":1503630000,"main":{"temp":283.963,"temp_min":283.963,"temp_max":283.963,"pressure":1023.89,"sea_level":1031.55,"grnd_level":1023.89,"humidity":97,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":1.17,"deg":252.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-25 03:00:00"},{"dt":1503640800,"main":{"temp":283.684,"temp_min":283.684,"temp_max":283.684,"pressure":1023.82,"sea_level":1031.49,"grnd_level":1023.82,"humidity":95,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.11,"deg":267},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-25 06:00:00"},{"dt":1503651600,"main":{"temp":291.227,"temp_min":291.227,"temp_max":291.227,"pressure":1024.09,"sea_level":1031.57,"grnd_level":1024.09,"humidity":73,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":1.71,"deg":143.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-25 09:00:00"},{"dt":1503662400,"main":{"temp":294.584,"temp_min":294.584,"temp_max":294.584,"pressure":1022.82,"sea_level":1030.33,"grnd_level":1022.82,"humidity":66,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":20},"wind":{"speed":1.65,"deg":147.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-25 12:00:00"},{"dt":1503673200,"main":{"temp":296.098,"temp_min":296.098,"temp_max":296.098,"pressure":1021.63,"sea_level":1029.19,"grnd_level":1021.63,"humidity":57,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":1.86,"deg":120.505},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-25 15:00:00"},{"dt":1503684000,"main":{"temp":294.832,"temp_min":294.832,"temp_max":294.832,"pressure":1020.58,"sea_level":1028.17,"grnd_level":1020.58,"humidity":54,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":2.15,"deg":109.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-25 18:00:00"},{"dt":1503694800,"main":{"temp":291.662,"temp_min":291.662,"temp_max":291.662,"pressure":1020.94,"sea_level":1028.34,"grnd_level":1020.94,"humidity":65,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":88},"wind":{"speed":2.81,"deg":98.0006},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-25 21:00:00"},{"dt":1503705600,"main":{"temp":289.7,"temp_min":289.7,"temp_max":289.7,"pressure":1020.36,"sea_level":1027.87,"grnd_level":1020.36,"humidity":79,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":76},"wind":{"speed":1.51,"deg":70.0009},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-26 00:00:00"},{"dt":1503716400,"main":{"temp":288.411,"temp_min":288.411,"temp_max":288.411,"pressure":1019.62,"sea_level":1027.18,"grnd_level":1019.62,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":88},"wind":{"speed":1.16,"deg":38.0009},"rain":{"3h":0.11},"sys":{"pod":"n"},"dt_txt":"2017-08-26 03:00:00"},{"dt":1503727200,"main":{"temp":288.21,"temp_min":288.21,"temp_max":288.21,"pressure":1019.41,"sea_level":1026.93,"grnd_level":1019.41,"humidity":92,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":24},"wind":{"speed":1.43,"deg":324.5},"rain":{"3h":0.02},"sys":{"pod":"d"},"dt_txt":"2017-08-26 06:00:00"},{"dt":1503738000,"main":{"temp":293.375,"temp_min":293.375,"temp_max":293.375,"pressure":1020.03,"sea_level":1027.53,"grnd_level":1020.03,"humidity":68,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":1.8,"deg":318.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-26 09:00:00"},{"dt":1503748800,"main":{"temp":295.072,"temp_min":295.072,"temp_max":295.072,"pressure":1019.9,"sea_level":1027.35,"grnd_level":1019.9,"humidity":61,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":1.76,"deg":312.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-26 12:00:00"},{"dt":1503759600,"main":{"temp":296.379,"temp_min":296.379,"temp_max":296.379,"pressure":1019.49,"sea_level":1026.88,"grnd_level":1019.49,"humidity":59,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"02d"}],"clouds":{"all":8},"wind":{"speed":1.82,"deg":275.006},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-26 15:00:00"},{"dt":1503770400,"main":{"temp":295.507,"temp_min":295.507,"temp_max":295.507,"pressure":1018.98,"sea_level":1026.48,"grnd_level":1018.98,"humidity":54,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.07,"deg":295.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-26 18:00:00"},{"dt":1503781200,"main":{"temp":290.346,"temp_min":290.346,"temp_max":290.346,"pressure":1019.61,"sea_level":1027.01,"grnd_level":1019.61,"humidity":74,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":1.41,"deg":317},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-26 21:00:00"},{"dt":1503792000,"main":{"temp":289.787,"temp_min":289.787,"temp_max":289.787,"pressure":1019.61,"sea_level":1027.07,"grnd_level":1019.61,"humidity":80,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":1.04,"deg":356.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-27 00:00:00"},{"dt":1503802800,"main":{"temp":289.657,"temp_min":289.657,"temp_max":289.657,"pressure":1019,"sea_level":1026.39,"grnd_level":1019,"humidity":82,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.3,"deg":324.5},"rain":{"3h":0.02},"sys":{"pod":"n"},"dt_txt":"2017-08-27 03:00:00"},{"dt":1503813600,"main":{"temp":289.314,"temp_min":289.314,"temp_max":289.314,"pressure":1018.37,"sea_level":1025.79,"grnd_level":1018.37,"humidity":89,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":1.56,"deg":310},"rain":{"3h":0.14},"sys":{"pod":"d"},"dt_txt":"2017-08-27 06:00:00"},{"dt":1503824400,"main":{"temp":290.111,"temp_min":290.111,"temp_max":290.111,"pressure":1018.29,"sea_level":1025.75,"grnd_level":1018.29,"humidity":92,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":1.04,"deg":43.0001},"rain":{"3h":0.41},"sys":{"pod":"d"},"dt_txt":"2017-08-27 09:00:00"},{"dt":1503835200,"main":{"temp":293.154,"temp_min":293.154,"temp_max":293.154,"pressure":1017.77,"sea_level":1025.29,"grnd_level":1017.77,"humidity":76,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":80},"wind":{"speed":2.07,"deg":256.502},"rain":{"3h":0.01},"sys":{"pod":"d"},"dt_txt":"2017-08-27 12:00:00"},{"dt":1503846000,"main":{"temp":292.709,"temp_min":292.709,"temp_max":292.709,"pressure":1017.48,"sea_level":1024.92,"grnd_level":1017.48,"humidity":69,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":76},"wind":{"speed":3.23,"deg":257.504},"rain":{"3h":0.09},"sys":{"pod":"d"},"dt_txt":"2017-08-27 15:00:00"},{"dt":1503856800,"main":{"temp":292.04,"temp_min":292.04,"temp_max":292.04,"pressure":1017.64,"sea_level":1025.16,"grnd_level":1017.64,"humidity":72,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":80},"wind":{"speed":3.11,"deg":292.517},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-27 18:00:00"},{"dt":1503867600,"main":{"temp":289.797,"temp_min":289.797,"temp_max":289.797,"pressure":1019.1,"sea_level":1026.53,"grnd_level":1019.1,"humidity":81,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":2.32,"deg":315.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-27 21:00:00"},{"dt":1503878400,"main":{"temp":286.11,"temp_min":286.11,"temp_max":286.11,"pressure":1019.59,"sea_level":1027.1,"grnd_level":1019.59,"humidity":100,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.22,"deg":300.011},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-28 00:00:00"},{"dt":1503889200,"main":{"temp":283.565,"temp_min":283.565,"temp_max":283.565,"pressure":1020.13,"sea_level":1027.64,"grnd_level":1020.13,"humidity":99,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.17,"deg":242},"rain":{},"sys":{"pod":"n"},"dt_txt":"2017-08-28 03:00:00"},{"dt":1503900000,"main":{"temp":283.763,"temp_min":283.763,"temp_max":283.763,"pressure":1020.57,"sea_level":1028.1,"grnd_level":1020.57,"humidity":93,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":20},"wind":{"speed":1.21,"deg":217.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-28 06:00:00"},{"dt":1503910800,"main":{"temp":291.046,"temp_min":291.046,"temp_max":291.046,"pressure":1021.48,"sea_level":1029.02,"grnd_level":1021.48,"humidity":76,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":44},"wind":{"speed":1.76,"deg":241.013},"rain":{"3h":0.0099999999999999},"sys":{"pod":"d"},"dt_txt":"2017-08-28 09:00:00"},{"dt":1503921600,"main":{"temp":293.494,"temp_min":293.494,"temp_max":293.494,"pressure":1021.69,"sea_level":1029.12,"grnd_level":1021.69,"humidity":68,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.97,"deg":235.512},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-28 12:00:00"},{"dt":1503932400,"main":{"temp":294.733,"temp_min":294.733,"temp_max":294.733,"pressure":1021.12,"sea_level":1028.55,"grnd_level":1021.12,"humidity":59,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":3.61,"deg":244.007},"rain":{},"sys":{"pod":"d"},"dt_txt":"2017-08-28 15:00:00"}],"city":{"id":2643743,"name":"London","coord":{"lat":51.5085,"lon":-0.1258},"country":"GB"}}
data = data['list']

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# @app.route("/")
# def hello():
# 	"""Basic hello method to print out the entire data"""
#     #return jsonify({'data': data['list']})
#     #return json.dumps(data['list'],indent=8)
# 	for i in range(0,len(data)):
# 		print(data[i]['weather'][0]['description'])
# 	return "blah"

# @app.route("/weather/london/<int:date>/<int:time>/temperature", methods=['GET'])
# def get_temp(date,time):
# 	return str(date)+"----"+str(time)


# A general summary of the weather:
#
#curl http://<host:ip>/weather/london/<date>/<hour minute>/
@app.route("/weather/london/<int:yyyymmdd>/<int:hhmm>/", methods=['GET'])
def get_summary(yyyymmdd,hhmm):
	""" Returns summary - description,temperature,pressure,humidity
	
	returns the summary in json format

	:param yyyymmdd: date

	:param hhmm: time

	:returns: summary in json format
	"""
	
	for i in range(0,len(data)):
		date = data[i]['dt_txt'].split(' ')[0].replace('-','')
		time = ''.join(data[i]['dt_txt'].split(' ')[1].split(':'))[0:4]

		if(date==str(yyyymmdd) and time==str(hhmm)):
			return jsonify({'description':data[i]['weather'][0]['description'],'temperature':str(int(round(data[i]['main']['temp']-273.15)))+'C','pressure':data[i]['main']['pressure'],'humidity':str(data[i]['main']['humidity'])+'%'})
			#break

		# print(date)
		# print(time)
	yyyymmdd = str(yyyymmdd)
	hhmm = str(hhmm)	
	raise InvalidUsage('No data for '+str(yyyymmdd[0:4]+'-'+yyyymmdd[4:6]+'-'+yyyymmdd[6:8])+' '+str(hhmm[0:2]+':'+hhmm[2:4]), status_code=410)

# curl http://<host:ip>/weather/london/<date>/<hour minute>/temperature
# e.g. curl http://<host:ip>/weather/london/20160706/0900/temperature/
# {
#   "temperature": "15C"
# }
@app.route("/weather/london/<int:yyyymmdd>/<int:hhmm>/temperature", methods=['GET'])
def get_temp(yyyymmdd,hhmm):
	
	for i in range(0,len(data)):
		date = data[i]['dt_txt'].split(' ')[0].replace('-','')
		time = ''.join(data[i]['dt_txt'].split(' ')[1].split(':'))[0:4]

		if(date==str(yyyymmdd) and time==str(hhmm)):
			return jsonify({'temperature':str(int(round(data[i]['main']['temp']-273.15)))+'C'})
			
	yyyymmdd = str(yyyymmdd)
	hhmm = str(hhmm)	
	raise InvalidUsage('No data for '+str(yyyymmdd[0:4]+'-'+yyyymmdd[4:6]+'-'+yyyymmdd[6:8])+' '+str(hhmm[0:2]+':'+hhmm[2:4]), status_code=410)


# curl http://<host:ip>/weather/london/<date>/<hour minute>/pressure
# e.g. curl http://<host:ip>/weather/london/20160706/0900/pressure/
# {
#   "pressure": "1028.12"
# }
@app.route("/weather/london/<int:yyyymmdd>/<int:hhmm>/pressure", methods=['GET'])
def get_pressure(yyyymmdd,hhmm):
	
	for i in range(0,len(data)):
		date = data[i]['dt_txt'].split(' ')[0].replace('-','')
		time = ''.join(data[i]['dt_txt'].split(' ')[1].split(':'))[0:4]

		if(date==str(yyyymmdd) and time==str(hhmm)):
			return jsonify({'pressure':data[i]['main']['pressure']})

	yyyymmdd = str(yyyymmdd)
	hhmm = str(hhmm)	
	raise InvalidUsage('No data for '+str(yyyymmdd[0:4]+'-'+yyyymmdd[4:6]+'-'+yyyymmdd[6:8])+' '+str(hhmm[0:2]+':'+hhmm[2:4]), status_code=410)

# curl http://<host:ip>/weather/london/<date>/<hour minute>/humidity
# e.g. curl http://<host:ip>/weather/london/20160706/0900/humidity/
# {
#   "humidity": "88%"
# }
@app.route("/weather/london/<int:yyyymmdd>/<int:hhmm>/humidity", methods=['GET'])
def get_humidity(yyyymmdd,hhmm):
	
	for i in range(0,len(data)):
		date = data[i]['dt_txt'].split(' ')[0].replace('-','')
		time = ''.join(data[i]['dt_txt'].split(' ')[1].split(':'))[0:4]

		if(date==str(yyyymmdd) and time==str(hhmm)):
			return jsonify({'humidity':str(data[i]['main']['humidity'])+'%'})
	yyyymmdd = str(yyyymmdd)
	hhmm = str(hhmm)	
	raise InvalidUsage('No data for '+str(yyyymmdd[0:4]+'-'+yyyymmdd[4:6]+'-'+yyyymmdd[6:8])+' '+str(hhmm[0:2]+':'+hhmm[2:4]), status_code=410)


if __name__ == '__main__':
    app.run()