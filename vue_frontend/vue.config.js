/*
module.exports = {
  "pages": {
    "vue_app_01": {
      "entry": "./src/main.js",
      "chunks": [
        "chunk-vendors"
      ]
    },
    "blood_bank": {
      "entry": "./src/blood_bank.js",
      "chunks": [
        "chunk-vendors"
      ]
    }
  },
  "filenameHashing": false,
  "productionSourceMap": false,
  "publicPath": "http://localhost:8080/",
  "outputDir": "../django_vue_mpa/static/vue/",
  "transpileDependencies": [
    "vuetify"
  ]
}    */

const BundleTracker = require("webpack-bundle-tracker");

const pages = {
    'vue_app_01': {
        entry: './src/main.js',
        chunks: ['chunk-vendors']
    },
    "blood_bank": {
      "entry": "./src/blood_bank.js",
      "chunks": [
        "chunk-vendors"
      ]
    },
    "bed_management": {
      "entry": "./src/bed_management.js",
      "chunks": [
        "chunk-vendors"
      ]
    },
}

module.exports = {
    pages: pages,
    filenameHashing: false,
    productionSourceMap: false,
    publicPath: process.env.NODE_ENV === 'production'
        ? ''
        : 'http://localhost:8080/',
    outputDir: '../django_vue_mpa/static/vue/',

    chainWebpack: config => {

        config.optimization
            .splitChunks({
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "chunk-vendors",
                        chunks: "all",
                        priority: 1
                    },
                },
            });

        Object.keys(pages).forEach(page => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        })

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../vue_frontend/webpack-stats.json'}]);

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://localhost:8080')
            .host('localhost')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["*"]})

    }
};