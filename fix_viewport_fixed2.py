import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the previously added fix_css
content = re.sub(r'<style>\s*/\* Fix horizontal scroll white space.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

viewport_meta = '<meta name="viewport" content="width=1200">'

content = content.replace('</head>', viewport_meta + '\n</head>', 1)

fix_css = """
<style>
/* Fix horizontal scroll white space for mobile while keeping PC layout intact */
@media screen and (max-width: 1200px) {
    html, body {
        overflow-x: hidden !important;
        width: 1200px !important;
    }
}
/* Hide 1x1 tracking pixels that sometimes break layout */
img[width="1"][height="1"], img[width="0"][height="0"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""
content = content.replace('</head>', fix_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed viewport 2 applied.")
