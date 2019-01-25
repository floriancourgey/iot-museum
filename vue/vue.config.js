module.exports = {
  outputDir: '../dist',
  // publicPath: '/',
  publicPath: '/static/',
  filenameHashing: false,
  pages: {
    index: {
      entry: 'src/museum-front/main.js',
      template: 'templates/museum-front.html',
      filename: '../museum/templates/museum/index.html', // relative to dist
    },
  },
}
