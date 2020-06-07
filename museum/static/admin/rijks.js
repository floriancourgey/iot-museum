var app;
(function(){
  if(!RIJKS_API_KEY || RIJKS_API_KEY.length < 1){
    alert('A Rijks Museum API key is required to use this functionnality.');
    return;
  }
  Vue.component('v-select', VueSelect.VueSelect);

  app = new Vue({
    delimiters: ['{[{', '}]}'],
    el: '#app',
    data: {
      locale: 'en', // nl|en
      paramsArtwork: {
        q: '',
        key: RIJKS_API_KEY,
        format: 'json',
        p: 0, // page
        ps: 20, // results per page
        imgonly: true,
      },
      maxArtworksCountForQuery: 0,
      artworksCount: 0,
      authorsCount: 0,
      loading: null,
      artworks: [],
      artworksSelected:{}, // {168:{},97:{}..}
      artworksSuccessfullyAdded:{},
      artworksNotAdded:{},
    },
    methods:{
      searchArtwork: function(){
        this.artworks = [];
        this.loading = true;
        axiosRijks.get('https://www.rijksmuseum.nl/api/'+this.locale+'/collection', {
          // params: _.omitBy(app.paramsArtwork, _.isEmpty)
          params: app.paramsArtwork,
        }).then(function(response){
          console.log(response.data);
          app.artworks = response.data['artObjects'];
          app.maxArtworksCountForQuery = response.data['count'];
          app.loading = false;
        });
      },
      switchSelectedArtwork: function(a){
        if(a._id in this.artworksSelected){
          Vue.delete(this.artworksSelected, a._id);
        } else {
          Vue.set(this.artworksSelected, a._id, a);
        }
      },
      addToDb: function(){
        if(!this.artworksSelected || Object.keys(this.artworksSelected).length<1){
          return;
        }
        app.artworksSuccessfullyAdded = [];
        app.artworksNotAdded = [];
        this.processArtworkToAddToDb();
      },
      processArtworkToAddToDb: function(){
        if(!this.artworksSelected || Object.keys(this.artworksSelected).length<1){
          app.refreshCounts();
          var text = '';
          if(app.artworksSuccessfullyAdded.length){
            text += 'The following artworks have been successfully added:\n';
            for(var a of app.artworksSuccessfullyAdded){
              text += '- '+app.getTitle(a, 'fr')+'\n';
            }
          }
          if(app.artworksNotAdded.length){
            text += '\nThe following artworks could not be added:\n';
            for(var a of app.artworksNotAdded){
              text += '- '+app.getTitle(a, 'fr')+'\n';
            }
          }
          alert(text);
          return;
        }

        var firstKey = Object.keys(this.artworksSelected)[0];
        var a = this.artworksSelected[firstKey];
        Vue.delete(app.artworksSelected, firstKey);

        var data = {
          author:app.getAuthor(a, 'fr'),
          name:app.getTitle(a, 'fr'),
          origin:'rmngp',
          url:app.getImage(a),
          origin_artwork_id: a._id,
        };
        console.log('Sending artwork', data);
        axiosLocal.post('/api/artworks/', data)
          .then(function(response){
            app.artworksSuccessfullyAdded.push(a);
          })
          .catch(function (error) {
            console.log(error);
            app.artworksNotAdded.push(a);
          })
          .then(function(){
            app.processArtworkToAddToDb();
          })
        ;
      },
      getTitle: function(artwork, lang){
        return artwork.title;
      },
      getAuthor: function(artwork, lang){
        return artwork.principalOrFirstMaker;
      },
      getImage: function(artwork){
        if(artwork.hasImage && artwork.webImage.url){
          return artwork.webImage.url;
        }
        return '';
      },
      getDate: function(artwork){
        if(artwork._source && artwork._source.date && artwork._source.date.display){
          return artwork._source.date.display;
        }
        return '';
      },
    }
  });
})();
