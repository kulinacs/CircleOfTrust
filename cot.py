from bs4 import BeautifulSoup
import json
import requests

class CircleOfTrust():

    def __init__(self, username, password):
        '''Create an authenticated request session for the user'''
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
        }
        self.session = requests.Session()
        # Set the User Agent so Reddit won't block us
        self.session.headers.update(user_agent)
        # Hit the landing page to start our session
        self.session.get('https://reddit.com/')
        # Confirm we do not need a captcha
        login_payload = {'op': 'login',
                         'user': username,
                         'passwd': password,
                         'rem': 'yes',
                         'api_type': 'json'
        }
        self.session.get('https://reddit.com/api/requires_captcha/login.json').json()
        # Get our session cookies and set modhash
        modhash = self.session.post('https://www.reddit.com/api/login/kulinacs', data=login_payload).json()['json']['data']['modhash']
        x_modhash = {
            'x-modhash': modhash
        }
        self.session.headers.update(x_modhash)

    def get_password(self, username):
        '''Get the password for the given username'''
        html = self.session.get('https://reddit.com/user/{}/circle/embed'.format(username)).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find(id="circle-passphrase")['value']

    def unlock(self, username, key):
        '''Unlock a Circle Of Trust'''
        html = self.session.get('https://reddit.com/user/{}/circle/embed'.format(username)).text
        soup = BeautifulSoup(html, 'html.parser')
        vote_id = soup.find(class_="link_fullname")['value']
        data = {'id': vote_id, 'vote_key': key}
        return self.session.post('https://www.reddit.com/api/guess_voting_key.json', data=data)

    def join(self, username):
        '''Join an unlocked Circle Of Trust'''
        html = self.session.get('https://reddit.com/user/{}/circle/embed'.format(username)).text
        soup = BeautifulSoup(html, 'html.parser')
        vote_id = soup.find(class_="link_fullname")['value']
        vote_hash = json.loads(soup.find(id="config").text[8:-1])['vote_hash']
        data = {'id': vote_id, 'dir': 1, 'vh': vote_hash, 'isTrusted': False}
        return self.session.post('https://www.reddit.com//api/circle_vote.json?dir={}&id={}'.format(1, vote_id), data=data)        

    def betray(self, username):
        '''Betray an unlocked Circle Of Trust'''
        html = self.session.get('https://reddit.com/user/{}/circle/embed'.format(username)).text
        soup = BeautifulSoup(html, 'html.parser')
        vote_id = soup.find(class_="link_fullname")['value']
        vote_hash = json.loads(soup.find(id="config").text[8:-1])['vote_hash']
        data = {'id': vote_id, 'dir': -1, 'vh': vote_hash, 'isTrusted': False}
        return self.session.post('https://www.reddit.com//api/circle_vote.json?dir={}&id={}'.format(-1, vote_id), data=data)        
