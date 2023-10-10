import sys
import time
from time import sleep 
from os import system 


try:
  import requests
except ImportError:
  system('pip install requests colorama')
  system('clear')
  print("Run it again!\n")
  sys.exit()



def SingleIP():
  try:
    system('clear')
    print("\n[+] Press Enter to Trae your self, or Enter your Target IP!"+"\n")
    print("[+] https://github.com/PengHackHandal\n\n")
    IP = input("[+] Enter your Target IP: ")
  except KeyboardInterrupt:
    print("\n[!] KeyboardInterrupt Exiting...\n")
    sleep(1)
    sys.exit()

  URL = "http://ip-api.com/json/{}?fields=status,massage,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,as,asname,mobile,proxy,query".format(IP)

  req = requests.get(URL).json()


  try:
    print("\n")
    print("[+] Target IP:", req['query'])
    print("[+] Status:", req['status'])
    print("[+] Country:", req['country'])
    print("[+] Country code:", req['countryCode'])
    print("[+] Region:", req['region'])
    print("[+] Regoin Name:", req['regionName'])
    print("[+] City:", req['city'])
    print("[+] ZIP ode:", req['zip'])
    print("\n")
    print("[+] Latitude:", req['lat'])
    print("[+] Longitude:", req['lon'])
    print("[+] Timezone:", req['timezone'])
    print("[+] ISP:", req['isp'])
    print("[+] AS:", req['as'])
    print("[+] ASname:", req['asname'])
    print("\n")
    print("[+] Mobile:", req['mobile'])
    print("[+] Proxy:", req['proxy'])
    print("\n")
    print("[+] Google Maps:"+" https://www google om/maps/place/"+str(req['lat'])+","+str(req['lon']))
  except KeyError:
    print("\n"+"  'INVALID IP ADDRESS'")
    sys.exit
SingleIP()
