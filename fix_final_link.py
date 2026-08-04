import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove ALL my injected styles to clean the slate
content = re.sub(r'<style>\s*/\* SUPER RESPONSIVE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<style>\s*/\* Safe mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<style>\s*/\* CLEAN MOBILE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

# 2. Replace the button link
old_url = r'<a href="https://app\.hawktrk\.com/click[^"]+" class="neon-btn">'
new_url = r'<a href="https://app.hawktrk.com/click?pid=2&amp;offer_id=22011&amp;sub2=u809325&amp;sub5=Abir" class="neon-btn">'
content = re.sub(old_url, new_url, content)

# 3. Add the minimal, perfect responsive CSS
better_responsive_css = """
<style>
/* CLEAN MOBILE OVERRIDES */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }

    /* Hide desktop nav */
    #navbar, header {
        display: none !important;
    }

    /* Custom mobile header */
    body::before {
        content: "Amazon";
        display: block;
        background: #232f3e;
        color: white;
        padding: 15px 20px;
        font-size: 22px;
        font-family: Arial, sans-serif;
        font-weight: bold;
        text-align: center;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Hide left sidebar */
    .apb-browse-left-nav,
    .apb-default-search-refinements-leftnav,
    #s-refinements,
    #leftCol {
        display: none !important;
        width: 0 !important;
        visibility: hidden !important;
    }

    /* Force main content container to take full width */
    #a-page, .a-container, #centerCol, #rightCol, .a-column, .a-span12, .apb-default-slot,
    .apb-browse-two-col-center-margin-right, .apb-browse-col-pad-right,
    div[class*="bxcGridContainer"] {
        width: 100% !important;
        max-width: 100vw !important;
        min-width: 0 !important;
        float: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Fix grid layouts */
    div[class*="bxcGridColumn"], div[class*="bxcGridRow"] {
        display: block !important;
        width: 100% !important;
        max-width: 100vw !important;
        min-width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        position: static !important;
        left: auto !important;
        right: auto !important;
        transform: none !important;
        float: none !important;
        clear: both !important;
    }
    
    /* Make text boxes use full width and wrap */
    div[class*="bxcGridText"] {
        width: 100% !important;
        white-space: normal !important;
        padding: 0 10px !important;
    }
    
    /* Center the neon button properly */
    .neon-btn-container {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        padding: 20px 0 !important;
    }
    
    /* Images */
    img, iframe, video {
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain;
    }
    
    /* Fix tables but don't break them globally */
    .apb-default-slot table, div[class*="bxcGridContainer"] table {
        display: block !important;
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: auto !important;
    }

    /* Hide spacer images on mobile */
    img[src*="SpacerTest"], img[alt*="white space"] {
        display: none !important;
    }

    /* Footer - FORCE IT TO BE VISIBLE AND WRAP PROPERLY */
    #navFooter {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    #navFooter, .navFooterLine, .navFooterColHead, .navFooterDescLine {
        white-space: normal !important;
        width: 100% !important;
        max-width: 100vw !important;
    }
    .navFooterVerticalColumn {
        display: block !important;
        width: 100% !important;
    }
    .navFooterCol {
        width: 100% !important;
        float: none !important;
        margin-bottom: 20px !important;
    }
    .navFooterLinkCol {
        width: 100% !important;
        margin-bottom: 20px !important;
    }
    
    /* Ensure the footer lists wrap as well */
    #navFooter ul {
        width: 100% !important;
        display: block !important;
    }
    #navFooter li {
        white-space: normal !important;
        word-wrap: break-word !important;
    }
}
/* Unconditionally hide tracking pixels */
img[width="1"][height="1"], img[width="0"][height="0"], img[width="1"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""

content = content.replace('</head>', better_responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix applied successfully.")
