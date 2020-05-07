# -*- coding: utf-8 -*-
import sqlite3 as sql
import json
import codecs

con = sql.connect("geodata1.sqlite")
cur = con.cursor()
cur.execute("select * from LOCATION ")

file= codecs.open("dump.js",'w',"utf-8")
file.write("myData = [\n")
count = 0

for row in cur:
    data = str(row[1].decode())
    
    try:js = json.loads(str(data))
    except:
        print("rara")
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"] 
    lng = js["results"][0]["geometry"]["location"]["lng"] 
    print('lat', lat, 'lng', lng) 
    location = js['results'][0]['formatted_address'] 
    location = location.replace("'","")
    print(location) 
    
    try:
        if(count==0):
            com = "["
        else:
            com = ",\n["
        count = count+1
            
            
        
        
        out = com+str(lat)+","+str(lng)+", '"+location+"']"
        file.write(out)
       
    except:
        print("error")
        continue
    
file.write("\n];\n")
file.close()
con.close()
        


