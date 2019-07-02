from flask import Flask, render_template, jsonify, send_from_directory
app = Flask(__name__)

# add favicon for website
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route("/")
def root():
    return render_template('index.html')




# @app.route('/bikes2weeks/<station_address>')
# def bikes_available_2weeks(station_address):
#     """ This function retrives the bike availability for the previous 14 days at the current hour. It expects the station
#         address as its input and returns the number of bikes available indexed by the date. """
#
#     # get current date
#     date = datetime.datetime.now()
#     # remove trailing minutes (to check for available bikes during this hour)
#     date = date.replace(minute=0, second=0, microsecond=0)
#     # convert time to hours only
#     hour = date.strftime("%X")
#
#     # add 59 minutes and 59 seconds for SQL query and format it correctly
#     datePlusOneHour = date + timedelta(hours=1) - timedelta(seconds=1)
#     datePlusOneHour = str(datePlusOneHour)
#     datePlusOneHour = datePlusOneHour.split(" ")[1]
#
#     # fix the URL request for a specific station
#     station_address = station_address
#     station_address = station_address.replace("_", " ")
#
#     # build query
#     static_query1 = """ SELECT avg(available_bikes), last_update
#                 FROM all_station_info
#                 WHERE cast(last_update as time) between \'"""
#     static_query2 = hour + "\' and \'" + str(datePlusOneHour)
#     static_query3 = "\' AND address=\'" + station_address
#     static_query4 = "\' AND last_update >= now() - INTERVAL 14 DAY Group by CAST(last_update AS DATE);"
#     constructedQuery = static_query1 + static_query2 + static_query3 + static_query4
#
#     # Holds average bikes organised by hour
#     daily_available_bikes = {}
#
#     rows = open_connection(constructedQuery)
#
#     for row in rows:
#         weekday = row[1].strftime('%x')
#         daily_available_bikes[weekday] = round(row[0])
#
#     return jsonify(daily_available_bikes)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)