import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old fixes
content = re.sub(r'<style>\n/\* Fix horizontal scroll white space.*?</style>\n', '', content, flags=re.DOTALL)
content = re.sub(r'<style>/\* Fix horizontal scroll white space.*?</style>', '', content, flags=re.DOTALL)

# Let's use a regex that's less strict to catch the block
content = re.sub(r'<style>\s*/\* Fix horizontal scroll white space.*?</style>', '', content, flags=re.DOTALL)

content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

# Use a viewport of 1400px which is typical for Amazon's large desktop view
viewport_meta = '<meta name="viewport" content="width=1400">'
content = content.replace('</head>', viewport_meta + '\n</head>', 1)

# Just hide the tracking pixels, no width/overflow constraints on body
fix_css = """
<style>
/* Hide 1x1 tracking pixels that sometimes break layout */
img[width="1"][height="1"], img[width="0"][height="0"], img[width="1"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""
content = content.replace('</head>', fix_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed viewport 6 applied.")
