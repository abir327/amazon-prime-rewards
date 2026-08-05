import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the minimal, perfect responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v5 */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        min-width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        padding-bottom: 80px !important;
    }

    * {
        max-width: 100vw !important;
        min-width: 0 !important;
        box-sizing: border-box !important;
    }

    /* Hide ALL possible desktop navigation elements */
    #navbar, header, #nav-main, #nav-belt, #nav-tools, #nav-top, .nav-assistant, 
    #nav-flyout-anchor, .nav-sprite-container, #nav-search-keywords, .nav-left, .nav-right,
    .nav-fill, #nav-search {
        display: none !important;
    }

    /* Custom mobile header */
    body::before {
        content: "Amazon";
        display: block;
        background: #232f3e;
        color: white;
        padding: 15px 20px;
        font-size: 22px;
        font-family: Arial, sans-serif;
        font-weight: bold;
        text-align: center;
        width: 100% !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        margin: 0 !important;
        position: relative;
        z-index: 9999;
    }

    /* Hide left sidebar */
    .apb-browse-left-nav,
    .apb-default-search-refinements-leftnav,
    #s-refinements,
    #leftCol {
        display: none !important;
        width: 0 !important;
        visibility: hidden !important;
    }

    /* Force main content container to take full width */
    #a-page, .a-container, #centerCol, #rightCol, .a-column, .a-span12, .apb-default-slot,
    .apb-browse-two-col-center-margin-right, .apb-browse-col-pad-right,
    div[class*="bxcGridContainer"], .a-row {
        width: 100% !important;
        max-width: 100vw !important;
        min-width: 0 !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: visible !important;
    }

    /* Fix grid layouts */
    div[class*="bxcGridColumn"], div[class*="bxcGridRow"] {
        display: block !important;
        width: 100% !important;
        max-width: 100vw !important;
        min-width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        position: static !important;
        left: auto !important;
        right: auto !important;
        transform: none !important;
        float: none !important;
        clear: both !important;
    }
    
    /* Make text boxes use full width and wrap */
    div[class*="bxcGridText"] {
        width: 100% !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        padding: 15px !important;
    }
    
    /* Center the neon button properly */
    .neon-btn-container {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        padding: 30px 0 !important;
        margin: 0 auto !important;
    }
    
    /* Images */
    img, iframe, video {
        max-width: 100vw !important;
        width: 100% !important;
        height: auto !important;
        object-fit: contain;
        display: block !important;
        margin: 0 auto !important;
    }
    
    /* Fix tables */
    .apb-default-slot table, div[class*="bxcGridContainer"] table, table {
        display: block !important;
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: auto !important;
    }

    /* Hide spacer images on mobile */
    img[src*="SpacerTest"], img[alt*="white space"] {
        display: none !important;
    }

    /* Footer - FORCE IT TO BE VISIBLE AND WRAP PROPERLY */
    #navFooter {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        margin: 0 !important;
        padding: 20px 0 !important;
        width: 100% !important;
        background: #232f3e !important;
    }
    
    #navFooter, .navFooterLine, .navFooterColHead, .navFooterDescLine {
        white-space: normal !important;
        width: 100% !important;
        max-width: 100vw !important;
        margin: 0 !important;
        text-align: center !important;
    }
    
    .navFooterVerticalColumn {
        display: block !important;
        width: 100% !important;
    }
    
    .navFooterCol {
        width: 100% !important;
        float: none !important;
        margin-bottom: 20px !important;
        padding: 0 10px !important;
    }
    
    .navFooterLinkCol {
        width: 100% !important;
        margin-bottom: 20px !important;
    }
    
    /* Footer copyright alignment fix */
    .navFooterCopyright {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        padding: 20px 10px !important;
        background: #131a22 !important;
        width: 100% !important;
    }
    
    .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 10px !important;
        margin-bottom: 10px !important;
        padding: 0 !important;
        list-style: none !important;
    }
    
    .navFooterCopyright li {
        border-right: 1px solid #444;
        padding: 0 10px !important;
        margin: 5px 0 !important;
        display: inline-block !important;
    }
    
    .navFooterCopyright li.nav_last {
        border-right: none !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        margin-top: 10px !important;
        color: #999 !important;
    }

    /* Ensure the footer lists wrap as well */
    #navFooter ul {
        width: 100% !important;
        display: block !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    #navFooter li {
        white-space: normal !important;
        word-wrap: break-word !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }
}
/* Unconditionally hide tracking pixels */
img[width="1"][height="1"], img[width="0"][height="0"], img[width="1"], img[src*="amazon-adsystem"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 5 applied.")
