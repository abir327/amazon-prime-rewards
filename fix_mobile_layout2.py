import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we remove old blocks
content = re.sub(r'<style>\s*/\* Safe mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)

responsive_css = """
<style>
/* Safe mobile responsive overrides for Amazon */
@media (max-width: 768px) {
    /* Prevent horizontal scrolling entirely on the document level */
    html, body {
        width: 100vw !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Make the overall container fluid and prevent it from forcing a wider width */
    #a-page, .a-container, .a-row, .a-popover-preload {
        min-width: 0 !important;
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
    }

    /* Fix the header so it doesn't force a wide page, but don't break its internal layout */
    #navbar {
        min-width: 0 !important;
        width: 100% !important;
        overflow-x: auto !important; /* Allow header to scroll horizontally if needed */
    }

    /* Hide the left sidebar navigation on mobile to save space */
    .apb-browse-left-nav {
        display: none !important;
    }

    /* Make the main content take full width */
    .apb-browse-two-col-center-margin-right,
    #centerCol, #rightCol, .a-column {
        width: 100% !important;
        max-width: 100vw !important;
        float: none !important;
        margin: 0 !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        box-sizing: border-box !important;
    }

    /* Ensure images and tables are responsive */
    img, table, iframe, video {
        max-width: 100% !important;
        height: auto !important;
    }
    
    table {
        display: block !important;
        overflow-x: auto !important;
    }
}
</style>
"""

content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Safe mobile layout 2 applied.")
