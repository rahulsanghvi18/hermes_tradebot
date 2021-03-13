const path = require('path')
const webpack = require('webpack');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {
        frontend: [
            path.resolve(__dirname, "apps/static/js/frontend/index.js"),
            path.resolve(__dirname, "apps/static/scss/frontend/index.scss")
        ],
        account: [
            path.resolve(__dirname, "apps/static/js/account/index.js"),
            path.resolve(__dirname, "apps/static/scss/account/index.scss")
        ]
    },
    output: {
        filename: "[name]-[contenthash].min.js",
        path: path.resolve(__dirname, "static/dist"),
        publicPath: "./"
    },
    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader"
                ]
            },
            {
                test: /\.js$/,
                enforce: 'pre',
                use: ['source-map-loader'],
            },
            {
                test: require.resolve("jquery"),
                loader: "expose-loader",
                options: {
                  exposes: ["$", "jQuery"],
                },
            },
        ]
    },
    plugins: [
        new webpack.ProgressPlugin(),
        new CleanWebpackPlugin(),
        new BundleTracker(options = {
            filename: "./webpack-stats.json",
            publicPath: '/static/dist/'
        }),
        new MiniCssExtractPlugin({
            filename: "[name]-[contenthash].min.css",
            chunkFilename: "[id]-[contenthash].min.css",
        }),
    ]
}