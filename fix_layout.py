import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's completely replace my old CSS
content = re.sub(r'<style>\s*/\* Safe mobile responsive overrides.*?</style>', '', content, flags=re.DOTALL)
content = re.sub(r'<meta[^>]*name=["\']viewport["\'][^>]*>', '', content)

viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
content = content.replace('</head>', viewport_meta + '\n</head>', 1)

responsive_css = """
<style>
/* Safe mobile responsive overrides for Amazon */
@media screen and (max-width: 768px) {
    html, body {
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
    }
    
    * {
        box-sizing: border-box !important;
    }

    #a-page, .a-container, .a-row, .a-popover-preload, div {
        max-width: 100vw !important;
    }

    /* Fix header */
    #navbar, #nav-main, #nav-belt, .nav-fill, .nav-right, #nav-tools, .nav-left, #nav-search {
        max-width: 100% !important;
        min-width: 0 !important;
    }
    
    header, #navbar {
        overflow-x: hidden !important;
        width: 100% !important;
    }

    /* HIDE LEFT NAV COMPLETELY ON MOBILE */
    .apb-browse-left-nav,
    .apb-default-search-refinements-leftnav,
    #s-refinements,
    #leftCol {
        display: none !important;
        width: 0 !important;
        visibility: hidden !important;
    }

    /* RIGHT CONTENT FULL WIDTH */
    .apb-browse-two-col-center-margin-right,
    #centerCol, #rightCol, .a-column, .a-span12, .apb-default-slot,
    .apb-browse-col-pad-right {
        width: 100% !important;
        max-width: 100% !important;
        float: none !important;
        margin: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }

    /* Force images and tables responsive */
    img, table, iframe, video {
        max-width: 100% !important;
        height: auto !important;
        object-fit: contain;
    }
    
    table, thead, tbody, th, td, tr {
        display: block !important;
        max-width: 100% !important;
        width: 100% !important;
    }

    /* Make grid rows stack */
    ._Y29ud_bxcGridRow_Zu5i8, ._Y29ud_bxcGridColumn_J5gfU {
        display: block !important;
        width: 100% !important;
        margin-left: 0 !important;
        padding-left: 0 !important;
    }
    
    ._Y29ud_bxcGridContainerWidth1500_36D4w {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* Footer fixes */
    .navFooterLine, .navFooterColHead, .navFooterDescLine {
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
    
    /* Neon button container */
    .neon-btn-container {
        width: 100% !important;
        max-width: 100% !important;
        overflow: hidden !important;
    }
}
img[width="1"][height="1"], img[width="0"][height="0"], img[width="1"] {
    display: none !important;
    position: absolute !important;
}
</style>
"""

content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Responsive applied.")
