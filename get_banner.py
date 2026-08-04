import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(.{0,3000})<div class="neon-btn-container">', content, re.DOTALL)
if match:
    # Just print all tags
    tags = re.findall(r'<[^>]+>', match.group(1)[-1500:])
    print('\n'.join(tags))
