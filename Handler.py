#SECTION - Modules
from _init_ import Database, key, CalulateStats;from pymongo import MongoClient;from cryptography.fernet import Fernet;import time, json
from smtplib import SMTP, SMTPException; 
from email import encoders; from email.mime.base import MIMEBase; from email.mime.multipart import MIMEMultipart; from email.mime.text import MIMEText
from Email import *


# SECTION - Client / Admin -- Booking manage
class System:
    def __init__(self, data: dict = None):
        self.config = Client = MongoClient("mongodb+srv://Admin:UlYgVuBdiZ9SvRmu@database.aqgh5a5.mongodb.net/?retryWrites=true&w=majority")
        self.done_calculation = False  # Flag to indicate if calculations are done
        if (data != None):
            print("System initialized | Database, Waiting for Inquired Information to be Processed")
            return self.Processing(data)
        return print("System initialized | Database, Waiting for Requests")
    def Processing(self, configs):
        """
        This function is used to decode the data that is sent from the client.
        It takes in the data as a string and returns the decoded data as a python object.
        """

        print("Processing Information")
        print("Encrypting...")
        for config in configs.keys():
            #x = json.dumps(configs, indent=2)
            #new = Fernet(key().Encry_Key()).encrypt(x.encode("utf-8")) 
            #print(configs)
            continue
        print("Encrypted")
        print("Processing Complete | Database initialized, Storing Encrypted Data Process Start")
        self.Store(configs, True)
    def Store(self, data=None, Debug=False):
        """
        This function is used to encode the data that is sent to the client.
        It takes in the data as a python object and returns the encoded data as a string.
        """
        Database(self.config).add_Indexes(data)
        print("Storing Complete | System pending..., Redirect Sent to Client")
        return
    def Clients(self):
        """ This function is used to return the data from the database. It takes in the data as a python object and sent to admin """
        return Database(self.config).get_indexes()
    def Stats(self):
        try:
            amount = CalulateStats().getAmount()
            Database(self.config).Update(file='Total Amount', Value=amount)
            self.done_calculation = True  # Set flag to True after calculations are done
            self.reset_key_file()
            return Database(self.config).get_statics()
        except Exception as e:
            print(f"An error occurred while processing stats: {e}")
            return 
    
    def Unavailable(self):
        try:
            Dates = Database(self.config).get_Dates()
            #Data
        except (TimeoutError, Exception) as e:
            raise("An error occurred:", e.errno)
        finally:
            print(Dates)
            return json.dumps(Dates, indent=2, default=str)
            #Data
        
    def reset_key_file(self):
        if self.done_calculation:
            with open('keys/Amount.key', 'w') as key:
                key.write('0')
                print("Key file reset to 0.")
    def Change(self, id):
        Database(self.config).change_index(id)
        
# SECTION - Admin Accept
class _(SMTP):
    def __init__(self, host: str = "", port: int = 0, Name : str = "", Email : str = "", Date : str = "", Time : str = "", id : str = "") -> None:
        self.Name = Name
        self.Email = Email
        self.Date = Date
        self.Time = Time
        self._id = id
        super().__init__(host, port)
    
    def MimeConfig(self):
        Main = MIMEMultipart("alternative")
        From = Main['From'] = "bernard.mantlaka@gmail.com"
        To = Main['To'] = self.Email
        Main['Subject'] = "Appointment Is Accepted"
        body = MIMEText(Accept.format(self.Name, self.Date, self.Time, "066 558 3774"), 'html')
        Main.attach(body)
        
        return From, To , Main
    def Accept(self):
        try:
            From, to, body =  self.MimeConfig()
            print(From, to, body)
            self.Config()
            self.Send(From, to, body)
        except ConnectionError as e:
            raise("An error occurred:", e)
        return
    
    def Reject(self):

        try:
            with open("Messages/Message.json", "r") as file:
                r =  json.loads(file.read(1024)); string = r["Decline"]
                req = string.format(r["Subject"].format('Declined'), self.Name,self.Date,self.Time)  
                self.Config()
                self.Send(self.Email, req)   
        except Exception as e:
            raise("An error occurred:", e)

        return
    
    def Config(self):
        try:
            self.ehlo(); self.starttls(); self.ehlo()
            self.login("bernard.mantlaka@gmail.com", "rlpy dgvb rddv ksro")  
        except Exception as e:
            raise("An error occurred", e)
        return 
    
    def Send(self,From, recipient, msg):
        try:
            self.sendmail(From, f"{recipient}", msg.as_string()); self.quit()
            System(None).Change(self._id)
        except ConnectionError as e:
            raise("An error occurred", e)
        return
    pass







