import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the viewport meta tag to remove initial-scale=1.0
content = re.sub(r'<meta name="viewport" content="width=1000, initial-scale=1.0">', '<meta name="viewport" content="width=1000">', content)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed viewport 5 applied.")
