with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

responsive_css = """
<style>
/* Aggressive mobile responsive overrides for Amazon desktop page */
html, body {
    width: 100% !important;
    max-width: 100vw !important;
    overflow-x: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Override all min-widths */
* {
    min-width: 0 !important;
    box-sizing: border-box !important;
}

/* Fix navbar */
#navbar, #nav-belt, #nav-main, .nav-fill, .nav-left, .nav-right, #nav-search, #nav-tools {
    display: flex !important;
    flex-wrap: wrap !important;
    width: 100% !important;
    max-width: 100% !important;
}

/* Ensure images scale */
img {
    max-width: 100% !important;
    height: auto !important;
    object-fit: contain !important;
}

/* Fix specific amazon container widths */
.a-container, .a-row, .a-column, .a-box, .a-box-inner, #a-page, .celwidget, .a-section, #dp-container, #dp, #centerCol, #rightCol, #leftCol {
    width: 100% !important;
    max-width: 100% !important;
    float: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 5px !important;
    padding-right: 5px !important;
}

/* Fix tables */
table, tr, td, tbody {
    max-width: 100% !important;
    width: auto !important;
    display: block !important;
}

/* Fix flex/grid issues */
.a-row {
    display: flex !important;
    flex-direction: column !important;
}
.a-span1, .a-span2, .a-span3, .a-span4, .a-span5, .a-span6, .a-span7, .a-span8, .a-span9, .a-span10, .a-span11, .a-span12 {
    width: 100% !important;
    float: none !important;
}

/* Hide some unnecessary desktop elements on mobile */
@media (max-width: 768px) {
    #nav-left-all-categories, .nav-right {
        display: none !important;
    }
}
</style>
"""

# Replace the previous responsive CSS
if "/* Make the entire layout fluid for mobile devices */" in content:
    import re
    # Remove old responsive css block
    content = re.sub(r'<style>\s*/\* Make the entire layout fluid.*?</style>', '', content, flags=re.DOTALL)
    
if "/* Aggressive mobile responsive overrides for Amazon desktop page */" not in content:
    content = content.replace('</head>', responsive_css + '</head>', 1)
    
with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Aggressive responsive CSS applied.")
