import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will inject a script at the very end of <head> that locks ueLogError
script = """
<script>
Object.defineProperty(window, 'ueLogError', {
    value: function() { return false; },
    writable: false,
    configurable: false
});
</script>
"""
content = content.replace('<head>', '<head>\\n' + script, 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ueLogError locked.")
