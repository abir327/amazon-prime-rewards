import re
with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()
match = re.search(r'(<style>.*?neon-btn.*?</style>)', content, re.DOTALL)
if match:
    print(match.group(1))
