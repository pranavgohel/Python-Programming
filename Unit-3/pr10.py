import re

with open("./data.txt", "w") as file:
    file.write("Hello! You can reach us at support@python.org or admin@test.com.")

with open("./data.txt", "r") as file:
    content = file.read()

emails = re.findall(r"[\w.-]+@[\w.-]+", content)

print("Extracted Emails:", emails)