import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up previous injected mobile styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add v19 CSS - Robust Footer + 3-Dot Icon
v19_css = """
<style>
/* CLEAN MOBILE OVERRIDES v19 */
@media screen and (max-width: 900px) {
    /* Reset */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    #a-page {
        width: 100% !important;
        display: block !important;
    }

    /* --- HEADER & 3-DOT MENU --- */
    #navbar, #nav-belt {
        background-color: #232f3e !important;
        display: block !important;
        width: 100% !important;
        position: relative !important;
        height: auto !important;
    }
    
    #nav-belt {
        padding: 10px 45px 10px 10px !important; /* Space for the 3-dot */
    }

    /* Vertical Ellipsis (3 dots) icon in the header */
    #nav-belt::after {
        content: "\\22EE" !important; 
        color: #ffffff !important;
        font-size: 30px !important;
        position: absolute !important;
        right: 15px !important;
        top: 10px !important;
        font-weight: bold !important;
        z-index: 10000 !important;
        cursor: pointer !important;
    }

    /* --- FOOTER RESPONSIVE OVERHAUL --- */
    #navFooter {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        background-color: #232f3e !important;
        width: 100% !important;
        padding: 40px 0 !important;
        margin: 0 !important;
        clear: both !important;
        text-align: center !important;
    }

    /* Force all major footer containers to stack */
    .navFooterVerticalColumn, .navFooterVerticalRow, .navFooterLinkCol, #navFooter ul, #navFooter li {
        display: block !important;
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
        text-align: center !important;
    }

    .navFooterLinkCol {
        margin-bottom: 30px !important;
        padding: 0 20px !important;
    }

    .navFooterColHead {
        display: block !important;
        font-size: 18px !important;
        font-weight: bold !important;
        color: #ffffff !important;
        margin-bottom: 15px !important;
        text-align: center !important;
    }

    #navFooter a {
        color: #dddddd !important;
        font-size: 15px !important;
        text-decoration: none !important;
        display: block !important;
        padding: 8px 0 !important;
        text-align: center !important;
    }

    #navFooter li {
        list-style: none !important;
    }

    /* Hide spacers that break the center alignment */
    .navFooterColSpacerInner, .navFooterDescSpacer {
        display: none !important;
    }

    /* Bottom Copyright Section */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        background-color: #131a22 !important;
        padding: 30px 10px !important;
        width: 100% !important;
        margin: 0 !important;
        text-align: center !important;
        border: none !important;
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
        color: #999999 !important;
        font-size: 12px !important;
        margin-top: 10px !important;
    }

    /* Description Items at the very bottom */
    .navFooterDescItem {
        width: 100% !important;
        margin-bottom: 20px !important;
        padding: 0 10px !important;
    }
}
</style>
"""

content = content.replace('</head>', v19_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 19 applied.")
