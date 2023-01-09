"""
@ 10-01-2023 modified by mdoodm
Edit #1
+ removed offline environment testing on line 19

"""
import requests,json

def get_email(user):
    req = requests.get(f"https://api.github.com/users/{user}/events/public").text #
    req = json.loads(req)
    counter = -1 # may need to tinker with this
    for key in req: # most likely a better way to do this 
        counter += 1 # walk through
        try:
            print('Email: '+str(req[int(counter)]['payload']['commits'][0]['author']['email'])) # inefficient walk through
        except Exception as e: # need to address this at a later date
            print(end='') # clean up if it can't find any email attached to the repository
            
user = str(input('Github Username\n:')) # enforcing string
get_email(user)
