import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL previous injected styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Professional Mobile Clean-up CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v11 */
@media screen and (max-width: 900px) {
    /* Reset and Base */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
        -webkit-text-size-adjust: 100%;
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* Hide bulky desktop noise and sprites */
    .nav-sprite, .nav-icon, img[src*="sprite"], img[src*="pixel"], 
    body > img, #a-page > img, .nav-sprite-container {
        display: none !important;
    }

    /* --- PROFESSIONAL MOBILE HEADER --- */
    #navbar, #navbar-main, header {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 1000 !important;
    }

    /* Create a clean mobile logo row */
    #nav-belt {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 10px 15px !important;
        height: 60px !important;
    }

    #nav-logo {
        display: block !important;
        margin: 0 !important;
        float: none !important;
    }
    
    /* Show "Amazon" text if logo is hidden/broken */
    #nav-logo::after {
        content: "amazon";
        color: white;
        font-size: 24px;
        font-weight: bold;
        font-family: Arial, sans-serif;
    }

    /* Hide messy desktop sub-headers */
    #nav-main, #nav-tools, #nav-search, #nav-global-location-slot {
        display: none !important;
    }

    /* Scrollable Horizontal Menu (Professional Links) */
    #nav-xshop-container {
        display: block !important;
        background: #37475a !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        padding: 12px 0 !important;
        border-bottom: 1px solid #131a22;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 0 10px !important;
    }
    
    #nav-xshop a {
        padding: 0 15px !important;
        color: #fff !important;
        font-size: 14px !important;
        text-decoration: none !important;
        font-weight: 500;
    }

    /* --- CONTENT AREA (Fix Overlap) --- */
    #a-page {
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
        position: relative !important;
        clear: both !important;
    }

    .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        float: none !important;
    }

    /* Fix the $1000 banner scaling */
    div[class*="bxcGridContainer"], .hero-image, .ad-banner {
        width: 100% !important;
        overflow: hidden !important;
    }

    img {
        max-width: 100% !important;
        height: auto !important;
        display: block !important;
    }

    /* --- FOOTER (Perfect Alignment) --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 0 !important;
        width: 100% !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 30px !important;
        padding: 0 20px !important;
        float: none !important;
        display: block !important;
    }
    
    .navFooterColHead {
        color: #fff !important;
        font-weight: bold !important;
        font-size: 16px !important;
        margin-bottom: 15px !important;
        display: block !important;
    }
    
    #navFooter ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    #navFooter li {
        margin-bottom: 12px !important;
    }
    
    #navFooter a {
        color: #ccc !important;
        text-decoration: none !important;
        font-size: 14px !important;
    }

    /* Bottom Copyright Alignment */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        background: #131a22 !important;
        padding: 25px 15px !important;
        margin: 0 !important;
        border: none !important;
    }
    
    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 15px !important;
        padding: 0 !important;
        margin: 0 0 15px 0 !important;
    }
    
    .navFooterLine li, .navFooterCopyright li {
        display: inline-block !important;
        margin: 0 !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 5px !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 11 applied.")
