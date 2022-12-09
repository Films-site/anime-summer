import type { AppProps } from 'next/app'

import '../app/styles/general.scss'
import DefaultLayout from '../app/layouts/DefaultLayout/DefaultLayout'

const App = ({ Component, pageProps }: AppProps): JSX.Element => {
  return (
    <DefaultLayout>
      <Component {...pageProps} />
    </DefaultLayout>
  )
}

export default App
