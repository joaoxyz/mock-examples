'''
- spec
- patch decorator
- patch object
'''

import requests

def get_time():
    r = requests.get("http://localhost/api/time")
    if r.status_code == 200:
        return r.json()
    return None

class A():
    def f(self, a, b, c):
        pass
