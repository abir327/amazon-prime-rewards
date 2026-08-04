import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if viewport meta exists
if 'name="viewport"' not in content:
    content = content.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">', 1)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added viewport meta tag.")
else:
    # Maybe update existing viewport
    content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">', content)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated viewport meta tag.")

