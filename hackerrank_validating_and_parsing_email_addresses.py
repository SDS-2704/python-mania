#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
import email.utils
import re
n = int(input())
for n_ in range(n):
   name_, eid_ = email.utils.parseaddr(input())
   if bool(re.match(r'^[a-zA-Z][a-zA-Z0-9\.\-\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', eid_)) == True:
      print(email.utils.formataddr((name_, eid_)))
   else:
    continue
