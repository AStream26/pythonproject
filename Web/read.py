# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

serviceurl = "http://py4e-data.dr-chuck.net/json?"
conn =  sqlite3.connect("geodata1.sqlite")
cur = conn.cursor()
#cur.execute(''' drop table LOCATION''' )
cur.execute('''
            CREATE TABLE IF NOT EXISTS LOCATION (address TEXT , geodata TEXT)''')

file = open('where.data')
count =0
for data in file:
    if count>20:
        print("20 records reterived")
        print("restart to add more record .......")
        break
    
    address= data.strip()
    cur.execute(''' select geodata from LOCATION where address = ?''',(memoryview(address.encode()),  ))    
    
    try:
        data = cur.fetchone()[0]
        print("data already exists!!")
        continue
    except:
        pass
    
        
        
    
    params = dict()
    params["address"] = address
    params["key"] = 42
         
    url = serviceurl + urllib.parse.urlencode(params)
    geodata = urllib.request.urlopen(url)
    data1 = geodata.read().decode()
    print("reteriving url .....")
    print('Retrieved', len(data1), 'characters', data[:20].replace('\n', ' '))
    
    cur.execute('''INSERT INTO LOCATION (address,geodata) VALUES 
                ( ?, ? )''',(memoryview(address.encode()),memoryview(data1.encode())
               ))
    conn.commit()
    count = count +1
    if(count%10==0):
        print("pausing for a while")
        time.sleep(5)
    
    
    
