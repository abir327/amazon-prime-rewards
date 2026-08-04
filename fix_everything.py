import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject ueLogError silence at the start of <head>
content = content.replace('<head>', '<head>\\n<script>window.ueLogError = function() { return false; }; window.ue_err = { ec: 0 };</script>\\n', 1)

# 2. Add more robust layout fixes
# Replace my previous fix
content = re.sub(r'<style>\s*/\* SUPER RESPONSIVE OVERRIDES.*?</style>', '', content, flags=re.DOTALL)

better_responsive_css = """
<style>
/* SUPER RESPONSIVE OVERRIDES */
@media screen and (max-width: 900px) {
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        max-width: 100vw !important;
        margin: 0 !important;
        padding: 0 !important;
        position: relative !important;
    }

    * {
        max-width: 100vw !important;
        box-sizing: border-box !important;
    }

    /* Hide desktop nav */
    #nav-belt, #nav-main, #navbar, header, .nav-sprite-v1, #nav-tools {
        display: none !important;
    }

    /* Hide left sidebar */
    .apb-browse-left-nav,
    .apb-default-search-refinements-leftnav,
    #s-refinements,
    #leftCol,
    .nav-left {
        display: none !important;
        width: 0 !important;
        visibility: hidden !important;
    }

    /* Force main content container to take full width */
    #a-page, .a-container, #centerCol, #rightCol, .a-column, .a-span12, .apb-default-slot,
    .apb-browse-two-col-center-margin-right, .apb-browse-col-pad-right {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        float: none !important;
        margin: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        left: auto !important;
        right: auto !important;
        transform: none !important;
    }

    /* Fix grid layouts */
    div[class*="bxcGridColumn"], div[class*="bxcGridRow"], div[class*="bxcGridContainer"] {
        display: block !important;
        width: 100% !important;
        min-width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        position: static !important;
        left: auto !important;
        right: auto !important;
        transform: none !important;
        float: none !important;
    }
    
    /* Cancel out push/pull classes from Amazon grid */
    div[class*="Push"], div[class*="Pull"] {
        left: auto !important;
        right: auto !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Center text */
    .a-section {
        width: 100% !important;
    }

    /* Images */
    img, table, iframe, video {
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain;
    }
    
    table, thead, tbody, th, td, tr {
        display: block !important;
        max-width: 100% !important;
        min-width: 0 !important;
        width: 100% !important;
    }

    /* Hide spacer images on mobile */
    img[src*="SpacerTest"], img[alt*="white space"] {
        display: none !important;
    }

    /* Footer fixes */
    #navFooter, .navFooterLine, .navFooterColHead, .navFooterDescLine {
        white-space: normal !important;
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

print("Better responsive + ueLogError fix applied.")
