import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL previous injected styles to start fresh
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Improved Responsive CSS (v13)
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v13 */
@media screen and (max-width: 900px) {
    /* Basic Page Setup */
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

    /* --- HEADER FIX (NO BLANK AREAS) --- */
    #navbar, #navbar-main, header {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        height: auto !important;
        z-index: 1000 !important;
    }

    #nav-belt {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 10px !important;
    }

    #nav-logo {
        display: block !important;
        float: none !important;
        margin: 0 !important;
    }

    /* Ensure text is visible in header items */
    .nav-a, .nav-link, #nav-tools a, #nav-xshop a {
        color: white !important;
        text-decoration: none !important;
    }

    /* Fix the horizontal scrollable menu (Professional 3-dot alignment) */
    #nav-xshop-container {
        display: block !important;
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
        font-size: 14px !important;
    }

    /* Hide only the messy background sprite images that overlap */
    body > img[src*="sprite"], #a-page > img[src*="sprite"] {
        display: none !important;
    }

    /* --- CONTENT FIX --- */
    #a-page {
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }

    .a-container, .a-row, .a-column, .a-span12, 
    .apb-browse-two-col-center-margin-right, div[class*="bxcGridContainer"] {
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* --- FOOTER ALIGNMENT (PERFECTLY CENTERED) --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 10px !important;
        text-align: center !important;
        width: 100% !important;
    }

    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        display: block !important;
        width: 100% !important;
        margin: 0 0 30px 0 !important;
        padding: 0 !important;
        float: none !important;
        text-align: center !important;
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
        margin-bottom: 10px !important;
        text-align: center !important;
    }

    #navFooter a {
        color: #ddd !important;
        font-size: 14px !important;
    }

    /* Bottom Section Alignment */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        width: 100% !important;
        background: #131a22 !important;
        padding: 25px 10px !important;
        margin: 0 !important;
        border: none !important;
        text-align: center !important;
    }

    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 15px !important;
        margin-bottom: 15px !important;
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

print("Mobile fix 13 applied.")
