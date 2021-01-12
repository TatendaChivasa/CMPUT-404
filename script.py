import requests

#getting the requests version
print(requests.__version__)

#getting the google homepage
response = requests.get("http://google.com/")
print(response.status_code)
