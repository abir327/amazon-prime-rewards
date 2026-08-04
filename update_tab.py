import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
old_title = "<title>Amazon.com: : All Departments</title>"
new_title = "<title>Amazon.com: $1,000 Sweepstakes</title>"
content = content.replace(old_title, new_title)

# Add favicon if not present
if "favicon.ico" not in content:
    content = content.replace("</title>", "</title>\n<link rel=\"shortcut icon\" href=\"https://www.amazon.com/favicon.ico\">")

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Tab updated!")
