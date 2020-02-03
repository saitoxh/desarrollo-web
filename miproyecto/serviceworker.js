var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/img/logo2.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});



importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyDFG3JLVnL02evX6FK99rpMox9qg1Sqr3Y",
  authDomain: "enmibarrio-a79e9.firebaseapp.com",
  databaseURL: "https://enmibarrio-a79e9.firebaseio.com",
  projectId: "enmibarrio-a79e9",
  storageBucket: "enmibarrio-a79e9.appspot.com",
  messagingSenderId: "584865762623",
  appId: "1:584865762623:web:8259d9345e13f29280978a"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {

  let title = 'titulo de la notificacion';

  let options = {
    body:'este es el mesaje ',
    icon:'/static/img/logo2.png'
  }

  self.registration.showNotification(title, options);

  
})

