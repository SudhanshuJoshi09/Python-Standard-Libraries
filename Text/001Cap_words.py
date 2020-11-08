#!/usr/bin/env python3

import string

sent = 'this is some content!'
print('*'*50 + ' Before ' + '*'*50)
print(sent)
print('*'*50 + ' After ' + '*'*50)
print(string.capwords(sent))