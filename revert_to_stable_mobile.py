import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Aggressively remove ALL previous injected mobile override styles
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Re-apply the surgical v16 style which was the "last known good" for the header
# and refined for the footer as requested.
stable_css = """
<style>
/* CLEAN MOBILE OVERRIDES v16_RESTORED */
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
        background-color: #232f3e !important;
    }

    /* Ensure images don't break the layout */
    img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* --- FOOTER FIX --- */
    #navFooter {
        display: block !important;
        background-color: #232f3e !important;
        padding: 40px 10px !important;
        margin-top: 20px !important;
        text-align: center !important;
    }
    
    .navFooterVerticalColumn, .navFooterCol, .navFooterLinkCol {
        width: 100% !important;
        float: none !important;
        display: block !important;
        margin-bottom: 25px !important;
        text-align: center !important;
    }

    .navFooterColHead {
        color: #fff !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
        display: block !important;
    }

    #navFooter ul {
        padding: 0 !important;
        list-style: none !important;
        margin: 0 !important;
    }

    #navFooter li {
        margin-bottom: 8px !important;
    }

    #navFooter a {
        color: #ccc !important;
        text-decoration: none !important;
        font-size: 14px !important;
    }

    /* Bottom Line Alignment */
    .navFooterCopyright, .navFooterLine, .navFooterDescLine {
        display: block !important;
        text-align: center !important;
        padding: 25px 10px !important;
        background-color: #131a22 !important;
        border: none !important;
    }
    
    .navFooterLine ul, .navFooterCopyright ul {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 12px !important;
        padding: 0 !important;
    }
    
    .navFooterCopyright span {
        display: block !important;
        color: #888 !important;
        margin-top: 10px !important;
    }
}
</style>
"""

# Inject before closing head
if '</head>' in content:
    content = content.replace('</head>', stable_css + '</head>', 1)
else:
    content = content.replace('<body', stable_css + '<body', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored stable mobile styles.")
