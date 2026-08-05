import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Aggressively remove ALL previous injected styles from any version
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Final, Most Robust Responsive CSS (v15)
# This version focuses on NOT hiding core containers, just adjusting their width and layout.
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES v15 */
@media screen and (max-width: 900px) {
    /* Reset Document and Page */
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #fff !important;
        position: relative !important;
    }

    #a-page {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
        overflow-x: hidden !important;
    }

    * {
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* --- HEADER: KEEP ALL BUT MAKE IT WORK --- */
    #navbar, #navbar-main, header, #nav-belt, #nav-main, #nav-tools {
        display: block !important;
        width: 100% !important;
        background: #232f3e !important;
        height: auto !important;
        position: relative !important;
        left: 0 !important;
        top: 0 !important;
        float: none !important;
    }
    
    #nav-belt {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        padding: 10px !important;
    }
    
    .nav-left, .nav-right, .nav-fill {
        display: block !important;
        width: 100% !important;
        float: none !important;
        text-align: center !important;
    }
    
    #nav-logo {
        margin: 0 auto 10px auto !important;
        display: inline-block !important;
    }
    
    #nav-tools {
        display: flex !important;
        justify-content: space-around !important;
        padding: 10px 0 !important;
        border-top: 1px solid #37475a;
    }

    /* Scrollable Horizontal Menu (Professional 3-dot alignment) */
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
        float: none !important;
        padding: 0 10px !important;
    }
    
    #nav-xshop a {
        padding: 5px 15px !important;
        color: #fff !important;
        font-size: 14px !important;
        text-decoration: none !important;
    }

    /* Hide desktop-only bulky search to keep it clean */
    #nav-search, #nav-flyout-anchor, .nav-sprite-container {
        display: none !important;
    }

    /* --- CONTENT AREA --- */
    .a-container, .a-row, .a-column, .a-span12, div[class*="bxcGridContainer"] {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
        position: relative !important;
    }

    img {
        width: 100% !important;
        height: auto !important;
        display: block !important;
    }

    /* --- FOOTER: PERFECT CENTER ALIGNMENT --- */
    #navFooter {
        display: block !important;
        background: #232f3e !important;
        color: white !important;
        padding: 40px 15px !important;
        width: 100% !important;
        text-align: center !important;
    }

    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        margin-bottom: 30px !important;
        display: block !important;
        float: none !important;
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
    }

    #navFooter li {
        margin-bottom: 10px !important;
        text-align: center !important;
    }

    #navFooter a {
        color: #ccc !important;
        font-size: 14px !important;
        text-decoration: none !important;
    }

    /* Bottom Copyright/Legal Bar */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        background: #131a22 !important;
        padding: 25px 15px !important;
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
    }

    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 10px !important;
    }
}
</style>
"""

# Find the end of head and inject there
if '</head>' in content:
    content = content.replace('</head>', better_responsive_css + '</head>', 1)
else:
    # Fallback if head tag is weird
    content = content.replace('<body', better_responsive_css + '<body', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 15 applied.")
