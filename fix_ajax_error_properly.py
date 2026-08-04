import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Instead of stubbing the logger which didn't stop the error from happening,
# let's just intercept the fetch/XHR calls to that specific URL and return {}
# This is more robust since it works on both dev and preview without needing server config
mock_script = """
<script>
(function() {
    // Intercept XHR
    var originalOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url) {
        if (typeof url === 'string' && url.includes('/customer-preferences/api/flyout/xop-and-country')) {
            // Hijack this specific request
            this._mockedUrl = url;
            // Provide a dummy url that won't fail with a parser error if it's hit, or just let it fail silently
        }
        return originalOpen.apply(this, arguments);
    };
    
    var originalSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function() {
        if (this._mockedUrl) {
            // Mock a successful JSON response
            Object.defineProperty(this, 'response', {writable: true});
            Object.defineProperty(this, 'responseText', {writable: true});
            Object.defineProperty(this, 'status', {writable: true});
            Object.defineProperty(this, 'readyState', {writable: true});
            
            this.status = 200;
            this.readyState = 4;
            this.response = "{}";
            this.responseText = "{}";
            
            if (this.onreadystatechange) {
                this.onreadystatechange();
            }
            if (this.onload) {
                this.onload();
            }
            return;
        }
        return originalSend.apply(this, arguments);
    };
    
    // Intercept fetch just in case
    var originalFetch = window.fetch;
    window.fetch = function() {
        var url = arguments[0];
        if (typeof url === 'string' && url.includes('/customer-preferences/api/flyout/xop-and-country')) {
            return Promise.resolve(new Response('{}', {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }));
        }
        return originalFetch.apply(this, arguments);
    };
})();
</script>
"""

# Remove the old stub
content = re.sub(r'<script>window.ueLogError = function\(\) \{\};</script>\n?', '', content)

if 'XMLHttpRequest.prototype.open' not in content:
    content = content.replace('</head>', mock_script + '\n</head>', 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added robust AJAX mock.")
