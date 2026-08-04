with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
match = re.search(r'(<div[^>]*>)\s*<div[^>]*>\s*<img[^>]*"OPT-in_Sweepstakes_LP[^>]*>', c)
if match:
    print(match.group(1))

# Find the rules text container
rules = c.find('OFFICIAL RULES')
if rules != -1:
    print(c[rules-200:rules+50])
