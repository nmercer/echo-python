from bs4 import BeautifulSoup
import requests
import json

BASE_URL = 'https://pitangui.amazon.com'
TODO_URL = 'https://pitangui.amazon.com/api/todos?type=TASK&size=1'

class Echo(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.last_todo_id = ''
        self.first_run = True
        self.login()

    def get(self, url):
        self.session.headers.update({'Referer':None})

        try:
            request = self.session.get(url)
            if request.status_code == 200:
                return request.text
        except:
            pass

        self.login()
        return False

    def post(self, url, data={}):
        self.session.headers.update({'Referer':BASE_URL})
        try:
            request = self.session.post(url, data=data)
            if request.status_code == 200:
                return True
            print request.status_code
            print type(request.status_code)
        except:
            pass

        self.login()
        return False

    def login(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13'})

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
        try:
            todo = json.loads(self.get(TODO_URL))['values'][0]['text']
            todo_id = json.loads(self.get(TODO_URL))['values'][0]['itemId']
        except:
            self.login()
            return None

        if not self.first_run:
            if self.last_todo_id != todo_id:
                self.last_todo_id = todo_id
                return todo
        else:
            self.last_todo_id = todo_id
            self.first_run = False

        return None
