var staticCacheName = 'hangarin-cache-v1';

self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(staticCacheName).then(function(cache) {
            return cache.addAll([
                '/',
                '/static/assets/css/bootstrap.min.css',
                '/static/assets/css/ready.css',
                '/static/assets/js/ready.min.js'
            ]);
        })
    );
});

self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});