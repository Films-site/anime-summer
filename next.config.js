// eslint-disable-next-line @typescript-eslint/no-var-requires
const path = require("path")
// eslint-disable-next-line @typescript-eslint/no-var-requires
const SpriteLoaderPlugin = require('svg-sprite-loader/plugin')

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
  compiler: {
    styledComponents: true
  },
  swcMinify: true,
  sassOptions: {
    includePaths: [path.join(__dirname, './app/styles')],
    prependData: `@import "@/app/styles/resources/variables/index.scss";`,
  },
  images : {
    domains : ['localhost']
  },
  webpack: (
    config
  ) => {
    config.module.rules.push({
      test: /\.svg$/,
      loader: 'svg-sprite-loader'
    })

    config.plugins.push(new SpriteLoaderPlugin())

    return config
  }
}

module.exports = nextConfig
