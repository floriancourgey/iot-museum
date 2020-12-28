var artworkHistory = [];

var timeoutId = null;
var timeoutInterval = 15; // in sec
var img = jQuery('#img');
img.css('height', window.innerHeight); // fix for old TV browsers

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
