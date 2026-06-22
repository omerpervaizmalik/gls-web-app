// Counter Animation - triggers when stat numbers scroll into view
(function () {
    function animateCounter(el) {
        var target = parseInt(el.getAttribute('data-target'), 10);
        var suffix = el.getAttribute('data-suffix') || '';
        var duration = 1800;
        var steps = 60;
        var stepValue = target / steps;
        var current = 0;
        var count = 0;
        el.textContent = '0' + suffix;
        var timer = setInterval(function () {
            count++;
            current = Math.min(Math.round(stepValue * count), target);
            el.textContent = current.toLocaleString() + suffix;
            if (current >= target) clearInterval(timer);
        }, duration / steps);
    }

    var hasAnimated = new WeakSet();

    var obs = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting && !hasAnimated.has(entry.target)) {
                hasAnimated.add(entry.target);
                animateCounter(entry.target);
                obs.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    function initCounters() {
        document.querySelectorAll('.stat-number[data-target]').forEach(function (el) {
            obs.observe(el);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCounters);
    } else {
        initCounters();
    }
})();
