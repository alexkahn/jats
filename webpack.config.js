const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const projectRoot = path.join(__dirname, 'jats');
const jsRoot = path.join(projectRoot, 'static/js');


module.exports = {
  context: __dirname,
  entry: path.join(jsRoot, 'main.js'),
  output: {
    path: path.resolve('./jats/static/bundles/'),
    filename: '[name]-[hash].js',
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin("[name]-[contenthash].css"),
  ],
  resolve: {
    extensions: ['', '.js', '.vue', '.json'],
    fallback: [path.join(__dirname, 'node_modules')],
    alias: {
      'vue$': 'vue/dist/vue.common.js',
      'src': projectRoot,
      'assets': path.join(jsRoot, 'assets'),
      'components': path.resolve(jsRoot, 'components')
    }
  },
  resolveLoader: {
    fallback: [path.join(__dirname, 'node_modules')]
  },
  module: {
    loaders: [
      {test: /\.vue$/, loader: 'vue'},
      {test: /\.js$/, loader: 'babel', include: [path.join(projectRoot, 'static/js')], exclude: /node_modules/},
      {test: /\.json$/, loader: 'json'},
      {test: /\.css$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader")},
      {test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/, loader: 'file-loader'},
    ]
  },
  rules: [{
    test: /\.scss$/,
    use: ExtractTextPlugin.extract({
      fallback: 'style-loader',
      use: [
        'css-loader',
        'sass-loader'
      ]
    })
  }]
}
