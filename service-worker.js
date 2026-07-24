const ARIANE_CACHE_V501 = 'ariane-v5-07-pwa-cache';
const ARIANE_ASSETS_V501 = [
  './',
  './index.html?v=507',
  './manifest.webmanifest?v=507',
  './icons/icon-192.png?v=507',
  './icons/icon-512.png?v=507',
  './icons/icon-maskable-512.png?v=507',
  './icons/apple-touch-icon.png?v=507'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(ARIANE_CACHE_V501)
      .then(cache => cache.addAll(ARIANE_ASSETS_V501))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys
        .filter(key => !key.includes('ariane-v5-07'))
        .map(key => caches.delete(key))
    )).then(() => self.clients.claim())
  );
});

// Strategie : reseau en priorite pour TOUT, avec repli sur le cache
// seulement si le reseau echoue (hors-ligne). Ca evite qu'une ancienne
// version reste affichee apres une mise a jour du fichier Ariane.
self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  if (url.origin !== location.origin) {
    event.respondWith(fetch(request).catch(() => caches.match(request)));
    return;
  }

  event.respondWith(
    fetch(request, { cache: 'no-store' }).then(response => {
      const copy = response.clone();
      caches.open(ARIANE_CACHE_V501).then(cache => cache.put(request, copy));
      return response;
    }).catch(() =>
      caches.match(request).then(cached => cached || caches.match('./index.html?v=507'))
    )
  );
});
