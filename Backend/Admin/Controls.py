from typing import Any, List, Optional, Union
import flet
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue
from Properties import *
import re
import smtplib
import json
import requests


def reqAcp(Data : dict):
    print(type(Data))
    result = json.dumps(Data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.148:5000/Accept/req/Client',data=result, headers=headers)
    if response.status_code!= 200:
        raise ValueError(response.text)
    return
def resDec(Data : dict):
    print(type(Data))
    result = json.dumps(Data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.148:5000/Decline/req/Client',data=result, headers=headers)
    if response.status_code!= 200:
        raise ValueError(response.text)
    return
def reqList(url : str = ""):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code!= 200:
        raise ValueError(response.text)
    return json.loads(response.text)
def resList(url : str = "", data : dict = {}):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code!= 200:
        raise ValueError(response.text)

def PostData(url : str = "", data : dict = {}):
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code!= 200:
        raise ValueError(response.text)
    return json.loads(response.text)


class WebTitle(flet.UserControl):
    def __init__(self, y):
        super().__init__()
        self.value = y

    def build(self):
        self.Title = ft.Text(**Title(self.value), font_family="Brusher")
        return self.Title

class Branding(flet.UserControl):
    def __init__(self, x):
        super().__init__()
        self.title = x

    def build(self):
        self.Webname = ft.Text(**WebName(), font_family="Aerial")
        return ft.Column([self.Webname, WebTitle(y=self.title), ft.Divider(color=ft.colors.BLACK)], width=2450, run_spacing=-5, spacing=-5)   

class Analystics(flet.UserControl):
    def __init__(self, type, Amount):
        super().__init__()
        self.T = type
        self.A = str(Amount)
        
    def build(self):
        
        self.Amount = ft.Text(**Amount(self.A, 25))
        self.Type = ft.Text(**Amount(self.T, 13))
        self.Anayls = ft.Container(**C_Box(), content=ft.Column([ self.Type, self.Amount]))
        return self.Anayls
    
class Client(flet.UserControl):
    def __init__(self, Name, Day, Month, Year, Time, Style, Size, Length, Color, Extras, Number, Email, id):
        super().__init__()
        self.id = id ;self.Size= Size; self.Length= Length ;self.Name = Name; self.Day = Day; self.Month = Month;  self.Year = Year; self.Time = Time; self.Style = Style; self.Color = Color; self.Extra = Extras; self.Number = Number; self.Email = Email
    def build(self):
        self._Box = ft.Container(**Box_())
        
        self._Box.content = ft.Column([
            ft.Row([                
                ft.Column([
                    ft.Text(**h4(f"{self.Name} || {self.Number}")),
                    ft.Divider(color=ft.colors.WHITE),
                    ft.Text(**h5(f"{self.Style} - {self.Size}")),
                    ft.Text(**h5(f"{self.Length}")),
                    ft.Text(**h5(f"Extra's : {self.Extra}")),
                    ft.Text(**h5(f"Color : {self.Color}")),
                    ft.Row(controls=[
                        ft.FilledButton(**Acpt_button(), on_click=lambda _: reqAcp({"n" : self.Name, "e" : self.Email, "t" : self.Time, "d" : self.Day, "i" : self.id})),
                        ft.FilledButton(**Decl_button(),on_click=lambda _: resDec({"n" : self.Name, "e" : self.Email, "t" : self.Time, "d" : self.Day, "i" : self.id}))
                    ],offset=ft.Offset(0, 0.2)),
                    
                ], spacing=0, run_spacing=0, offset=ft.Offset(0.03, 0), width=350),
                ft.Column([
                    ft.Text(**h1(f"{self.Day}")),
                    ft.Text(**h1(f"{self.Month}")),
                    ft.Text(**h5(f"{self.Year}")),
                    ft.Divider(color=ft.colors.WHITE),
                    ft.Text(**h1(f"{self.Time}")),
                    ], width=54, run_spacing=0, spacing=0, horizontal_alignment=ft.MainAxisAlignment.CENTER)
                    
                ], run_spacing=0, spacing=0)

        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        return self._Box

class Nav(flet.UserControl):
    def __init__(self, page):
        super().__init__()
        self.Pg = page
    
    def build(self):
        self.Con = flet.TextButton(**MainButton("Console"), on_click=lambda e: self.page.go('/Web-Admin/@Console-Panel'))
        self.CP = flet.TextButton(**MainButton("CPanel"), on_click=lambda e: self.page.go('/Web-Admin/@CPanel-HybridSalon'))
        self.Dash = flet.TextButton(**MainButton("Dashboard"), on_click=lambda e: self.page.go("/Web-Admin/@Dashboard"))
        
        return ft.Row([self.Con, self.CP, self.Dash], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.END, offset=ft.Offset(0, 0.2))
    
class Chart(flet.UserControl):
    def __init__(self, curr, prev):
        self.Val = round(((curr-prev)/prev) * 100)
        self.Amount = 100+self.Val
        pass

    def build(self):
        normal_radius = 50
        hover_radius = 60
        normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        hover_title_style = ft.TextStyle(
            size=22,

            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )

        def on_chart_event(e: ft.PieChartEvent):
            for idx, section in enumerate(chart.sections):
                if idx == e.section_index:
                    section.radius = hover_radius
                    section.title_style = hover_title_style
                else:
                    section.radius = normal_radius
                    section.title_style = normal_title_style
            chart.update()

        chart = ft.PieChart(
            sections=[
                ft.PieChartSection(
                    self.Val,
                    title=f"Loss: {self.Val}%",
                    title_style=normal_title_style,
                    color=ft.colors.GREEN,
                    radius=normal_radius,
                ),
                ft.PieChartSection(
                    self.Amount,
                    title=f"Amount: {self.Amount}%",
                    title_style=normal_title_style,
                    color=ft.colors.GREEN,
                    radius=normal_radius,
                ),
            ],
            sections_space=0,
            center_space_radius=40,
            on_chart_event=on_chart_event,
            expand=True,
        )
        return chart
    pass

from flet import Text, CupertinoTextField, Divider, Column, CrossAxisAlignment, UserControl

class ProcessTree(UserControl):
    def __init__(self, file, showcase):
        super().__init__()
        self.file = file
        self.showcase = showcase
        self.Section()

    def Section(self):
        controls = []  # Initialize a list to store controls
      
        for x in self.file:
            j = x['name']
            if x['name'] == "Knotless Braids(1-million)":
                j = "Knotless Braids"

            t = Text(**Main(j))
            button = ft.FilledButton(**Proceed(), on_click=self.On_Pub, text='Proceed')
            controls.append(button)
            controls.append(t)  # Add Main control to the list
            for Sub_ in x:
                if Sub_ != 'name':
                    Sub = Text(**SubText(Sub_), key=Sub_)
                    controls.append(Sub)  # Add Sub control to the list

                    controls.append(Text(**SubInfo("Lengths:")))
                    for length in x[Sub_][1]:
                        Len_ = ft.CupertinoTextField(value=length,helper_text=length, **PriceField(), on_submit=self.On_Submit)
                        controls.append(Len_)  # Add Len_ control to the list
                        

                    controls.append(Text(**SubInfo("Extra:")))
                    for Xtra in x[Sub_][2]:  # Corrected index from [1] to [2]
                        ext = ft.CupertinoTextField(value=Xtra,helper_text=Xtra, **PriceField(), on_submit=self.On_Submit)
                        controls.append(ext)  # Add Xtra_ control to the list
                    
                    controls.append(Text(**SubInfo("Xpr:")))
                    if x['name'] == "Knotless Braids(1-million)":
                        for c in self.showcase:
                            a = self.showcase[c]
                            for s in a:
                                b = a[s]
                                for Xpression in b:
                                    print(b[0])
                                    if Sub.key == b[0]:
                                        for Xpr in b[2]:
                                            Xpr_ = ft.CupertinoTextField(value=Xpr, helper_text=Xpr, **PriceField(), on_submit=self.On_Submit)
                                            controls.append(Xpr_)  # Add Len_ control to the list
                                        break  # Stop processing further values for this instance



                                        
                                    
                        pass
                    controls.append(Divider(color=ft.colors.BLACK))
        self.controls = controls  # Store the list of controls for later use
        return

    def On_Submit(self, e):
        a = e.control.value
        b = e.control.helper_text

        for x in self.file:
            dict_index = self.file.index(x)

            for i in x:
                if i == "name":
                    continue
                else:
                    for key in x[i][1]:
                        if key == b:
                            file = self.file[dict_index][i][1]
                            try:
                                index = file.index(b)
                                file[index] = a
                                b = a
                                e.control.update()
                            except ValueError:
                                pass  # If b is not found in the list, continue to the next iteration

                    for value in x[i][2]:
                        if value == b:
                            file2 = self.file[dict_index][i][2]
                            try:
                                index2 = file2.index(b)
                                file2[index2] = a
                                b = a
                                e.control.update()
                            except ValueError:
                                pass  # If b is not found in the list, continue to the next iteration
                            
                    if x['name'] == "Knotless Braids(1-million)":
                        for c in self.showcase:
                            n = self.showcase[c]
                            for s in n:
                                j = n[s]

                                # Finding the index of 'b' in the list self.showcase[c][s][2]
                                try:
                                    idex = self.showcase[c][s][2].index(b)
                                    self.showcase[c][s][2][idex] = a
                                    b = a
                                    print("done")
                                    e.control.update()
                                except ValueError:
                                    pass  # If b is not found in the list, continue to the next iteration

                                # Finding the index of 'b' in the list self.showcase[c][s][1]
                                try:
                                    idex1 = self.showcase[c][s][1].index(b)
                                    self.showcase[c][s][1][idex1] = a
                                    b = a
                                    print("done")
                                    e.control.update()
                                except ValueError:
                                    pass  # If b is not found in the list, continue to the next iteration
        return


    
    def On_Pub(self, e):
        return resList("http://10.0.0.148:5000/api/set", {"Set" : self.file, "Showcase" : self.showcase})
    def build(self):
        Prices = ft.Column(controls=self.controls, horizontal_alignment=CrossAxisAlignment.CENTER)
        return Prices


class Gui(UserControl):
    def __init__(self):
        super().__init__()
    
    def Pub(self, e):
        print({self.Announce.value, self.Set1.value, self.Set2.value})
        return PostData("http://10.0.0.148:5000/Announcement", {"1": self.Set1.value, "2" : self.Set2.value, "Msg" : self.Announce.value,})
    def build(self):
        Col = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, run_spacing=10, spacing=10)
        self.Announce = CupertinoTextField("Enter Announcement")
        self.Set1 = CupertinoTextField("Enter Time")
        self.Set2 = CupertinoTextField("Enter Time")
        self.submit = ft.FilledButton(**Proceed(), text="Submit", on_click=self.Pub)

        Col.controls.append(self.Announce)
        Col.controls.append(self.Set1)
        Col.controls.append(self.Set2)
        Col.controls.append(self.submit)
        

        return Col