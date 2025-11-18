import requests
from requests import Session

s = requests.Session()
s.auth = ("mathemagician", "43c3ec8")

r = s.post("https://usaco.org/index.php?page=viewproblem2&cpid=1524")
print(r.text)
