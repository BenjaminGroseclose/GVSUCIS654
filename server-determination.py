import os

hostname = "96.7.137.208"
response = os.system("ping /n 5 " + hostname)

print("United States East")
print(response)

hostname = "United States West"
response = os.system("ping /n 5 " + hostname)

print("United Kingdom")
print(response)


hostname = "77.74.193.94"
response = os.system("ping /n 5 " + hostname)

print("United Kingdom")
print(response)


hostname = "45.235.47.246"
response = os.system("ping /n 5 " + hostname)

print("Brazil")
print(response)


hostname = "185.238.200.7"
response = os.system("ping /n 5 " + hostname)

print("Russia")
print(response)


hostname = "92.173.162.22 "
response = os.system("ping /n 5 " + hostname)

print("France")
print(response)

