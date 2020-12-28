var artworkHistory = [];

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
      jQuery('#img').css('background-image', 'url(' + data.url_online + ')');
    });

  // if(this.timeoutInterval <= 0){
  //   this.timeoutInterval = 10;
  // }
  // this.timeoutId = setTimeout(function(){
  //   console.log('setTimeout() called');
  //   app.next();
  // }, this.timeoutInterval*1000);
  // console.log('next() timeoutId='+this.timeoutId);
}

next();
