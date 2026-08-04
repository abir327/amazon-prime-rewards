import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the bad XHR mock
content = re.sub(r'<script>\s*\(function\(\) \{\s*var originalXHR = window.XMLHttpRequest;.*?window.XMLHttpRequest = MockXHR;\s*\}\)\(\);\s*</script>', '', content, flags=re.DOTALL)

# Add the prototype mock
xhr_proto_intercept = """
<script>
(function() {
    var originalOpen = XMLHttpRequest.prototype.open;
    var originalSend = XMLHttpRequest.prototype.send;
    
    XMLHttpRequest.prototype.open = function(method, url) {
        this._url = url;
        return originalOpen.apply(this, arguments);
    };
    
    XMLHttpRequest.prototype.send = function(data) {
        var isMenu = this._url && (typeof this._url === 'string') && (this._url.indexOf('hMenu') > -1 || this._url.indexOf('menu') > -1 || this._url.indexOf('ajax') > -1 || this._url.indexOf('flyout') > -1);
        if (isMenu || (data && typeof data === 'string' && data.indexOf('hMenuDesktopFirstLayer') > -1)) {
            console.log("Intercepted AJAX via proto to:", this._url);
            
            var self = this;
            setTimeout(function() {
                try { Object.defineProperty(self, 'readyState', { value: 4, configurable: true }); } catch(e) { self.readyState = 4; }
                try { Object.defineProperty(self, 'status', { value: 200, configurable: true }); } catch(e) { self.status = 200; }
                try { Object.defineProperty(self, 'responseText', { value: '<div></div>', configurable: true }); } catch(e) { self.responseText = '<div></div>'; }
                try { Object.defineProperty(self, 'response', { value: '<div></div>', configurable: true }); } catch(e) { self.response = '<div></div>'; }
                
                if (typeof self.onreadystatechange === 'function') {
                    self.onreadystatechange();
                }
                if (typeof self.onload === 'function') {
                    self.onload();
                }
            }, 50);
            return;
        }
        return originalSend.apply(this, arguments);
    };
})();
</script>
"""

content = content.replace('<head>', '<head>\n' + xhr_proto_intercept, 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("XHR proto intercepted.")
