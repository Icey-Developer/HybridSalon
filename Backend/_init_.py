import secrets
from cryptography.fernet import Fernet;import smtplib, json,  flask
from datetime import datetime
import calendar
from bson.objectid import ObjectId
from pymongo import MongoClient


class Wrapper(object):
    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)
    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def run(self, **kwargs):
        self.app.run(**kwargs)

class Database(object):
    def __init__(self, config,**kwargs) -> None: # - Initiating / Connecting to the database
        self.DB = config["Database"]
        self.stats_db = config["Statics"]
        self.Query_Col = self.DB["Clients"]
        
        return None
    
    def add_Indexes(self, dict=None):
        self.Query_Col.insert_one(dict)
    def get_indexes(self):
        Clients = []
        for index in self.Query_Col.find({}):
            # Convert ObjectId to string
            try:
                index['_id'] = str(index['_id'])
                #converting encrypted to decrypted
                self.decryt = index['details']
                #self.decryt = Fernet(key().Encry_Key()).encrypt((self.decryt).encode())
                print(self.decryt)
                Clients.append(index)
            except Exception as e:
                raise(e)
            finally:
                print("Processed!")
        return json.dumps(Clients, indent=2, default=str).encode('utf-8')
    
    def Update(self, file : str = '', Value : int | str = None):
        Arr = []
        today = datetime.today()
        datem = today.month

        try:
            x = self.stats_db[file].update_one({"Month" : calendar.month_name[datem]}, {"$set" : {"Value" : Value} })
            print(Value, "documents updated")
        except ConnectionError as e:
            return e
        finally:
            return 


    def get_statics(self):
        Arr = []

        today = datetime.today()
        datem = today.month

        try:
            for l in self.stats_db['Total Amount'].find({"Month" : calendar.month_name[datem]},{}):
                print(l)
            for i in self.stats_db['Current Popular Style'].find({"Month" : calendar.month_name[datem]},{}):
                print(i)
            s = self.DB['Clients'].count_documents({})
            t = self.stats_db["Total Appointments"].count_documents({})

            for c in self.stats_db['Total Amount'].find({"Month" : calendar.month_name[datem]},{}):
                print(c['Value'])
            
            for p in self.stats_db['Total Amount'].find({"Month" : calendar.month_name[datem-1]},{}):
                print(p['Value'])
            Arr.append(l); Arr.append(i); Arr.append(s); Arr.append(t)
            Arr.append(c['Value']); Arr.append(p['Value'])
        except ConnectionError as e:
            raise(f"Connect Error: {e}")
        finally:
            pass
        return json.dumps(Arr, indent=2, default=str).encode('utf-8')
    def change_index(self, id):
        client = self.Query_Col.find({"_id" : ObjectId(id)})
        for index in client:
            print(index)
        
        self.stats_db['Total Appointments'].insert_one(index)
        self.Query_Col.delete_one({"_id" : ObjectId(id)})
        return
    
    def get_Dates(self):
        Array = []
        try:
            for d in self.stats_db['Total Appointments'].find():
                print(d.get('D$T')['Date'])
                Array.append(d.get('D$T')['Date'])
        except (ConnectionError, IndexError, TimeoutError, ValueError) as e:
            print("encountered an error : {e}".format(e))
        finally:
            return Array

    def getCoiffureStats(self):
        try:
            for x in self.stats_db['Total Appointments'].find():
                print(x.get('Coiffure')['l'])   
        except ConnectionError as e:
            print(f"Connection Error: {e}")
        finally:
            return x.get('Coiffure')['l'], x.get('Coiffure')['s'], x.get('Coiffure')['e']
class key():
    def __init__(self) -> None: return

    def timeout(self) -> int: return 

    def generate(self, length=32) -> id:
        """Generate a random API key."""
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    def Encry_Key(self) -> bytes:
        with open("keys/Secret.key", "r") as file:
            p = file.read()

        return p.encode()

class CalulateStats:
    def __init__(self) -> None:
        self.config = Client = MongoClient("mongodb+srv://Admin:UlYgVuBdiZ9SvRmu@database.aqgh5a5.mongodb.net/?retryWrites=true&w=majority")
        return
    
    def split(self):
        l, s, e = Database(self.config).getCoiffureStats()  # Assuming this method returns strings containing numeric values
        extract = int(''.join(x for x in l if x.isdigit())) + int(''.join(x for x in s if x.isdigit())) + int(''.join(x for x in e if x.isdigit()))
        print(extract)
        return extract

    def getAmount(self):
        try:
            with open('keys/Amount.key', 'r+') as key:
                amount_from_file = int(key.read())
                amount_to_update = amount_from_file + self.split()
                print(amount_to_update)

                return self.Upd(amount_to_update)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def Upd(self, new_amount) -> None:
        try:
            with open('keys/Amount.key', 'r+') as key:
                prev_amount = int(key.read())
                updated_amount = prev_amount + new_amount + new_amount
                key.write(str(updated_amount))
            return updated_amount
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
