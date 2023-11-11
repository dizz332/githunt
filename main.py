import requests,json

# old
"""
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
"""

# new
def getEmail(user):
    headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer <YOUR-TOKEN>",
    "X-GitHub-Api-Version": "2022-11-28"
    }

    data = {
    "blog": "https://github.com/blog",
    "name": "monalisa octocat"
    }

    r = requests.patch(
    "https://api.github.com/user", 
    headers=headers,
    json=data
    )
    return r.text
    
if __name__ == "__main__":
    user = str(input('Github Username\n:')) # enforcing string
    print(getEmail(user))
    
# this is insanely unfinished