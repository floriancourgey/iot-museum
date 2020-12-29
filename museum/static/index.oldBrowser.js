const app = {
  // data
  artworkHistory: [],
  timeoutId: null,
  timeoutAfterSuccess: 15, // in sec
  timeoutAfterError: 1, // in sec
  artwork: null, // json data from server
  // DOM
  img: jQuery('#img'),
  artwork_name: jQuery('#artwork_name'),
  artwork_author: jQuery('#artwork_author'),
  artwork_date_display: jQuery('#artwork_date_display'),
  // constructor
  init: function(){
    this.setImageHeight();
    this.next();
  },
  // main method
  next: function(){
    var self = this;
    debug('next() called');
    // if(this.isPaused){
    //   console.log('next() exit because app.isPaused');
    //   return;
    // }
    // artworkHistory.push(app.artwork);
    // clearTimeout(this.timeoutId);
    jQuery.get(urlNext)
      .success(function (data) {
        self.artwork = data;
        // when image is loaded
        self.img.error(function(e){
          self.removeAllListeners();
          debug('Image error, calling next');
          self.timeoutId = setTimeout(function(){
            self.timeoutId = null;
            self.next();
          }, self.timeoutAfterError*1000);
        })
        self.img.on('load', function() {
          self.removeAllListeners();
          debug('img loaded');
          // change text
          self.artwork_name.text(self.artwork.name);
          self.artwork_author.text(self.artwork.author);
          self.artwork_date_display.text(self.artwork.date_display);
          // and set timeout
          self.timeoutId = setTimeout(function(){
            self.timeoutId = null;
            self.next();
          }, self.timeoutAfterSuccess*1000);
          debug('setTimeout() called with id '+self.timeoutId);
        }).attr('src', self.artwork.url_online);
      })
      .error(function(){
        self.removeAllListeners();
        debug('API error, calling next');
        self.timeoutId = setTimeout(function(){
          self.timeoutId = null;
          self.next();
        }, self.timeoutAfterError*1000);
      });

    // if(this.timeoutInterval <= 0){
    //   this.timeoutInterval = 10;
    // }

    // console.log('next() timeoutId='+this.timeoutId);
  },
  // helpers
  setImageHeight: function (){
    var percent = 0.9;
    this.img.css('height', percent * window.innerHeight); // fix for old TV browsers
  },
  removeAllListeners: function (){
    console.log('Removing all listeners');
    this.img.off();
  }
}
