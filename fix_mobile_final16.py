import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up ALL previous injected mobile styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Add the Surgical Mobile Fix (v16)
# This version focuses on structural width and stacking ONLY.
surgical_css = """
<style>
/* CLEAN MOBILE OVERRIDES v16 */
@media screen and (max-width: 900px) {
    /* Basic Document Reset */
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Force all major containers to be full width */
    #a-page, .a-container, .a-row, .a-section, #navbar, #nav-belt, #nav-main, #nav-footer {
        width: 100% !important;
        max-width: 100vw !important;
        float: none !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        padding-left: 5px !important;
        padding-right: 5px !important;
        box-sizing: border-box !important;
    }

    /* Stack the header rows */
    #nav-belt, #nav-main {
        display: block !important;
        height: auto !important;
    }

    /* Ensure images don't break the layout */
    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* --- FOOTER FIX --- */
    #navFooter {
        padding: 40px 10px !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        float: none !important;
        display: block !important;
        margin-bottom: 20px !important;
        text-align: center !important;
    }

    #navFooter ul {
        padding: 0 !important;
        list-style: none !important;
    }

    /* Bottom Line Alignment */
    .navFooterCopyright, .navFooterLine {
        display: block !important;
        text-align: center !important;
        padding: 20px 0 !important;
    }
    
    .navFooterLine ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 10px !important;
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

print("Mobile fix 16 (Surgical) applied.")
