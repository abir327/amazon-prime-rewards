import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add viewport meta tag if not present
if 'name="viewport"' not in content:
    content = content.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">', 1)

responsive_css = """
<style>
/* Safe mobile responsive overrides for Amazon */
@media (max-width: 768px) {
    body, html {
        overflow-x: hidden;
        width: 100%;
    }
    
    /* Make the overall container fluid */
    #a-page, .a-container, .a-row {
        min-width: 0 !important;
        max-width: 100% !important;
    }

    /* Fix the header so it doesn't force a wide page, but don't break its internal layout */
    #navbar {
        min-width: 0 !important;
        width: 100% !important;
        overflow-x: auto !important; /* Allow header to scroll horizontally if needed, instead of breaking page width */
    }

    /* Hide the left sidebar navigation on mobile to save space */
    .apb-browse-left-nav {
        display: none !important;
    }

    /* Make the main content take full width */
    .apb-browse-two-col-center-margin-right,
    #centerCol, #rightCol, .a-column {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        box-sizing: border-box !important;
    }

    /* Ensure images and tables are responsive */
    img, table {
        max-width: 100% !important;
        height: auto !important;
    }
}
</style>
"""

# Ensure we remove any old responsive hacks just in case
content = re.sub(r'<style>\s*/\* Safe mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)

content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Safe mobile layout applied.")
