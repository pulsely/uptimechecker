'use strict'
const {VueLoaderPlugin} = require('vue-loader')
const path = require('path');
const webpack = require('webpack');

// const Uppy = require('@uppy/core');
// const XHRUpload = require('@uppy/xhr-upload');
// const companion = require('@uppy/companion');
// const Dashboard = require('@uppy/dashboard');


module.exports = {
    mode: 'development',
    entry: [
        './src/app.js'
    ],
    output: {
        filename: '../../lookandfeel/js/bundle-2022-09-23.js',
        path: path.resolve(__dirname, '../src/')
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
            {
            test: /\.(jpe?g|png|gif|woff|woff2|eot|ttf|svg)(\?[a-z0-9=.]+)?$/,
            loader: 'url-loader?limit=100000'
        }
        ]

    },
    plugins: [
        new VueLoaderPlugin(),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js'
        },
    }
}
