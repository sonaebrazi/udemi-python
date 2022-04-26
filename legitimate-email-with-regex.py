'''
1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
2. An @ symbol
3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
4. A period
5. 2 to 3 lowercase and uppercase letters
'''
import re

email_list = "db@aol.com m@.com @apple.com db@.com"
print("Email Matches :" ,len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}",email_list)))