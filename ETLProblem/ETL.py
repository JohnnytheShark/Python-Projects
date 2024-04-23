'''
Linkedin Learning Course Problem: 

Load Data From Traffic.csv File attached into a "traffic" table in SQLLite3 Database

Parameters: 
    - IP Address should be a Valid IP
    - Times recorded in the time column should not be in the future
    - Path can't Be Empty
    - Status Code must be a valid HTTP Status Code
    - Size Can't be Negative or Empty

    Report the Percentage of Bad Rows. Fail the ETL if there are more than 5% bad rows

    CSV Data Structure: 
    ip,time,path,status,size
'''

import pandas as pd
import sqlite3
from http import HTTPStatus
from ipaddress import ip_address
from contextlib import closing

status_codes = set(HTTPStatus)

class ETLProcess():
    '''ETL (Extract Transform Load) Class Function used to handle data from CSV Files'''
    def __init__(self,filename,db,badPercentage,tableName):
        self.filename = filename
        self.db = db
        self.badPercentage = badPercentage
        self.tableName = tableName
        # List of Validation Functions
        self.validations = [
            self.ipAddressCheck,
            self.timeCheck,
            self.emptyPathisNotEmpty,
            self.statusCodeValidity,
            self.sizeNotEmptyorNegative
        ]

    def ipAddressCheck(self,row):
        '''First check to see if the row has a valid IP Address'''
        try: 
            ip_address(row['ip'])
            return True
        except ValueError: 
            return False
    
    def timeCheck(self,row):
        '''We Check to see if the time is not in the future'''
        now = pd.Timestamp.now()
        rowTime = pd.to_datetime(row['time'],errors="coerce")
        if rowTime > now:
            return False
        return True
    
    def emptyPathisNotEmpty(self,row):
        '''Path Column Can't Be Empty'''
        if pd.isnull(row['path']) or not row['path'].strip():
            return False
        return True
    
    def statusCodeValidity(self,row):
        '''Status Codes have to be a valid HTTP Status Code'''
        if row['status'] not in status_codes:
            return False
        return True
    
    def sizeNotEmptyorNegative(self,row):
        '''Size Can't be Negative or Empty'''
        if pd.isnull(row['size']) or row['size'] < 0:
            return False
        return True

    def validityCheck(self,row):
        '''This function runs through validity checks to insure that our data can be inserted into the database'''
        for validation in self.validations:
            if not validation(row):
                return False
        return True
        
    def ETL(self):
        'Extract Transform Load Main Function'
        df = pd.read_csv(self.filename,parse_dates=['time'])
        # Bad Row(s) processing based on allowed percentage
        badRows = df[~df.apply(self.validityCheck,axis=1)]
        if len(badRows) > 0:
            percent_bad = len(badRows)/len(df) * 100
            print(f'{len(badRows)} ({percent_bad: .2f}%) bad rows')
            if percent_bad >= self.badPercentage:
                raise ValueError(f'too many bad rows ({percent_bad:.2f}%)')
        
        # Only retrieve the rows that were cleaned correctly. 
        df = df[~df.index.isin(badRows.index)]
        with closing(sqlite3.connect(self.db)) as conn:
            conn.execute('BEGIN')
            with conn:
                df.to_sql(self.tableName,conn,if_exists="append",index=False)

if __name__ == '__main__':
    ETLProcessor = ETLProcess('ETLProblem/traffic.csv','ETLProblem/traffic.db',5,'traffic')
    ETLProcessor.ETL()
