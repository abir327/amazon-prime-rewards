import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

json_patch = """
<script>
(function() {
    var originalParse = JSON.parse;
    JSON.parse = function(text, reviver) {
        try {
            return originalParse(text, reviver);
        } catch (e) {
            console.warn("JSON.parse error caught:", e, "Input was:", text ? text.substring(0, 100) : text);
            return {};
        }
    };
})();
</script>
"""

# Insert right after <head> to be safe
content = content.replace('<head>', '<head>\\n' + json_patch, 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("JSON.parse patched.")
