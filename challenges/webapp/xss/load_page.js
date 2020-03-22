// Load libs
var system = require('system');
var webPage = require('webpage');
var TIMER_EXIT = 5000;

var page = webPage.create();
var url = 'https://xss.webchal.photon.rkevin.dev';

phantom.addCookie({
  name: "flag",
  value: "ECS{N0M_N0M_N0M_C5B1ABC976B9851714588981280B9F66}",
  domain: "xss.webchal.photon.rkevin.dev",
  secure: false,
  httponly: false,
  path: "/"
});

phantom.addCookie({
  name: "beamsplitter_xss",
  value: system.env["beamsplitter_cookie"],
  domain: "xss.webchal.photon.rkevin.dev",
  secure: false,
  httponly: true,
  path: "/"
});

phantom.addCookie({
  name: "message",
  value: "aHR0cHM6Ly93d3cubGFubWFzdGVyNTMuY29tL3N0YXRpYy9pbWFnZXMvcG9zdHMvY29va2llX21vbnN0ZXIuanBn",
  domain: "xss.webchal.photon.rkevin.dev",
  secure: false,
  httponly: false,
  path: "/"
});

page.open(url, function(status) {
  page.evaluate(function() {
    console.log(document.title);
  });
});

setTimeout(function(){phantom.exit()}, TIMER_EXIT);


//console.log(flag);
