import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add an XHR interceptor
xhr_intercept = """
<script>
(function() {
    var originalXHR = window.XMLHttpRequest;
    function MockXHR() {
        var xhr = new originalXHR();
        var originalOpen = xhr.open;
        var originalSend = xhr.send;
        
        xhr.open = function(method, url) {
            this._url = url;
            return originalOpen.apply(this, arguments);
        };
        
        xhr.send = function(data) {
            var isMenu = this._url && (this._url.indexOf('hMenu') > -1 || this._url.indexOf('menu') > -1 || this._url.indexOf('ajax') > -1 || this._url.indexOf('flyout') > -1);
            if (isMenu || (data && typeof data === 'string' && data.indexOf('hMenuDesktopFirstLayer') > -1)) {
                console.log("Intercepted AJAX request to:", this._url);
                // Return dummy HTML response
                Object.defineProperty(this, 'readyState', { value: 4, writable: false });
                Object.defineProperty(this, 'status', { value: 200, writable: false });
                Object.defineProperty(this, 'responseText', { value: '<div></div>', writable: false });
                Object.defineProperty(this, 'response', { value: '<div></div>', writable: false });
                
                if (typeof this.onreadystatechange === 'function') {
                    this.onreadystatechange();
                }
                if (typeof this.onload === 'function') {
                    this.onload();
                }
                return;
            }
            return originalSend.apply(this, arguments);
        };
        
        return xhr;
    }
    window.XMLHttpRequest = MockXHR;
})();
</script>
"""

content = content.replace('<head>', '<head>\\n' + xhr_intercept, 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("AJAX intercepted.")
