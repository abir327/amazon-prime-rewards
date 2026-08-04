with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.finditer(r'ueLogError', c)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(c), m.end() + 50)
    print(f"...{c[start:end]}...")
    print("-" * 20)
