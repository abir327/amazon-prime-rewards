with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.finditer(r'<div[^>]*class="[^"]*apb-browse-two-col-center-margin-right[^"]*"[^>]*>', c)
for m in matches:
    print(m.group(0))

matches = re.finditer(r'<div[^>]*class="[^"]*a-column[^"]*"[^>]*>', c)
for m in matches:
    print(m.group(0))

