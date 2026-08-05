import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL previous injected styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Final Professional Responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v12 */
@media screen and (max-width: 900px) {
    /* Reset document flow */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* Hide messy desktop sprites and loose images */
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

    /* Clean Mobile Belt */
    #nav-belt {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 10px 15px !important;
        height: auto !important;
        min-height: 50px !important;
    }

    /* Logo Styling */
    #nav-logo {
        display: flex !important;
        align-items: center !important;
        margin: 0 !important;
        float: none !important;
        height: 40px !important;
    }
    
    #nav-logo::after {
        content: "amazon";
        color: white;
        font-size: 22px;
        font-weight: bold;
        font-family: "Amazon Ember", Arial, sans-serif;
    }

    /* Hide Bulky Desktop Items */
    #nav-main, #nav-tools, #nav-search, #nav-global-location-slot, .nav-right, .nav-left {
        display: none !important;
    }

    /* THE "3-DOT" MENU FEEL: Scrollable Horizontal Menu */
    #nav-xshop-container {
        display: block !important;
        background: #37475a !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        padding: 10px 0 !important;
        border-bottom: 1px solid #131a22;
        -webkit-overflow-scrolling: touch;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 0 10px !important;
        float: none !important;
    }
    
    #nav-xshop a {
        padding: 0 15px !important;
        color: #fff !important;
        font-size: 14px !important;
        text-decoration: none !important;
        font-weight: 500;
        display: inline-block !important;
    }

    /* --- CONTENT AREA: FIX OVERLAP --- */
    #a-page {
        display: block !important;
        position: relative !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
        z-index: 1 !important;
    }

    /* Force all containers to stack and not overlap */
    .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right, div[class*="bxcGridContainer"] {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        float: none !important;
        position: relative !important;
        display: block !important;
    }

    /* Scale banners and hero images */
    img {
        max-width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* --- FOOTER: PERFECT CENTER ALIGNMENT --- */
    #navFooter {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 0 !important;
        width: 100% !important;
        text-align: center !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        margin-bottom: 30px !important;
        padding: 0 15px !important;
        float: none !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    
    .navFooterColHead {
        color: #fff !important;
        font-weight: bold !important;
        font-size: 16px !important;
        margin-bottom: 12px !important;
        display: block !important;
        text-align: center !important;
    }
    
    #navFooter ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    
    #navFooter li {
        margin-bottom: 10px !important;
        text-align: center !important;
    }
    
    #navFooter a {
        color: #ccc !important;
        text-decoration: none !important;
        font-size: 14px !important;
    }

    /* Bottom Copyright/Legal Section */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        background: #131a22 !important;
        padding: 25px 15px !important;
        width: 100% !important;
        margin: 0 !important;
        border: none !important;
    }
    
    .navFooterLine ul, .navFooterCopyright ul {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 12px !important;
        margin-bottom: 15px !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 5px !important;
        text-align: center !important;
    }
    
    /* Clean up the description items at the bottom */
    .navFooterDescItem {
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 15px !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 12 applied.")
