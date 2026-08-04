import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old fixes
content = re.sub(r'<style>\s*/\* Fix horizontal scroll white space.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

# Remove the JSON parse error stub, which is not really fixing the root cause, and might cause other errors. 
# Also remove window.ueLogError
content = re.sub(r'<script>window.ueLogError = function\(\) \{\};</script>\n?', '', content)

# Use a viewport of 1000px which is typical for Amazon's min-width on desktop, but adding initial-scale to prevent zooming out too much
viewport_meta = '<meta name="viewport" content="width=1000, initial-scale=1.0">'
content = content.replace('</head>', viewport_meta + '\n</head>', 1)

fix_css = """
<style>
/* Fix horizontal scroll white space for mobile while keeping PC layout intact */
html, body {
    overflow-x: hidden !important; /* This is the key to stopping the side scroll */
    width: 100% !important; /* Use 100% of the viewport width */
    min-width: 1000px !important; /* Make sure the content doesn't get squished */
    margin: 0 !important;
    padding: 0 !important;
}

/* Make sure the main wrappers don't overflow */
#a-page, .a-container {
    overflow-x: hidden !important;
    max-width: 100% !important; 
}

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

print("Fixed viewport 4 applied.")
