import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the hardcoded viewport
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

# Add the proper responsive viewport
viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
content = content.replace('</head>', viewport_meta + '\n</head>', 1)

# Remove the tracking pixels fix if it's there
content = re.sub(r'<style>\s*/\* Hide 1x1 tracking pixels.*?</style>', '', content, flags=re.DOTALL)

# Add mobile responsive CSS
responsive_css = """
<style>
/* Safe mobile responsive overrides for Amazon */
@media screen and (max-width: 768px) {
    /* Prevent horizontal scrolling entirely on the document level */
    html, body {
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
    }
    
    * {
        box-sizing: border-box !important;
    }

    /* Force all containers to not exceed viewport width */
    #a-page, .a-container, .a-row, .a-popover-preload, div {
        max-width: 100vw !important;
    }

    /* Fix the header so it doesn't force a wide page */
    #navbar, #nav-main, #nav-belt, .nav-fill, .nav-right, #nav-tools, .nav-left, #nav-search {
        max-width: 100% !important;
        min-width: 0 !important;
    }
    
    /* Allow the header to scroll horizontally independently if needed, without stretching body */
    header, #navbar {
        overflow-x: hidden !important;
        width: 100% !important;
    }

    /* Hide the left sidebar navigation on mobile to save space */
    .apb-browse-left-nav {
        display: none !important;
    }

    /* Make the main content take full width */
    .apb-browse-two-col-center-margin-right,
    #centerCol, #rightCol, .a-column, .a-span12, .apb-default-slot {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding-left: 5px !important;
        padding-right: 5px !important;
    }

    /* Ensure images and tables are responsive */
    img, table, iframe, video {
        max-width: 100% !important;
        height: auto !important;
    }
    
    /* specific amazon table overrides */
    table, thead, tbody, th, td, tr {
        display: block !important;
        max-width: 100% !important;
        width: 100% !important;
    }

    /* Footer fixes */
    .navFooterLine, .navFooterColHead, .navFooterDescLine {
        white-space: normal !important;
    }
    .navFooterVerticalColumn {
        display: block !important;
        width: 100% !important;
    }
    .navFooterCol {
        width: 100% !important;
        float: none !important;
        margin-bottom: 20px !important;
    }
    
    /* Neon button responsiveness */
    .neon-btn-container {
        width: 100% !important;
        max-width: 100% !important;
        overflow: hidden !important;
    }
    .neon-btn {
        width: 100% !important;
        max-width: 300px !important;
        margin: 0 auto !important;
        display: flex !important;
    }
}
/* Hide some extra amazon tracking image pixels that might cause scroll */
img[width="1"][height="1"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""

content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile responsive layout applied.")
