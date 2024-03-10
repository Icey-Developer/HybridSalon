#SECTION - Modules // Params
#- Web Routes // Flask
import os
from _init_ import Wrapper, Database, key; from flask import Flask, render_template, redirect, url_for, abort, request, Response, jsonify;from flask_cors import CORS; from Handler import System, _
# - Web Database // MongoDB
from pymongo.mongo_client import MongoClient; from pymongo.server_api import ServerApi; import secrets;import json


#SECTION - Database config // MongoDB config
flask_Web = Flask(__name__, static_folder="staticFiles", template_folder="templates"); Web = Wrapper(flask_Web)
Client = MongoClient("mongodb+srv://Admin:UlYgVuBdiZ9SvRmu@database.aqgh5a5.mongodb.net/?retryWrites=true&w=majority"); DB = Database(Client)
CORS(flask_Web)

#SECTION

# - Requests
@flask_Web.route("/Booking/success?&transaction_id=<id>")
def Complete(id):
    return render_template('Routes/Redirect.html')
@flask_Web.route('/Redirect:About', methods=['GET', 'POST'])
def Redirect():
    if request.method == 'POST':
        Data = request.get_json(True)
        if (Data):
            System(Data)
            print("Valid Inquired Information found... Sent to Processing")
        else:
            return "Invalid / None Inquired information found"
        
        # Process the data as needed
    # After processing or if it's a GET request, redirect to the Complete endpoint
    return redirect(url_for('Complete', id=str(key().generate()))) 
@flask_Web.route('/Admin/req/Clients', methods=['GET'])
def GetClients():
    try:
        res = System(None).Clients()
    except ValueError as e:
        return jsonify({'error': 'Bad Request','message': 'Invalid JSON format in request body.'}), 400
    return res
@flask_Web.route('/Accept/req/Client', methods=['GET', 'POST'])
def AcceptClient():
    if 'Content-Type' not in request.headers:
        return jsonify({'error': 'Missing Content-Type header', 'message': 'Please include Content-Type header with value "application/json".'}), 400

    # Check if the Content-Type header is 'application/json'
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Unsupported Media Type', 'message': 'This API only supports JSON data.'}), 415

    try:
        # Try to parse the JSON data from the request body
        json_data = request.data.decode()

    except TypeError as e:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid JSON format in request body.'}), 400
    finally:
        s = _("smtp.gmail.com", 587,json.loads(json_data)['n'], json.loads(json_data)['e'], json.loads(json_data)['d'],json.loads(json_data)['t'],json.loads(json_data)['i'])
        s.Accept()
        pass
    

    # Process the JSON data as needed
    # Return a success response
    return jsonify({'message': 'Request successfully received.', 'data': json_data}), 200
@flask_Web.route('/Decline/req/Client', methods=['POST'])
def DeclineClient():
    if 'Content-Type' not in request.headers:
        return jsonify({'error': 'Missing Content-Type header', 'message': 'Please include Content-Type header with value "application/json".'}), 400

    # Check if the Content-Type header is 'application/json'
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Unsupported Media Type', 'message': 'This API only supports JSON data.'}), 415

    try:
        # Try to parse the JSON data from the request body
        json_data = request.data.decode()

    except TypeError as e:
        return jsonify({'error': 'Bad Request', 'message': 'Invalid JSON format in request body.'}), 400
    finally:
        s = _("smtp.gmail.com", 587,json.loads(json_data)['n'], json.loads(json_data)['e'], json.loads(json_data)['d'],json.loads(json_data)['t'],json.loads(json_data)['i'])
        s.Reject()
        pass
    

    # Process the JSON data as needed
    # Return a success response
    return jsonify({'message': 'Request successfully received.', 'data': json_data}), 200
    return
@flask_Web.route('/Admin/req/Stats', methods=['GET'])
def GetStats():
    try:
        res = System(None).Stats()
    except TypeError as e:
        print(f"Error occurred : {e}")
    finally:
        return res


# - Routes
@flask_Web.route("/Policy")
def Policy():
    return render_template("Routes/Policy.html")
@flask_Web.route("/Home")
def Home():
    return render_template("Routes/Braids.html")
@flask_Web.route("/Schedule")
def Schedule():
    return render_template("Routes/Schedule_Braids.html")

# - Api
@flask_Web.route("/api/set", methods=['GET', 'POST'])
def Api_Book():
    if request.method == 'POST':
        Data = request.get_json(True)
        if (Data):
            with open('templates/Json/Prices.json', 'w') as new:
                new.write(json.dumps(Data['Set']))
                print(Data['Set'])
            
            with open('templates/Json/Showcase.json', 'w') as New:
                New.write(json.dumps(Data['Showcase']))
                print(Data['Showcase'])

            print("Updated!")
        else:
            return jsonify("Invalid / None Inquired information found")
        
        # Process the data as needed
    # Read data from a JSON file
    
    with open('templates/Json/Prices.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@flask_Web.route("/api/show", methods=['GET', 'POST'])
def Api_show():
    with open('templates/Json/Showcase.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@flask_Web.route("/Announcement", methods=['POST'])
def Announcement():
    if request.method == 'POST':
        Data = request.data
        if not Data:
            return "Invalid Data/ No such instance as 'Data' found"
        with open('Messages/Announcement.json', 'w') as Announce:
            Announce.write(Data.decode())
    return jsonify("Successful Request & Json Parsing")

@flask_Web.route("/Unavailable/Date", methods=['GET'])
def Date():
    if request.method == 'GET':
        try:
            data = System(None).Unavailable()
            print(data)
        except KeyError as e:
            print(f"Error occurred : {e}")

    return data

@flask_Web.route("/Get/Available-time", methods=['GET'])
def Time():
    try:
        with open('Messages/Announcement.json', "r") as key:
            data = key.read()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error occurred: Unable to read the file."

    

# - Initiated
if __name__ == "__main__":
    Web.run(debug=True, host='0.0.0.0')
    
