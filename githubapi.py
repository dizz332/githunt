"""
@ First modified by dizz-pfeffel
@ Repo ~ https://github.com/dizz-pfeffel/githunt
"""
import requests,re

class getemail:
    def getemail(user):
        req = requests.get(f"https://api.github.com/users/{user}/events/public")
        print(re.findall("email", req))
getemail.getemail(input(b"Username: "))
