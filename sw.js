const CACHE = 'clarinetcraft-v1';
const SAMPLES = ['D3','F3','As3','D4','F4','As4','D5','F5','As5','D6','Fs6'].flatMap(n => ['mp3','ogg'].map(e => './samples/clarinet/' + n + '.' + e));
const SHELL = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png', ...SAMPLES];

// Instala sem falhar se algum arquivo estiver ausente (cada um é guardado separadamente).
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.all(SHELL.map(u => c.add(u).catch(() => {}))))
      .then(() => self.skipWaiting())
  );
});
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});
// Rede primeiro; se estiver offline, usa o que já foi guardado (gravações do clarinete e biblioteca de partitura inclusas).
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res && (res.ok || res.type === 'opaque')) {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, copy)).catch(() => {});
      }
      return res;
    }).catch(() =>
      caches.match(e.request).then(r =>
        r || (e.request.mode === 'navigate' ? caches.match('./index.html') : Response.error())
      )
    )
  );
});
