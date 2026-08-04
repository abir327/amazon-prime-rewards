with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()
    head_end = content.find('</head>')
    print(content[:head_end+7])
