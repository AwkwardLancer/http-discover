import requests
import sys

host = sys.argv[1]
methods = ['OPTIONS','GET','POST','PUT','DELETE','TRACE','CONNECT','HEAD','PATCH']

print ("-" * 80)
print ("| HTTP Methods discover, by Awkward_Lancer (https://github.com/AwkwardLancer) |")
print ("-" * 80)

try:
	for method in methods:
		answer = requests.request(method, host)
		print (method + " -> " + answer.reason)
except:
	print ("Error: website closed the connection")
