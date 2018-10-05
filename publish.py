#!/usr/bin/python
import scan, json, sys
import mqtt as m
from time import sleep as sleep
from os import system, name
d = scan.detect()
data={}
history={""}
m.init()
print(d.setif("YOURinterfaceHERE!"))
print(d.interface)

def clear():
 if name == "nt":
  _ = system('cls')
 else:
  _ = system('clear')

try:
 while(1):
  print("Scanning...")
  if d.scan():
   clear()
   print("Number of denied AP's: " + str(d.deny))
   print("Number of allowed AP's: " + str(d.permit))
   print("Number of hidden AP's: " + str(d.hidden))
   print("Number of \"Media\" AP's: " + str(d.media))
   print("Names of denied AP's: " + str(d.wlan_list))
   print
   for each in d.wlans:
#    for known in history:
    if each not in history:
     history.add(each)
   print("Scan history")
#   for known in history:
   print history
#  print(d.wlans)
   data["networks"] = d.wlan_list
   data["media"] = d.media
   data["hidden"] = str(d.hidden)
   data["deny"] = str(d.deny)
   data["allow"] = str(d.permit)
# approximately 12 students in an affected area
   data["students"] = "~" + str(int(d.deny) * 12)
   m.send(str=None,retain=True)
#  sleep(0.5)
   m.send(str=json.dumps(data),retain=True)
#  print(json.dumps(data))
  sleep(5)
except Exception as e:
 print e
 m.close
 sys.exit()

