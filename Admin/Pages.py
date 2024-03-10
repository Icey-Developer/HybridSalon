import flet
from flet import *
from Controls import *
from Properties import *
import requests
from ast import literal_eval
import json
from datetime import datetime
import re
import calendar
from Controls import *


def get_(url):

    r = requests.get(url)
    return r

def get_statics(url):
    r = requests.get(url)
    return r


def Loading(page):
    return View(
        route='/Loading',
        controls=[
            Column([
                ft.Image(src='Images/blb.png', width=200,height=200),
                ft.Text(**Title("Blues Lavish Braids"),font_family="Brusher", text_align=TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ],
        bgcolor='#fbe5fe', horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER
    )


def Dashboard(page):
    stats = get_statics('http://10.0.0.148:5000/Admin/req/Stats')
    Amount = json.loads(stats.text)[0]
    Popular = json.loads(stats.text)[1]
    curr = json.loads(stats.text)[4]
    prev = json.loads(stats.text)[5]

    print(type(curr), type(prev))
    return View(
        route='/Web-Admin/@Dashboard',
        controls=[
            Container(**BG(), content=ft.Column([Branding("BLUE"),
                                                 ft.Container(Nav(page), width=500, height=50, gradient=ft.LinearGradient(colors=['#fbe5fe', '#FF9CF8'], rotation=180), border=ft.border.all(1, "000000"), border_radius=15),
                                                 ft.Column([
                                                     ft.Row([
                                                        
                                                         Analystics(
                                                            f"Currently Popular: ({Popular["Month"]})", Popular["Value"]),
                                                         Analystics(
                                                             f"Total Amount: ({Amount["Month"]})", Amount["Value"]),
                                                     ]),
                                                     ft.Row([
                                                         Analystics(
                                                             "Current Appointments", json.loads(stats.text)[2]),
                                                         Analystics(
                                                             "Total Appointments", json.loads(stats.text)[3]),

                                                         
                                                     ])
                                                 ], ),
                                                 Divider(
                                                     color=ft.colors.BLACK),
                                                 Gui(),
                                                 #Chart(curr, prev)
                                                 ]), padding=20)

        ],
        padding=0
    )


def CPanel(page):

    class Bookings(ft.UserControl):
        def __init__(self):
            super().__init__()
            self.content = ft.Column(horizontal_alignment=CrossAxisAlignment.CENTER, )
            self.res()

        def res(self):
                try:
                    bytes_Dict = get_('http://10.0.0.148:5000/Admin/req/Clients')
                    str_Cli = bytes_Dict.content.decode('utf-8')
                    dict_Cli = json.loads(str_Cli)
                    self.build_client(dict_Cli)
                except ValueError as ve:
                    print("Error:", ve)
                except Exception as e:
                    print("An error occurred:", e)

        def build_client(self, args):
                for x in args:
                    print("")
                    Day, Month, Year = Extract(x["D$T"]["Date"])
                    
                    client = Client(
                        x['details']['n'],
                        Day, Month, Year,
                        x['D$T']['Time'],
                        x["Coiffure"]['T'],
                        re.split(r"\s", x["Coiffure"]['l'])[0],
                        x["Coiffure"]['s'],
                        "Black",
                        x["Coiffure"]['e'],
                        x['details']['Tel'],
                        x['details']['e'],
                        x['_id'],

                    )
                    self.content.controls.append(client)
                
        def build(self):
             return self.content

    def Extract(date_string):
        date_object = datetime.strptime(date_string, "%d %B %Y")
        print(date_object)
        date_object = str(date_object.date())  # Extract only the date component
        form = str.replace(date_object, "-", " ")
        final = re.split(r"\s", form)
        Year = final[0]
        Month = calendar.month_name[int(final[1])][0:3]
        Day = final[2]

        return Day, Month, Year
    return View(
        route='/Web-Admin/@CPanel-HybridSalon',
        controls=[
            Container(**BG(), content=ft.Column([Branding("CPanel"),
                                                 ft.Container(Nav(page), width=500, height=50, gradient=ft.LinearGradient(colors=['#fbe5fe', '#FF9CF8'], rotation=180), border=ft.border.all(1, "000000"), border_radius=15),
                                                 Bookings(),
                                                 
                                                 ]),padding=20)
            



        ],
        padding=0

    )


def Console(page):
    req = reqList("http://10.0.0.148:5000/api/set")
    reqS = reqList("http://10.0.0.148:5000/api/show")

    
    return View(
        route='/Web-Admin/@Console-Panel',
        controls=[
            Container(**BG(), content=ft.Column([
                Text(**Title("Console"),font_family="Brusher"),ft.Divider(color=ft.colors.BLACK),
                ft.Container(Nav(page), width=500, height=50, gradient=ft.LinearGradient(colors=['#fbe5fe', '#FF9CF8'], rotation=180), border=ft.border.all(1, "000000"), border_radius=15)
                , ft.Divider(color=ft.colors.BLACK), 
                 ProcessTree(req, reqS)
                    

            ], scroll=ScrollMode.ALWAYS, on_scroll_interval=0)
            )



        ]
    
    )

