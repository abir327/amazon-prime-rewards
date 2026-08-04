import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old responsive CSS
content = re.sub(r'<style>\s*/\* Safe mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)

# Add a fixed width viewport for PC layout on mobile
viewport_meta = '<meta name="viewport" content="width=1100">'

if '<meta name="viewport"' in content:
    content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', viewport_meta, content)
else:
    content = content.replace('</head>', viewport_meta + '\n</head>', 1)

# Also add a style to hide overflow on body to prevent white space if something extends beyond 1100px
fix_css = """
<style>
/* Fix horizontal scroll white space while keeping PC layout */
html, body {
    overflow-x: hidden !important;
    max-width: 1100px !important;
    margin: 0 auto !important;
}
#a-page {
    overflow-x: hidden !important;
}
/* Hide 1x1 tracking pixels that sometimes break layout */
img[width="1"][height="1"], img[width="0"][height="0"] {
    display: none !important;
}
</style>
"""
content = content.replace('</head>', fix_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed viewport applied.")
