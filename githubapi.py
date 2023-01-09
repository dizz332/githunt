import requests,json

class getemail:
    def getemail(user):
        req = requests.get(f"https://api.github.com/users/{user}/events/public").text
        req = json.loads(req)
        counter = -1
        for key in req:
            counter += 1 # walk through
            try:
                print('Email: '+str(req[int(counter)]['payload']['commits'][0]['author']['email'])) # aids walk through
            except Exception as e:
                print(end='') # clean up if it can't find any email attached to the repository
getemail.getemail(input("Username: "))
