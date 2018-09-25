#!/usr/bin/python

import json
from   json2html import *

with open('32f9fc36-6963-9ee0-9b44-a89112919e29.json') as js:
  j = json.load(js)
  o = json2html.convert(json=j)
  f = open('32f9fc36-6963-9ee0-9b44-a89112919e29.html', 'w')
  f.write(o)
