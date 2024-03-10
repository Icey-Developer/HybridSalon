import flet
from flet import *
from Controls import *
from Properties import *
from Pages import *
import time
import requests
import json




def Main_(page : Page):
   page.window_width = 1440/3 - 5
   page.title = "Admin(Blue)"
   page.fonts = {
           "Brusher" : "fonts/Brusher.ttf",
           "Pacifico" : "fonts/Pacifico-Regular.ttf",
        }
   page.views.append(Loading(page=page))
   page.update()

   page.views.clear()
   page.views.append(Dashboard(page))

   page.update()
    
   def Route_Change(route):

        if page.route == "/Web-Admin/@CPanel-HybridSalon":
           page.views.clear()
           page.views.append(CPanel(page))
           page.update()
        if page.route == "/Web-Admin/@Dashboard":
           page.views.clear()
           page.views.append(Dashboard(page))
           page.update()
        if page.route == "/Web-Admin/@Console-Panel":
           page.views.clear()
           page.views.append(Console(page))
           page.update()
         

   page.on_route_change = Route_Change
   page.update()
    

app(Main_, assets_dir="assets")