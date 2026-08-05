import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove previous injected styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Final Polished Responsive CSS (v14)
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v14 */
@media screen and (max-width: 900px) {
    /* Full width reset */
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

    /* --- HEADER: NO BLANK AREAS --- */
    #navbar, #navbar-main, header, #nav-belt, #nav-main {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 1000 !important;
    }

    /* Fix Header Items Visibility */
    #nav-belt {
        padding: 10px 15px !important;
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
    }

    #nav-logo {
        display: block !important;
        float: none !important;
        margin: 0 !important;
    }

    /* Professional Scrollable Menu (Menu Bar) */
    #nav-main {
        border-top: 1px solid #37475a !important;
        background: #37475a !important;
    }

    #nav-xshop-container {
        display: block !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        -webkit-overflow-scrolling: touch;
        padding: 12px 5px !important;
    }

    #nav-xshop {
        display: inline-flex !important;
        float: none !important;
        padding: 0 !important;
    }

    #nav-xshop a, #nav-tools a {
        color: white !important;
        padding: 0 15px !important;
        font-size: 14px !important;
        text-decoration: none !important;
        display: inline-block !important;
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
        padding: 0 20px !important;
        float: none !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
    }

    .navFooterColHead {
        color: #fff !important;
        font-weight: bold !important;
        font-size: 16px !important;
        margin-bottom: 12px !important;
        display: block !important;
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
        width: 100% !important;
    }

    #navFooter a {
        color: #ccc !important;
        font-size: 14px !important;
        text-align: center !important;
        display: block !important;
    }

    /* Bottom Copyright Section */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        background: #131a22 !important;
        padding: 30px 15px !important;
        width: 100% !important;
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
        padding: 0 !important;
    }

    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 10px !important;
        text-align: center !important;
    }
    
    /* Ensure banners fit screen */
    .a-container, #a-page, .a-row, div[class*="bxcGridContainer"] {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    img {
        max-width: 100% !important;
        height: auto !important;
    }
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 14 applied.")
