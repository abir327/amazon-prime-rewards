import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up ALL previous injected mobile styles to ensure no conflicts
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the STABLE surgical CSS (v21)
surgical_css = """
<style>
/* CLEAN MOBILE OVERRIDES v21 */
@media screen and (max-width: 900px) {
    /* Safe Document Reset */
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        -webkit-text-size-adjust: 100%;
    }

    #a-page {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        display: block !important;
    }

    /* --- STABLE HEADER & 3-DOT MENU --- */
    #navbar, #nav-belt, #nav-main {
        width: 100% !important;
        background-color: #232f3e !important;
        display: block !important;
        position: relative !important;
    }

    #nav-belt {
        padding: 10px 50px 10px 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
    }

    /* The 3-dot Menu Icon */
    #nav-belt::after {
        content: "\\22EE" !important;
        color: #fff !important;
        font-size: 28px !important;
        position: absolute !important;
        right: 15px !important;
        top: 10px !important;
        cursor: pointer !important;
        z-index: 9999;
    }

    /* --- STABLE CONTENT STACKING --- */
    .a-container, .a-row, .a-section, div[class*="bxcGridContainer"] {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 10px !important;
        box-sizing: border-box !important;
    }

    img {
        max-width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* --- STABLE FOOTER RESPONSIVE --- */
    #navFooter {
        display: block !important;
        background-color: #232f3e !important;
        color: #fff !important;
        padding: 30px 10px !important;
        width: 100% !important;
        text-align: center !important;
        clear: both !important;
    }

    /* Center and stack footer columns */
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        float: none !important;
        margin: 0 0 25px 0 !important;
        display: block !important;
        text-align: center !important;
    }

    .navFooterColHead {
        color: #fff !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
        font-size: 16px !important;
    }

    #navFooter ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    #navFooter a {
        color: #ddd !important;
        display: block !important;
        padding: 6px 0 !important;
        font-size: 14px !important;
    }

    /* Bottom Copyright Alignment */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        background-color: #131a22 !important;
        padding: 20px 10px !important;
        text-align: center !important;
        border: none !important;
    }

    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 12px !important;
        margin-bottom: 10px !important;
    }
}
</style>
"""

# Inject into the head
if '</head>' in content:
    content = content.replace('</head>', surgical_css + '</head>', 1)
else:
    content = content.replace('<body', surgical_css + '<body', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 21 (Re-stabilized) applied.")
