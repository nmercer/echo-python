from bs4 import BeautifulSoup
import requests
import json

BASE_URL = 'https://pitangui.amazon.com'
TODO_URL = 'https://pitangui.amazon.com/api/todos?type=TASK&size=1'

class Echo(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13'})
        self.login()

    def get(self, url):
        print "GET"
        self.session.headers.update({'Referer':None})
        request = self.session.get(url)

        # Todo - Error Check this
        return request.text

    def post(self, url, data={}):
        print "POST"
        self.session.headers.update({'Referer':BASE_URL})
        request = self.session.post(url, data=data)

        # Todo - Error Check this
        return True

    def login(self):
        login_page = self.get(BASE_URL)

        soup = BeautifulSoup(login_page)
        form = soup.find_all('form')[0]
        action = form.get('action')
        inputs = form.findAll('input')

        data = {}
        for inp in inputs:
            if inp.get('name') and inp.get('value'):
                data[inp.get('name')] = inp.get('value')

        data['email'] = self.username
        data['password'] = self.password
        data['create'] = 0
        data['ue_back'] = 1

        self.post(action, data=data)

    def get_latest_todo(self):
        return json.loads(self.get(TODO_URL))['values'][0]['text']
