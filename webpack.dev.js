const { merge } = require('webpack-merge');
const common = require("./webpack.common");

module.exports = merge(common, {
    mode: 'development',
    watch:true,
    watchOptions:{
        aggregateTimeout: 200,
        poll: 1000
    },
    devServer: {
        contentBase: './static/dist'
    }
})