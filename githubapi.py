"""
@ First modified by dizz-pfeffel
@ Repo ~ https://github.com/dizz-pfeffel/githunt
"""
import requests,json

class getemail:
    def getemail(user):
        r = requests.get(f"https://api.github.com/users/{user}/events/public")
        githubjson = json.load(r)
        emails = githubjson("email")
        print(emails)
getemail.getemail("dizz-pfeffel")
