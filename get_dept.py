with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.find('Department')
while idx != -1:
    if 'h1' in content[idx-50:idx+50]:
        print(content[idx-400:idx+300])
        break
    idx = content.find('Department', idx + 1)
