with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.finditer(r'<style>.*?@media screen and \(max-width: 900px\).*?</style>', c, re.DOTALL)
for m in matches:
    print(m.group(0)[:500])
    print("... truncated ...")
    print("-" * 40)
