# To solve this problem I want you to receive a string like this :
# rand_str = "https://www.youtube.com http://www.google.com"
# And, then Grab the URL and provide the following output using a back reference substitution :
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>

import re

rand_str = "https://www.youtube.com http://www.google.com"
regex = re.compile(r"(https?://([\w.]+))")

rand_str = re.sub(regex, r"<a href='\1'>\2</a>\n", rand_str)

print(rand_str)