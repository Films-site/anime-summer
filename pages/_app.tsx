import type { AppProps } from 'next/app'

import AnimeLayout from '@/app/layouts/AnimeLayout/AnimeLayout'

import '@/app/styles/main.scss'

const App = ({ Component, pageProps }: AppProps): JSX.Element => {
  return (
    <AnimeLayout>
      <Component {...pageProps} />
    </AnimeLayout>
  )
}

export default App
