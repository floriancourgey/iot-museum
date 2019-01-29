var app;
(function(){
  if(!RMNGP_API_KEY || RMNGP_API_KEY.length < 1){
    alert('A Rmn-GP API key is required to use this functionnality.');
    return;
  }
  Vue.component('v-select', VueSelect.VueSelect);

  app = new Vue({
    delimiters: ['{[{', '}]}'],
    el: '#app',
    data: {
      paramsArtwork: {
        lang: 'fr',
        per_page: 15,
        page: 1,
        q: '',
        'facets[techniques]': '',
        'facets[periods]': '',
        'facets[collections]': 'Peintures',
      },
      artworksCount: 0,
      authorsCount: 0,
      loading: null,
      artworks: [],
      artworksSelected:{}, // {168:{},97:{}..}
      artworksSuccessfullyAdded:{},
      artworksNotAdded:{},
      collections: [
        {value: '', text: 'All'},
        {value: 'Dessins', text: 'Dessins (108k)'},
        {value: 'Photographies', text: 'Photographies (92k)'},
        {value: 'Estampes', text: 'Estampes (43k)'},
        {value: 'Objets d\'art', text: 'Objets d\'art (40k)'},
        {value: 'D.A.G.', text: 'D.A.G. (40k)'},
        {value: 'Peintures', text: 'Peintures (31k)'},
        {value: 'Arts de l\'Islam', text: 'Arts de l\'Islam (17k)'},
        {value: 'Arts de l\'Extrême-Orient', text: 'Arts de l\'Extrême-Orient (16k)'},
        {value: 'collection Rothschild', text: 'collection Rothschild (14k)'},
        {value: 'Sculptures', text: 'Sculptures (13k)'},
      ],
      techniques: [
        {value:'', text:'All'},
        {value:'dessin à la plume', text:'dessin à la plume (24k)'},
        {value:'mine de plomb', text:'mine de plomb (23k)'},
        {value:'huile sur toile', text:'huile sur toile (23k)'},
        {value:'dessin au crayon', text:'dessin au crayon (18k)'},
        {value:'aquarelle', text:'aquarelle (17k)'},
      ],
      periods: [
        {value:'', text:'All'},
        {value:'Europe (période) - période moderne', text:'Europe moderne 1492-1789 (60k)'},
        {value:'Europe (période) - période contemporaine 1789-1914', text:'Europe contemporaine 1789-1914 (159k)'},
        {value:'17e siècle', text:'17e (35k)'},
        {value:'18e siècle', text:'18e (45k)'},
        {value:'19e siècle', text:'19e (175k)'},
        {value:'20e siècle', text:'20e (125k)'},
      ],
      autocompleteAuthors: [],
      commonAuthors: [],
    },
    methods:{
      searchArtwork: function(){
        this.artworks = [];
        this.loading = true;
        axiosRmngp.get('https://api.art.rmngp.fr/v1/works', {
          params:_.omitBy(app.paramsArtwork, _.isEmpty)
        }).then(function(response){
          console.log(response.data);
          app.artworks = response.data['hits']['hits'];
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
          origin_id: a._id,
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
        if(artwork._source && artwork._source.title && artwork._source.title[lang]){
          return artwork._source.title[lang];
        }
        return '';
      },
      getAuthor: function(artwork, lang){
        if(artwork._source && artwork._source.authors.length > 0 && artwork._source.authors[0].name){
          return artwork._source.authors[0].name[lang];
        }
        return '';
      },
      getImage: function(artwork){
        if(artwork._source && artwork._source.images.length > 0){
          return artwork._source.images[0].urls.original;
        }
        return '';
      },
      getDate: function(artwork){
        if(artwork._source && artwork._source.date && artwork._source.date.display){
          return artwork._source.date.display;
        }
        return '';
      },
      refreshCounts: function(){
        axiosLocal.get(urlArtworksCount).then(function(response){
          app.artworksCount = response.data.count;});
        axiosLocal.get(urlArtworksAuthorsCount).then(function(response){
          app.authorsCount = response.data.count;});
      },
      onAuthorSearch: function(search, loading){
        if(search.length<3) return;
        console.log(search);
        loading(true);
        axiosRmngp.get('https://api.art.rmngp.fr/v1/authors', {params:{q:search}})
        .then(function(response){
          console.log(response.data);
          for(var hit of response.data.hits.hits){
            var name;
            try{name=hit._source.name.fr}catch(e){console.log('e',e);continue}
            // app.autocompleteAuthors.push({
            //   label: name,
            //   value: name,
            // });
            app.autocompleteAuthors.push(name);
          }
          loading(false);
        });
      },
      refreshCommonAuthors: function(){
        axiosLocal.get(urlCommonAuthors).then(function(response){app.commonAuthors = _.shuffle(response.data).slice(0, 20);});
      },
      selectCommonAuthor: function(author){
        app.paramsArtwork['facets[authors]'] = author.key;
        this.searchArtwork();
      },
    },
    mounted: function(){
      this.$nextTick(function () {
        this.searchArtwork();
        this.refreshCounts();
        this.refreshCommonAuthors();
      })
    },
  });
})();
