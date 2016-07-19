# -*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()

class A:
    type='zpwust'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return  'im'+self.name+' '+str(self.age)
x=A('zpwust',1243)
print x

