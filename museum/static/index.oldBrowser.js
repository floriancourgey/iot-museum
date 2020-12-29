var artworkHistory = [];

// data
var timeoutId = null;
var timeoutAfterSuccess = 15; // in sec
var timeoutAfterError = 1; // in sec
var artwork = null; // json data from server
// DOM
var img = jQuery('#img');
img.css('height', 0.9 * window.innerHeight); // fix for old TV browsers
var artwork_name = jQuery('#artwork_name');
var artwork_author = jQuery('#artwork_author');
var artwork_date_display = jQuery('#artwork_date_display');

function removeAllListeners(elem){
  console.log('Removing all listeners from '+elem);
  elem.off();
}

function next(){
  debug('next() called');
  // if(this.isPaused){
  //   console.log('next() exit because app.isPaused');
  //   return;
  // }
  // artworkHistory.push(app.artwork);
  // clearTimeout(this.timeoutId);
  jQuery.get(urlNext)
    .success(function (data) {
      artwork = data;
      // when image is loaded
      img.error(function(e){
        removeAllListeners(img);
        debug('Image error, calling next');
        timeoutId = setTimeout(function(){
          timeoutId = null;
          next();
        }, timeoutAfterError*1000);
      })
      img.on('load', function() {
        removeAllListeners(img);
        debug('img loaded');
        // change text
        artwork_name.text(artwork.name+' ');
        artwork_author.text(artwork.author+' ');
        artwork_date_display.text(artwork.date_display);
        // and set timeout
        timeoutId = setTimeout(function(){
          timeoutId = null;
          next();
        }, timeoutAfterSuccess*1000);
        debug('setTimeout() called with id '+timeoutId);
      }).attr('src', artwork.url_online);
    })
    .error(function(){
      removeAllListeners(img);
      debug('API error, calling next');
      timeoutId = setTimeout(function(){
        timeoutId = null;
        next();
      }, timeoutAfterError*1000);
    });

  // if(this.timeoutInterval <= 0){
  //   this.timeoutInterval = 10;
  // }

  // console.log('next() timeoutId='+this.timeoutId);
}

next();
