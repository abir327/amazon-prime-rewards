import re

with open('public/amazon.html', 'r', encoding='utf-8') as f:
    content = f.read()

fetch_intercept = """
<script>
(function() {
    var originalFetch = window.fetch;
    window.fetch = function(url, options) {
        var urlStr = typeof url === 'string' ? url : (url ? url.url : '');
        var dataStr = (options && options.body && typeof options.body === 'string') ? options.body : '';
        var isMenu = urlStr.indexOf('hMenu') > -1 || urlStr.indexOf('menu') > -1 || urlStr.indexOf('ajax') > -1 || urlStr.indexOf('flyout') > -1;
        
        if (isMenu || dataStr.indexOf('hMenuDesktopFirstLayer') > -1) {
            console.log("Intercepted Fetch request to:", urlStr);
            return Promise.resolve(new Response('<div></div>', {
                status: 200,
                headers: { 'Content-Type': 'text/html' }
            }));
        }
        return originalFetch.apply(this, arguments);
    };
})();
</script>
"""

content = content.replace('<head>', '<head>\n' + fetch_intercept, 1)

with open('public/amazon.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fetch intercepted.")
