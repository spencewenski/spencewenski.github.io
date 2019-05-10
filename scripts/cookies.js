'use strict';

document.addEventListener("DOMContentLoaded", function(event) {
  cookies();
});

const COOKIE_ACCEPTED_NAME = "CookieAccepted";
const ONE_YEAR_SECONDS = 60*60*24*365;

function cookies() {
  if (!checkAccepted()) {
    showMessage();
  } else {
    cookieAccepted();
  }
}

function showMessage() {
  document.getElementById("cookie-message").style.display = 'block';
}

function checkAccepted() {
  return getCookie(COOKIE_ACCEPTED_NAME) === 'true';
}

function cookieAccepted() {
  document.getElementById("cookie-message").style.display = 'none';
  document.cookie = COOKIE_ACCEPTED_NAME + "=true;path=/;samesite=strict;max-age=" + ONE_YEAR_SECONDS;
}

// https://stackoverflow.com/questions/14573223/set-cookie-and-get-cookie-with-javascript
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
