#!/usr/bin/python
""" A library to detect "counter-revolutionary"
    WLAN SSIDs inside of Innovator's Hall
"""

import subprocess
from subprocess import PIPE,STDOUT
from time import sleep as sleep


class detect:
 ap_name1="Capitol Residence Hall" 
 ap_name2="Capitol" 
 media_ap = {"DIRECT","PS4"}
# class initialization
 def __init__(self):
  self.interface=None
  self.permit = 0
  self.deny = 0
  self.hidden = 0
  self.wlans={}
  self.media=0
  self.wlan_list=""
# set all values to default to acquire new data
 def reset_stats(self):
  self.permit = 0
  self.deny = 0
  self.hidden = 0
  self.wlans={}
  self.media=0
  self.wlan_list=""

 def scan(self, name=None, debug=False):
# run shell command to obtain AP's
# use default if not "testing" 
  if debug:
   os = subprocess.Popen("sudo iwlist " + str(name) + " scan | grep ESSID", shell=True, stdout=PIPE)
  else:
   os = subprocess.Popen("sudo iwlist " + str(self.interface) + " scan | grep ESSID", shell=True, stdout=PIPE)
# retrieve output
  w=os.communicate()[0]

# interface may need more time to scan or cannot scan
  if w.find("scanning") != -1: #$iface_name	Interface doesn't support scanning
#   print(w)
   return False

# interface is ready to scan; further parse
  elif w.find("Device or resource busy") == -1:
# reset stats to relfect new data
   self.reset_stats()
# parse data and remove extra characters
   k=' '.join(w.split()).replace("ESSID:", "")
   p = k.split("\" \"")
   for each in p:
    each = each.replace("\"", "")
# check if each name is allowed, increase allow count
    if each in (self.ap_name1, self.ap_name2):	# Python tricks at work here
     self.permit += 1
# else increase deny count
    else:
     self.deny += 1
# check if AP is hidden; distinguished by "", 
# increase hidden count
     if each == "":
      self.hidden += 1
# add (append) names to list, excluding hidden AP's
     else:
      self.wlan_list += each + ", "
# check if each AP name starts with characters that
# may represent those of a media device ex: "DIRECT"
# and increase media device count
      for m in self.media_ap:
       if each.startswith(m):
        self.media += 1
# append all (but not hidden) wlan names to WLAN dict
    self.wlans[each] = each
# debug
#   print ("Number of allowed AP's: " + str(self.permit))
#   print ("Number of counter-revolutionary AP's: " + str(self.deny))
   return True
# there may be a problem if we reach this point
  else:
   return False


# Check if interface is a WLAN interface
# TODO: find a better way of detecting WLAN interfaces
 def setif(self, name):
  self.interface=name
  if not self.scan(self.interface, debug=True):
   print(self.interface + " - this interface may not work...")
#   print("Interface cannot scan for networks")
   return False
  else:
   return True

