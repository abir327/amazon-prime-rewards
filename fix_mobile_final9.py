import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the professional responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v9 */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #f3f3f3 !important;
    }

    * {
        box-sizing: border-box !important;
    }

    /* --- SPRITE FIX (CRITICAL) --- */
    /* Prevent sprite sheets from expanding to full width */
    .nav-sprite, .nav-icon, img[src*="sprite"], img[src*="pixel"], .nav-logo-base {
        width: auto !important;
        max-width: none !important;
        display: inline-block !important;
    }
    
    /* Hide tracking pixels and scattered preload icons */
    img[height="1"], img[width="1"], body > img, #a-page > img {
        display: none !important;
    }

    /* --- HEADER FIXES (No Overlap, Professional) --- */
    #navbar, #navbar-main {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        margin: 0 !important;
        z-index: 1000 !important;
    }
    
    #nav-belt {
        display: flex !important;
        flex-direction: column !important;
        padding: 10px !important;
    }
    
    #nav-logo {
        display: flex !important;
        justify-content: center !important;
        margin-bottom: 10px !important;
        float: none !important;
    }
    
    #nav-tools {
        display: flex !important;
        justify-content: space-around !important;
        width: 100% !important;
        float: none !important;
        border-top: 1px solid #37475a;
        padding-top: 10px !important;
    }
    
    #nav-tools a {
        color: white !important;
        text-decoration: none !important;
        font-size: 13px !important;
    }

    /* Hide desktop-only bulky nav */
    #nav-search, #nav-main {
        display: none !important;
    }
    
    /* Professional Scrollable Menu (The "PC Items" in mobile) */
    #nav-xshop-container {
        display: block !important;
        width: 100% !important;
        background: #37475a !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        -webkit-overflow-scrolling: touch;
        padding: 10px 0 !important;
        border-bottom: 1px solid #131a22;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 0 10px !important;
        float: none !important;
    }
    
    #nav-xshop a {
        padding: 5px 15px !important;
        color: #ddd !important;
        font-size: 14px !important;
        text-decoration: none !important;
    }

    /* --- CONTENT FLOW --- */
    #a-page {
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }

    .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right, div[class*="bxcGridContainer"] {
        width: 100% !important;
        max-width: 100vw !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Content Images (Banners) should be full width */
    div[class*="bxcGrid"] img, .a-row img, .hero-image img, #centerCol img {
        width: 100% !important;
        height: auto !important;
        display: block !important;
    }

    /* --- FOOTER FIXES (Alignment & Spacing) --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 20px !important;
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
        color: white !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        font-size: 16px !important;
    }
    
    #navFooter ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
        text-align: center !important;
    }
    
    #navFooter li {
        margin-bottom: 8px !important;
        text-align: center !important;
    }
    
    #navFooter a {
        color: #ccc !important;
        text-decoration: none !important;
        font-size: 14px !important;
    }

    /* Bottom Copyright Alignment */
    .navFooterCopyright, .navFooterLine {
        display: block !important;
        width: 100% !important;
        background: #131a22 !important;
        padding: 20px 10px !important;
        margin: 0 !important;
        border: none !important;
        text-align: center !important;
    }
    
    .navFooterCopyright ul, .navFooterLine ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 15px !important;
        margin-bottom: 10px !important;
    }
    
    .navFooterCopyright li, .navFooterLine li {
        display: inline-block !important;
        margin: 5px !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 15px !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 9 applied.")
