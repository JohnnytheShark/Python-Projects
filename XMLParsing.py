import pandas as pd
import numpy as np
import os
import openpyxl
import urllib.request
import xmltodict


class ATCXMLREADER():
    def __init__(self,filename):
        self.filename = filename

    def readExcelSheet(self,sheetname):
        if os.path.isfile(self.filename) == True:
            Data = pd.read_excel(self.filename,sheet_name=sheetname)
            return Data
        else:
            raise Exception("Unable to open file")
        
    def retreiveXMLData(self,link):
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            data = xmltodict.parse(the_page)
            return data
