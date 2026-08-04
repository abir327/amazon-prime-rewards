import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old fixes
content = re.sub(r'<style>\s*/\* Fix horizontal scroll white space.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

# Use a viewport of 1000px which is typical for Amazon's min-width on desktop
viewport_meta = '<meta name="viewport" content="width=1000, maximum-scale=1.0">'
content = content.replace('</head>', viewport_meta + '\n</head>', 1)

fix_css = """
<style>
/* Fix horizontal scroll white space for mobile while keeping PC layout intact */
html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    min-width: 1000px !important;
}

#a-page, #navbar, .a-container {
    overflow-x: hidden !important;
    max-width: 100% !important;
}

/* Hide 1x1 tracking pixels that sometimes break layout */
img[width="1"][height="1"], img[width="0"][height="0"], img[width="1"] {
    display: none !important;
}
</style>
"""
content = content.replace('</head>', fix_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed viewport 3 applied.")
