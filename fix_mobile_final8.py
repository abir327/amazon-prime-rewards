import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the professional responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v8 */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        position: relative !important;
    }

    /* Remove any fake header from previous versions */
    body::before { display: none !important; content: none !important; }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* --- HEADER FIXES (No Overlap) --- */
    #navbar, #navbar-main {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        height: auto !important;
        background: #232f3e !important;
        margin: 0 !important;
        padding: 0 !important;
        top: 0 !important;
        z-index: 100 !important;
    }
    
    #nav-belt, #nav-main {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        height: auto !important;
        background: inherit !important;
    }
    
    #nav-logo {
        padding: 10px !important;
        display: flex !important;
        justify-content: center !important;
        float: none !important;
    }
    
    /* Show mobile-friendly tools */
    #nav-tools {
        display: flex !important;
        justify-content: center !important;
        gap: 15px !important;
        width: 100% !important;
        padding: 10px 0 !important;
        float: none !important;
    }
    
    #nav-tools a {
        color: white !important;
        text-decoration: none !important;
        font-size: 14px !important;
    }

    /* Hide bulky items */
    #nav-search, .nav-sprite-container, #nav-flyout-anchor, .nav-search-scope {
        display: none !important;
    }
    
    /* Scrollable Menu (Professional Alignment) */
    #nav-xshop-container {
        display: block !important;
        width: 100% !important;
        background: #37475a !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        -webkit-overflow-scrolling: touch;
        padding: 5px 0 !important;
    }
    
    #nav-xshop {
        display: inline-flex !important;
        padding: 5px 10px !important;
        float: none !important;
    }
    
    #nav-xshop a {
        padding: 5px 12px !important;
        color: white !important;
        font-size: 13px !important;
    }

    /* Prevent hidden sprites/text from leaking */
    .nav-sprite, .nav-icon, .nav-logo-base, .nav-logo-ext, .nav-logo-locale {
        display: none !important;
    }
    
    body > img, #a-page > img {
        display: none !important;
    }

    /* --- CONTENT FLOW (No Overlap) --- */
    #a-page {
        margin-top: 0 !important;
        padding-top: 0 !important;
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

    /* --- FOOTER FIXES (Professional Alignment) --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        padding: 30px 15px !important;
        width: 100% !important;
        text-align: center !important;
    }
    
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        width: 100% !important;
        text-align: center !important;
        margin: 15px 0 !important;
        border: none !important;
    }
    
    /* Center links in footer */
    #navFooter ul, .navFooterLine ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        padding: 0 !important;
        margin: 0 auto !important;
        list-style: none !important;
        gap: 15px !important;
    }
    
    #navFooter li {
        display: inline-block !important;
        margin: 5px !important;
        text-align: center !important;
    }
    
    #navFooter a {
        color: white !important;
        font-size: 13px !important;
        text-decoration: none !important;
    }

    .navFooterCol, .navFooterLinkCol, .navFooterVerticalColumn {
        width: 100% !important;
        margin: 0 0 25px 0 !important;
        padding: 0 !important;
        float: none !important;
        display: block !important;
    }
    
    .navFooterColHead {
        margin-bottom: 10px !important;
        font-size: 16px !important;
        display: block !important;
    }

    /* Bottom Copyright Section */
    .navFooterCopyright {
        padding: 20px 0 !important;
        background: #131a22 !important;
        margin-top: 20px !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #999 !important;
        margin-top: 10px !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 8 applied.")
