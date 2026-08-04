with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
styles = re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
for s in styles:
    if 'max-width: 768px' in s or 'max-width: 900px' in s or 'RESPONSIVE' in s or 'mobile' in s.lower():
        print("FOUND RESPONSIVE STYLE BLOCK")
        print(s[:300])
        print("...[truncated]...")
        print(s[-300:])
        print("="*40)
