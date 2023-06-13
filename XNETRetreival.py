# %%
import tkinter as tk
from tkinter import ttk
import requests
import certifi
from html.parser import HTMLParser
import re
import pandas as pd
import numpy as np

class MyHTMLParser(HTMLParser):
    keys=[]
    versions = []
    def __init__(self):
        super().__init__()

    def handle_data(self,data):
        if "ses=" in data:
            searchingString = re.search(r'ses=[A-Za-z\d&]+ISN=[\dA-Za-z&]+TRN=[\dA-Za-z]+',data).group()
            MyHTMLParser.keys.append(searchingString)
        elif "&v=" in data:
            searchingString = re.search(r'&v=\d+',data).group()
            MyHTMLParser.versions.append(searchingString)



class App(tk.Frame):
    message = ''
    '''Application Class that runs the application for corporate'''
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()

    def close_win(self):
        '''Function to close the application'''
        self.destroy()
        exit()

    def collectdata(self):
        '''Collect the XNET Data from XNET'''
        try:
            '''Establish a connection and get the session id to be able to make the requests'''
            with requests.Session() as session:
                r = session.get(url,auth=(username.get(),password.get()),verify=certifi.where())
                if r.status_code == 200:
                    parser = MyHTMLParser()
                    parser.feed(r.text)
                    '''Get the versions of the report that we need to download to create this report'''
                    versions = session.get(url,auth=(username.get(),password.get()),params=pa)
                    parser.feed(versions.text)
                    for i in parser.versions[0:3]:
                        version = i.replace("&v=","")
                        downloadReport = session.get(url,auth=(username.get(),password.get()),params=par,allow_redirects=True)
                        if downloadReport.status_code == 200:
                            open(f'./{version}.csv',"w").write(downloadReport.text)
                        else:
                            raise Exception(f"Unable to download version {version} of Report. Something has gone wrong. You will have to download the file manually to continue.")
                        
                else:
                    raise Exception("Unauthorized. Did you use the correct credentials?")

            App.message = "Completed Collecting Data"
            results.config(text=App.message)
        except Exception as e:
            print(f'An exception occurred: {str(e)}')
            App.message = str(e)
            results.config(text=App.message)

    def cleandata(self):
        try:
            print("Cleaning")
        except:
            print("Failed to Clean")


#Create the Visual Portion:
myapp = App()
myapp.master.title("Automation Application")
myapp.master.maxsize(1000,400)
label1 = tk.Label(myapp,text="Username").pack()
global username
username = tk.Entry(myapp)
username.pack()
label2 = tk.Label(myapp,text="Password").pack()
global password
password = tk.Entry(myapp,show="*")
password.pack()
StartButton = tk.Button(myapp,text="Collect Data from XNET",command=myapp.collectdata)
StartButton.pack()
global results
results = tk.Label(myapp,text=myapp.message)
results.pack(pady=5)
CleanDataButton = tk.Button(myapp,text="Cleanse the Data Collected",command=myapp.cleandata).pack(pady=20)
QuitButton = tk.Button(myapp,text="Quit Application",command=myapp.close_win).pack(pady=20)
myapp.mainloop()
