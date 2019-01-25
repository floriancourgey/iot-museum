<template>
  <main class="row text-center text-light">
    <div class="col">
      <div class="row">
        <div class="col-lg-2">

        </div>
        <div class="col-lg-8">
          <div :style="{'background-image':artwork.url}" id="img"></div>
        </div>
        <div class="col-lg-2 w3-display-container">
          <div class="w3-display-middle" style="width:100%">
            <h1>{{artwork.name}}&nbsp;</h1>
            <h2>{{artwork.author}}&nbsp;</h2>
          </div>
        </div>
      </div>
      <div class="row m-4">
        <div class="col">
          <div>
            <button @click="previous()" class="btn btn-light btn-sm">&lt;&lt;</button>
            <button @click="pause()" class="btn btn-light btn-sm">pause</button>
            <button @click="play()" class="btn btn-light btn-sm">play</button>
            <button @click="next()" class="btn btn-light btn-sm">&gt;&gt;</button>
          </div>
          <div class="my-2">
            <a id="adminLink" target="_blank">Edit in admin</a>
          </div>
          <div class="my-2">
            Change every
            <input type="number" class="p-0 px-1 d-inline-block form-control form-control-sm" style="width:55px" v-model.number="timeoutInterval">
            seconds
          </div>
          <div>
            Fetching among a total of {{numberOfArtworks}} artworks.
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data: function(){
    return {
      // urlNext: urlNext,
      timeoutId: null,
      timeoutInterval: 10,
      numberOfArtworks: null,
      artwork: {},
      artworksHistory: [],
    }
  },
  methods: {
    previous: function(){},
    pause: function(){},
    play: function(){},
    next: function(){
      console.log('next() called');
      /*$.get(self.urlNext, null, function(artwork){
        console.log(artwork);
        self.artwork = artwork;
        // setArtwork(self.artwork);
        self.artworkHistory.push(self.artwork);
      });*/
      clearTimeout(self.timeoutId);
      if(!this.timeoutInterval || this.timeoutInterval <= 0){
        this.timeoutInterval = 10;
      }
      console.log('next() using timeoutInterval='+self.timeoutInterval);
      self.timeoutId = setTimeout(function(){
        console.log('setTimeout() called');
        self.next();
      }, self.timeoutInterval*1000);
      console.log('next() timeoutId='+self.timeoutId);
    },
  }
}
</script>
