with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.finditer(re.compile(r'Claim Now', re.IGNORECASE), c)
for m in matches:
    start = max(0, m.start() - 200)
    end = min(len(c), m.end() + 200)
    print(f"...{c[start:end]}...")
    print("-" * 20)
