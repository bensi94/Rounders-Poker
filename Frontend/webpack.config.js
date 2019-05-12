const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require('webpack');

module.exports = {
    devtool: 'inline-source-map',
    entry: './Src/index.js',
    output: {
        path: path.join(__dirname, '/dist'),
        publicPath: '/',
        filename: 'bundle.js'
    },
    devServer: {
        contentBase: './dist',
        host: process.env.HOST,
        historyApiFallback: true,
        open: true
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        mainFields: ['jsnext:main', 'main']
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader', 'eslint-loader']
            },
            {
                test: /\.(less|css)$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'less-loader'
                ]
            },
            {
                test: /\.(ttf|eot|svg|woff|woff2)(\?.+)?$/,
                loader: 'file-loader?name=[hash:12].[ext]'
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: path.resolve('./index.html')
        }),
        new webpack.DefinePlugin({
            'process.env.BASE_API_URL': JSON.stringify(process.env.BASE_API_URL)
        })
    ]
};
