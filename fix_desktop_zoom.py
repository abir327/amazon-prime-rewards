import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove any viewport meta tags that might have been added
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

# Remove any responsive style blocks we added
content = re.sub(r'<style>\s*/\* Scoped mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<style>\s*/\* Aggressive mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<style>\s*/\* Make the entire layout fluid.*?</style>', '', content, flags=re.DOTALL)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed responsive hacks and viewport to allow natural desktop zoom on mobile.")
