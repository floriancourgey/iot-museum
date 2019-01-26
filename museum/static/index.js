var app = new Vue({
  el: '#app',
  data: {
    isPaused: false,
    artwork: {},
    timeoutId: null, // if of the tiemout process (to be stopped when Pause)
    artworkHistory: [], // array of displayed artwork
    timeoutInterval: 10,
  },
  methods:{
    previous: function(){
      this.pause();
      if(this.artworkHistory.length < 1){
        return;
      }
      this.artwork = this.artworkHistory.pop();
    },
    pause: function(){
      this.isPaused = true;
      clearTimeout(self.timeoutId);
    },
    play: function(){
      this.isPaused = false;
      this.next();
    },
    next: function(){
      console.log('next() called');
      axios.get(urlNext)
        .then(function (response) {
          app.artwork = response.data;
          app.artworkHistory.push(app.artwork);
        });
      clearTimeout(this.timeoutId);
      if(this.isPaused){
        return;
      }
      if(this.timeoutInterval <= 0){
        this.timeoutInterval = 10;
      }
      this.timeoutId = setTimeout(function(){
        console.log('setTimeout() called');
        app.next();
      }, this.timeoutInterval*1000);
      console.log('next() timeoutId='+this.timeoutId);
    },
    getArtworkUrl: function(){
      if(!this.artwork){
        return null;
      }
      if(this.artwork.url_online && this.artwork.url_online.length>0){
        return this.artwork.url_online;
      }
      if(this.artwork.url_local && this.artwork.url_local.length>0){
        return MEDIA_URL+this.artwork.url_local;
      }
      return null;
    },
  },
  mounted: function () {
    this.$nextTick(function () {
      app.next();
    })
  }
})
