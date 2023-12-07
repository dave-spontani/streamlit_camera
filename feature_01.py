###############Query Builder for the FDA Api
import requests
##Base query: https://api.fda.gov/drug/event.json

res = requests.get("https://api.fda.gov/drug/event.json?search=receivedate:[20040101+TO+20231207]&count=patient.drug.openfda.pharm_class_epc.exact")

print(res)

print("Hello")
