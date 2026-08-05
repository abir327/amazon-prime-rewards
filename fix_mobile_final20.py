import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up previous injected mobile styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add v20 CSS - Hyper-aggressive Footer Visibility + 3-Dot Icon
v20_css = """
<style>
/* CLEAN MOBILE OVERRIDES v20 */
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
        position: relative !important;
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
        padding: 10px 50px 10px 15px !important;
    }

    /* Vertical Ellipsis (3 dots) in header */
    #nav-belt::after {
        content: "\\22EE" !important; 
        color: #ffffff !important;
        font-size: 32px !important;
        position: absolute !important;
        right: 15px !important;
        top: 8px !important;
        font-weight: bold !important;
        z-index: 10005 !important;
    }

    /* --- FOOTER: HYPER-AGGRESSIVE VISIBILITY --- */
    #navFooter {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        background-color: #232f3e !important;
        width: 100% !important;
        padding: 50px 10px !important;
        margin: 20px 0 0 0 !important;
        clear: both !important;
        text-align: center !important;
        z-index: 9999 !important;
        position: relative !important;
    }

    /* Force all text items to be white and centered */
    #navFooter .navFooterColHead, #navFooter a, #navFooter li, #navFooter span, #navFooter h5 {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        color: #ffffff !important;
        width: 100% !important;
        text-align: center !important;
        float: none !important;
        background: transparent !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    .navFooterVerticalColumn, .navFooterVerticalRow, .navFooterLinkCol {
        display: block !important;
        width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .navFooterLinkCol {
        margin-bottom: 40px !important;
    }

    .navFooterColHead {
        font-size: 18px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        text-transform: uppercase !important;
    }

    #navFooter ul {
        display: block !important;
        padding: 0 !important;
        margin: 0 !important;
        list-style: none !important;
    }

    #navFooter li {
        margin-bottom: 12px !important;
    }

    #navFooter a {
        color: #cccccc !important;
        font-size: 16px !important;
        padding: 10px 0 !important;
        text-decoration: none !important;
    }

    /* Hide spacers */
    .navFooterColSpacerInner, .navFooterDescSpacer {
        display: none !important;
    }

    /* Bottom Copyright Bar */
    .navFooterLine, .navFooterCopyright, .navFooterDescLine {
        display: block !important;
        background-color: #131a22 !important;
        padding: 30px 10px !important;
        width: 100% !important;
        margin: 0 !important;
        border: none !important;
    }

    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 15px !important;
        margin-bottom: 15px !important;
    }

    .navFooterLine li, .navFooterCopyright li {
        display: inline-block !important;
        width: auto !important;
    }

    .navFooterCopyright span {
        display: block !important;
        color: #777777 !important;
        font-size: 13px !important;
        margin-top: 15px !important;
    }
}
</style>
"""

content = content.replace('</head>', v20_css + '</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 20 applied.")
