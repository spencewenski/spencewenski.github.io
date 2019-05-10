'use strict';

document.addEventListener("DOMContentLoaded", function(event) {
  loading();
});

const INITIAL_DELAY_MS = 100;
const DELAY_INCREASE_AMOUNT_MS = 75;
const FINALIZE_DELAY_MS = 1000 * 20;  // 20 seconds
const ERROR_DELAY_MS = 1000 * 60 * 3; // 3 minutes

const ACTUAL_MAX = 0.99;
const EMPTY_PROGRESS_BAR = "<progress id='progress-bar'></progress>";
const PROGRESS_BAR_ID = 'progress-bar';
const CLEVER_STRING_ID = 'clever-string';
const PERCENT_STRING_ID = 'percent';

function loading() {
  increment(INITIAL_DELAY_MS);
}

function increment(delay) {
  setTimeout(function() {
    var progressBar = document.getElementById(PROGRESS_BAR_ID);
    var value = progressBar.value + ((ACTUAL_MAX - progressBar.value) * randomRange(0.08, 0.12));
    if (ACTUAL_MAX - value > 0.001) {
      setPercent(value);
      increment(delay + DELAY_INCREASE_AMOUNT_MS);
    } else {
      setPercent(ACTUAL_MAX);
      finalize();
    }
  }, delay);
}

function finalize() {
  setTimeout(function() {
    var cleverString = document.getElementById(CLEVER_STRING_ID);
    cleverString.innerHTML = 'Finalizing';
    var progressBar = document.getElementById(PROGRESS_BAR_ID);
    progressBar.outerHTML = EMPTY_PROGRESS_BAR;
    error();
  }, FINALIZE_DELAY_MS)
}

function error() {
  setTimeout(function() {
    alert('It appears the website is unresponsive. Please try again later.');
  }, ERROR_DELAY_MS);
}

function setPercent(percent) {
  var progressBar = document.getElementById(PROGRESS_BAR_ID);
  progressBar.value = percent;
  var percentText = document.getElementById(PERCENT_STRING_ID);
  percentText.innerHTML = (percent * 100).toFixed(1);
}

function randomRange(min, max) {
  return Math.random() * (max - min) + min;
}
