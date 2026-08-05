import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the professional responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v7 */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        padding-bottom: 100px !important; /* Bottom scroll space */
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* --- HEADER FIXES --- */
    #navbar, #nav-belt, #nav-main {
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
    }
    
    #nav-logo {
        padding: 10px !important;
        display: block !important;
        text-align: center;
    }
    
    #nav-tools {
        display: flex !important;
        justify-content: space-around !important;
        width: 100% !important;
        padding: 10px 0 !important;
    }

    /* Hide bulky desktop nav items that break layout */
    #nav-search, .nav-sprite-container, #nav-flyout-anchor {
        display: none !important;
    }
    
    /* Make the horizontal menu scrollable (Professional 3-dot feel) */
    #nav-xshop-container {
        overflow-x: auto !important;
        white-space: nowrap !important;
        display: block !important;
        background: #37475a !important;
        -webkit-overflow-scrolling: touch;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 10px !important;
    }
    
    #nav-xshop a {
        padding: 0 15px !important;
        color: white !important;
        font-size: 14px !important;
        text-decoration: none !important;
    }

    /* Hide the messy sprite images showing at the top */
    body > img[src*="sprite"], #a-page > img[src*="sprite"], .nav-sprite {
        display: none !important;
    }

    /* --- CONTENT FIXES --- */
    #a-page, .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right, div[class*="bxcGridContainer"] {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    div[class*="bxcGridColumn"], div[class*="bxcGridRow"] {
        display: block !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 10px !important;
        position: static !important;
    }
    
    img {
        max-width: 100vw !important;
        width: 100% !important;
        height: auto !important;
    }

    /* --- FOOTER FIXES --- */
    #navFooter {
        background: #232f3e !important;
        color: white !important;
        padding: 20px 10px !important;
        text-align: center !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        display: block !important;
        width: 100% !important;
        margin: 0 0 20px 0 !important;
        padding: 0 !important;
        float: none !important;
    }

    /* Fix the copyright and bottom link alignment */
    .navFooterCopyright, .navFooterLine {
        display: block !important;
        text-align: center !important;
        width: 100% !important;
        padding: 15px 0 !important;
        border: none !important;
    }
    
    .navFooterCopyright ul, .navFooterLine ul {
        padding: 0 !important;
        margin: 0 auto 10px auto !important;
        list-style: none !important;
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
    }
    
    .navFooterCopyright li, .navFooterLine li {
        display: inline-block !important;
        margin: 5px 10px !important;
        white-space: nowrap !important;
    }

    .navFooterCopyright span {
        display: block !important;
        margin-top: 10px !important;
        font-size: 12px !important;
        color: #ccc !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 7 applied.")
