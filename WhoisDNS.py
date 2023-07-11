import whois
import sys
import pyfiglet
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("WHOIS Lookup")
print(ascii_banner)

target = input(str( "TargetDomain: " ))

#Banner
print("_" * 50)
print("Scanning: " + target )
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

res = whois.whois(target)
print(res)