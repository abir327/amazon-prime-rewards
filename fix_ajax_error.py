import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a stub for ueLogError so it doesn't complain in the console
stub = "<script>window.ueLogError = function() {};</script>"
if "window.ueLogError = function" not in content:
    content = content.replace('</head>', stub + '\n</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added ueLogError stub.")
