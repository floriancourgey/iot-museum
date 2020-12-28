var artworkHistory = [];

var timeoutId = null;
var timeoutInterval = 15; // in sec
var img = jQuery('#img');
img.css('height', window.innerHeight - 100); // fix for old TV browsers
var artwork_name = jQuery('#artwork_name');
var artwork_author = jQuery('#artwork_author');
var artwork_date_display = jQuery('#artwork_date_display');

function next(){
  debug('next() called');
  if(timeoutId){
    debug('timeout not null, exit');
    return;
  }
  // if(this.isPaused){
  //   console.log('next() exit because app.isPaused');
  //   return;
  // }
  // artworkHistory.push(app.artwork);
  // clearTimeout(this.timeoutId);
  jQuery.get(urlNext)
    .success(function (data) {
      debug('data');
      debug(data);
      debug('json');
      debug(JSON.stringify(data));
      // when image is loaded
      img.on('load', function() {
        img.off(); // remove timeout
        debug('img loaded');
        // change text
        artwork_name.text(data.name+' ');
        artwork_author.text(data.author+' ');
        artwork_date_display.text(data.date_display);
        // and set timeout
        clearTimeout(timeoutId);
        timeoutId = setTimeout(function(){
          clearTimeout(timeoutId);
          timeoutId = null;
          next();
        }, timeoutInterval*1000);
        debug('setTimeout() called with id '+timeoutId);
      }).attr('src', data.url_online);
    })
    .error(function(){
      debug('error, calling next');
      next();
    });

  // if(this.timeoutInterval <= 0){
  //   this.timeoutInterval = 10;
  // }

  // console.log('next() timeoutId='+this.timeoutId);
}

next();
