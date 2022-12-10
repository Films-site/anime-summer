import type { AppProps } from 'next/app'

import AnimeLayout from '@/app/layouts/AnimeLayout/AnimeLayout'
import { requireSvg } from '@/app/utils/loadSvg'

import '@/app/styles/main.scss'

requireSvg()

const App = ({ Component, pageProps }: AppProps): JSX.Element => {
  return (
    <AnimeLayout>
      <Component {...pageProps} />
    </AnimeLayout>
  )
}

export default App
