with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

responsive_css = """
<style>
/* Make the entire layout fluid for mobile devices */
body, html {
    overflow-x: hidden;
    width: 100%;
}

img {
    max-width: 100% !important;
    height: auto !important;
}

#a-page, .a-container, .a-row, .a-column {
    min-width: 0 !important;
    max-width: 100% !important;
}

/* Specific elements that often overflow on amazon */
#navbar, #nav-main, #nav-belt, .nav-sprite-v1 {
    min-width: 0 !important;
    width: 100% !important;
    overflow-x: auto;
}

table {
    max-width: 100% !important;
    width: 100% !important;
    table-layout: fixed;
    word-break: break-word;
}
</style>
"""

# add it right before </head>
if "/* Make the entire layout fluid" not in content:
    content = content.replace('</head>', responsive_css + '</head>', 1)
    with open('public/amazon.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added responsive CSS.")
else:
    print("Already added responsive CSS.")
