var artworkHistory = [];

var timeoutId = null;
var timeoutInterval = 15; // in sec
var img = jQuery('#img');
img.css('height', window.innerHeight); // fix for old TV browsers
var artwork_name = jQuery('#artwork_name');
var artwork_author = jQuery('#artwork_author');

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
      debug('data');
      debug(data);
      debug('json');
      debug(JSON.stringify(data));
      img.attr('src', data.url_online);
      artwork_name.text(data.name+' ');
      artwork_author.text(data.author+' ');
      artwork_date_display.text(data.date_display);
    });

  // if(this.timeoutInterval <= 0){
  //   this.timeoutInterval = 10;
  // }
  timeoutId = setTimeout(function(){
    debug('setTimeout() called');
    next();
  }, timeoutInterval*1000);
  // console.log('next() timeoutId='+this.timeoutId);
}

next();
