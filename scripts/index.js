'use strict';

document.addEventListener("DOMContentLoaded", function(event) {
  adWarning();
});

// https://www.detectadblock.com/
function adWarning() {
  var e = document.getElementById('bwCfaGEgVWjq');
  if (e) {
    alert('This site works better with an ad blocker enabled. Please enable an ad blocker to continue');
    // check again
    adWarning();
  }
}
