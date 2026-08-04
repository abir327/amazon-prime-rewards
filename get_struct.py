with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

rules = c.find('OFFICIAL RULES')
if rules != -1:
    print(c[rules-1000:rules+50])
