/* Copy-to-clipboard button for <pre><code> blocks */
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('pre > code').forEach(function (codeEl) {
        var pre = codeEl.parentElement;

        var btn = document.createElement('button');
        btn.className = 'copy-code-btn';
        btn.textContent = 'Copy';
        btn.setAttribute('aria-label', 'Copy code to clipboard');

        btn.addEventListener('click', function () {
            var text = codeEl.textContent;
            navigator.clipboard.writeText(text).then(function () {
                btn.textContent = 'Copied!';
                btn.classList.add('copied');
                setTimeout(function () {
                    btn.textContent = 'Copy';
                    btn.classList.remove('copied');
                }, 1500);
            });
        });

        pre.appendChild(btn);
    });
});
