import requests as req
x = req.get("https://www.google.com")
print(x.status_code)