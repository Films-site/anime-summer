import '../app/styles/main.scss'
import type { AppProps } from 'next/app'
import Layout from "../app/components/Common/Layout";
import { QueryClient, QueryClientProvider } from 'react-query';

const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            refetchOnWindowFocus: false
        }
    }
})

const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
	<QueryClientProvider client={queryClient}>
      <Layout>
        <main>
          <Component {...pageProps} />
        </main>
      </Layout>
	</QueryClientProvider>
  )
}

export default MyApp
