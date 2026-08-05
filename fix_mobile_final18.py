import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up ALL previous injected mobile styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Surgical Mobile Fix (v18) - Deep Footer Fix
surgical_css = """
<style>
/* CLEAN MOBILE OVERRIDES v18 */
@media screen and (max-width: 900px) {
    /* Basic Document Reset */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        height: auto !important;
        min-height: 100vh !important;
    }

    /* Force all major containers to be full width */
    #a-page, .a-container, .a-row, .a-section, #navbar, #nav-belt, #nav-main {
        width: 100% !important;
        max-width: 100vw !important;
        float: none !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        padding-left: 5px !important;
        padding-right: 5px !important;
        box-sizing: border-box !important;
        display: block !important;
        position: relative !important;
    }

    /* Stack the header rows */
    #nav-belt, #nav-main {
        display: block !important;
        height: auto !important;
        background-color: #232f3e !important;
    }

    /* Ensure images don't break the layout */
    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* --- FOOTER FIX (v18 Deep Fix) --- */
    #navFooter {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        width: 100% !important;
        background-color: #232f3e !important;
        padding: 40px 0 !important;
        margin: 20px 0 0 0 !important;
        text-align: center !important;
        position: relative !important;
        clear: both !important;
        float: none !important;
        z-index: 10 !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        margin-bottom: 30px !important;
        padding: 0 20px !important;
        box-sizing: border-box !important;
    }

    .navFooterColHead {
        display: block !important;
        font-size: 16px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        color: #fff !important;
        text-align: center !important;
    }

    #navFooter ul {
        padding: 0 !important;
        margin: 0 !important;
        list-style: none !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }

    #navFooter li {
        margin-bottom: 12px !important;
        width: 100% !important;
        text-align: center !important;
    }

    #navFooter a {
        color: #ddd !important;
        font-size: 14px !important;
        text-decoration: none !important;
        display: block !important;
        padding: 5px 0 !important;
    }

    /* Bottom Copyright/Legal Section */
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
        color: #888 !important;
    }
    
    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 15px !important;
        padding: 0 !important;
        margin: 0 0 15px 0 !important;
        width: 100% !important;
    }

    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        font-size: 12px !important;
        margin-top: 10px !important;
        text-align: center !important;
    }
    
    .navFooterDescItem {
        width: 100% !important;
        text-align: center !important;
        margin-bottom: 20px !important;
        padding: 0 10px !important;
    }
}
</style>
"""

# Inject before closing head
if '</head>' in content:
    content = content.replace('</head>', surgical_css + '</head>', 1)
else:
    content = content.replace('<body', surgical_css + '<body', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile fix 18 (Deep Footer) applied.")
