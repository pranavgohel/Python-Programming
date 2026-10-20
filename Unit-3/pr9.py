import re

text = "Contact: support@python.org, Code: 404, Status: Active"

m = re.match("Contact", text)
print("1. match:", m.group())

s = re.search("Code", text)
print("2. Search:", s.group())

f = re.findall("Active", text)
print("3. Findall:", f)