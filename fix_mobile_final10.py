import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the refined responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v10 */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* --- SPRITE FIX --- */
    .nav-sprite, .nav-icon, img[src*="sprite"], img[src*="pixel"], .nav-logo-base {
        max-width: none !important;
        width: auto !important;
        display: inline-block !important;
    }
    
    /* Hide tracking/junk images */
    body > img, #a-page > img, img[height="1"], img[width="1"] {
        display: none !important;
    }

    /* --- HEADER FIX (No Overlap) --- */
    header#navbar-main, #navbar, #nav-belt, #nav-main {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        height: auto !important;
        top: auto !important;
        left: auto !important;
        margin: 0 !important;
        z-index: 100 !important;
    }
    
    #nav-belt {
        padding: 10px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
    }
    
    #nav-logo {
        float: none !important;
        margin-bottom: 10px !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    .nav-left, .nav-right, .nav-fill {
        width: 100% !important;
        float: none !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Hide bulky search/flyouts on mobile for now to keep it clean */
    #nav-search, #nav-flyout-anchor, .nav-sprite-container {
        display: none !important;
    }
    
    #nav-tools {
        display: flex !important;
        justify-content: space-around !important;
        width: 100% !important;
        padding: 10px 0 !important;
        float: none !important;
        border-top: 1px solid #37475a;
    }
    
    #nav-tools a {
        color: white !important;
        text-decoration: none !important;
        font-size: 13px !important;
    }

    /* Professional Horizontal Menu */
    #nav-xshop-container {
        display: block !important;
        width: 100% !important;
        background: #37475a !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        -webkit-overflow-scrolling: touch;
        padding: 10px 0 !important;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 0 10px !important;
        float: none !important;
    }
    
    #nav-xshop a {
        padding: 5px 15px !important;
        color: #fff !important;
        font-size: 14px !important;
        text-decoration: none !important;
        display: inline-block !important;
    }

    /* --- CONTENT FLOW --- */
    #a-page {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right, div[class*="bxcGridContainer"] {
        width: 100% !important;
        max-width: 100vw !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Ensure hero images and content banners scale */
    img {
        max-width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* --- FOOTER FIX (Alignment) --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 10px !important;
        width: 100% !important;
        text-align: center !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        margin: 0 0 30px 0 !important;
        padding: 0 !important;
        float: none !important;
        display: block !important;
        text-align: center !important;
    }
    
    .navFooterColHead {
        display: block !important;
        margin-bottom: 10px !important;
        font-size: 16px !important;
        color: #fff !important;
        font-weight: bold !important;
    }
    
    #navFooter ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    #navFooter li {
        margin-bottom: 10px !important;
        text-align: center !important;
    }
    
    #navFooter a {
        color: #ddd !important;
        font-size: 14px !important;
        text-decoration: none !important;
    }

    /* Bottom Section */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        width: 100% !important;
        background: #131a22 !important;
        padding: 20px 10px !important;
        margin: 0 !important;
        border: none !important;
        text-align: center !important;
    }
    
    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 10px !important;
        padding: 0 !important;
        margin-bottom: 10px !important;
    }
    
    .navFooterLine li, .navFooterCopyright li {
        display: inline-block !important;
        margin: 5px !important;
    }
    
    .navFooterDescItem {
        width: 100% !important;
        margin-bottom: 20px !important;
        padding: 0 10px !important;
    }
    
    .navFooterDescSpacer {
        display: none !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #999 !important;
        font-size: 12px !important;
        margin-top: 10px !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 10 applied.")
