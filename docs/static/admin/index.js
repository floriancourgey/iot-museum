function objectToHttpQuery(o){
  return Object.keys(o)
    .filter(function(k){return o[k] && o[k].toString().length > 0; })
    .map(function(k){return k + '=' + o[k] })
    .join('&').replace(' ', '%20');
}
var app = new Vue({
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
    paramsAuthor: {
      q: 'van gogh',
    },
    artworks: [],
    authors: [],
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
  },
  methods:{
    searchArtwork: function(){
      var query = objectToHttpQuery(app.paramsArtwork);
      var url =
      $.ajax({
        url: 'https://api.art.rmngp.fr/v1/works?'+query,
        type: "GET",
        beforeSend: function(xhr){xhr.setRequestHeader('ApiKey', RMNGP_API_KEY);},
        success: function(data) {
          console.log(data);
          app.artworks = data['hits']['hits'];
          setTimeout(function(){
            $('.artwork').elevateZoom({
              zoomWindowPosition: 10,
              zoomWindowWidth: 900, //400
              zoomWindowHeight: 600, // 400
            });
            console.log('elevateZoom OK');
          }, 3000);
        }
      });
    },
    searchAuthor: function(){
      var query = objectToHttpQuery(app.paramsAuthor);
      var url =
      $.ajax({
        url: 'https://api.art.rmngp.fr/v1/authors?'+query,
        type: "GET",
        beforeSend: function(xhr){xhr.setRequestHeader('ApiKey', RMNGP_API_KEY);},
        success: function(data) {
          console.log(data);
          app.authors = data['hits']['hits'];
        }
      });
    },
    getTitle: function(artwork, lang){
      if(artwork._source && artwork._source.title && artwork._source.title[lang]){
        return artwork._source.title[lang];
      }
      return '';
    },
    getName: function(artwork, lang){
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
    }
  }
});
