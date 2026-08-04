with open('public/amazon.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
styles = re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
for s in styles:
    if 'Safe mobile responsive overrides' in s:
        print(s)
