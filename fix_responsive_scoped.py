import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove aggressive css block
content = re.sub(r'<style>\s*/\* Aggressive mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)

responsive_css = """
<style>
/* Scoped mobile responsive overrides for Amazon */
@media (max-width: 768px) {
    html, body {
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    * {
        min-width: 0 !important;
        box-sizing: border-box !important;
    }

    /* Fix navbar */
    #navbar, #nav-belt, #nav-main, .nav-fill, .nav-left, .nav-right, #nav-search, #nav-tools {
        width: 100% !important;
        max-width: 100% !important;
    }
    
    #nav-belt {
        display: flex !important;
        flex-wrap: wrap !important;
    }

    /* Ensure images scale */
    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* Fix specific amazon container widths */
    .a-container, .a-row, .a-column, .a-box, .a-box-inner, #a-page, .celwidget, .a-section, #dp-container, #dp, #centerCol, #rightCol, #leftCol, #wayfinding-breadcrumbs-container {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }

    /* Fix tables */
    table {
        max-width: 100% !important;
    }

    /* Fix flex/grid issues */
    .a-span1, .a-span2, .a-span3, .a-span4, .a-span5, .a-span6, .a-span7, .a-span8, .a-span9, .a-span10, .a-span11, .a-span12 {
        width: 100% !important;
        float: none !important;
    }
}
</style>
"""

if "/* Scoped mobile responsive overrides for Amazon */" not in content:
    content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Scoped responsive CSS applied.")
