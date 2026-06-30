var staticCacheName = `cata-log-pwa-v${Date().now()}`;

// list all static files to be cached in the pwa
var filesToCache = [
  // icons
  "/static/favicon.svg",
  "/static/favicon.ico",
  "/static/favicon-96x96.png",
  "/static/web-app-manifest-192x192.png",
  "/static/web-app-manifest-512x512.png",
  "/static/apple-touch-icon.png",
  // js
  "/static/js/theme-switcher.js",
  "/static/js/catalog-viewer.js",
  "/static/js/provider-form.js",
  "/static/js/provider-actions.js",
];

// Cache on install
self.addEventListener("install", (event) => {
  this.skipWaiting();
  event.waitUntil(
    caches.open(staticCacheName).then((cache) => {
      return cache.addAll(filesToCache);
    }),
  );
});

// Clear cache on activate
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((cacheName) => cacheName.startsWith("cata-log-pwa-"))
          .filter((cacheName) => cacheName !== staticCacheName)
          .map((cacheName) => caches.delete(cacheName)),
      );
    }),
  );
});

// Serve from Cache
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    }),
  );
});
