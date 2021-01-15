import requests

#getting the requests version
print(requests.__version__)

#getting the google homepage
response = requests.get("http://google.com/")
print(response.status_code)

#getting script from github
script_file = requests.get("https://raw.githubusercontent.com/TatendaChivasa/CMPUT-404/main/cmput404_lab1/script.py")
print(script_file.text)