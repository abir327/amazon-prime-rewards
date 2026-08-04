with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\\n', '\n')

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Literals fixed.")
