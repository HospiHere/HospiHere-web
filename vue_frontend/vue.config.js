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
}