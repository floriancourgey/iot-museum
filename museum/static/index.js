// if of the tiemout process (to be stopped when Pause)
var timeoutId = null;
// array of displayed artwork
var artworkHistory = [];
// jquery objects
var $img = null;
var $name = null;
var $author = null;
var $timeoutInterval = null;
var $pause = null;
var $play = null;
// functions
function previous(){
  pause();
  if(artworkHistory.length < 1){
    return;
  }
  artwork = artworkHistory.pop();
  setArtwork(artwork);
}
function pause(){
  $pause.hide();
  $play.show();
  clearTimeout(timeoutId);
}
function play(){
  $play.hide();
  $pause.show();
  next();
}
function next(){
  console.log('next() called');
  $.get(urlNext, null, function(artwork){
    console.log(artwork);
    setArtwork(artwork);
    artworkHistory.push(artwork);
  });
  clearTimeout(timeoutId);
  timeoutInterval = parseInt($timeoutInterval.val());
  if(timeoutInterval <= 0){
    timeoutInterval = 10;
  }
  console.log('next() using timeoutInterval='+timeoutInterval);
  timeoutId = setTimeout(function(){
    console.log('setTimeout() called');
    next();
  }, timeoutInterval*1000);
  console.log('next() timeoutId='+timeoutId);
}
function setArtwork(a) {
  $img.attr('src', a.url);
  $name.html(a.name);
  $author.html(a.author);
}
$(function(){
  $img = $('#img');
  $name = $('#name');
  $author = $('#author');
  $timeoutInterval = $('#timeoutInterval');
  $pause = $('#pause');
  $play = $('#play');
  play();
});
