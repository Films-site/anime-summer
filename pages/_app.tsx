import type { AppProps } from 'next/app'

import AnimeLayout from '@/app/layouts/AnimeLayout/AnimeLayout'
import { requireSvg } from '@/app/utils/LoadSvg'

import '@/app/styles/main.scss'
import { ReactElement, useMemo, useState } from 'react'
import {
  ThemeProvider,
  createTheme,
} from '@mui/material/styles'
import { CssBaseline } from '@mui/material'
import { ThemeContext } from '@/app/contexts/ThemeContext'
import { getColorsByTheme } from '@/app/utils/GetColorsByTheme'

requireSvg()

const App = ({ Component, pageProps }: AppProps): ReactElement => {
  const [mode, setMode] = useState<'light' | 'dark'>('dark')

  const colorMode = useMemo(
    () => ({
      toggleColorMode: () => {
        setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'))
      },
    }),
    [],
  )

  const theme = useMemo(
    () =>
      createTheme(getColorsByTheme(mode)),
    [mode]
  )

  return (
    <ThemeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <AnimeLayout>
          <Component {...pageProps} />
        </AnimeLayout>
      </ThemeProvider>
    </ThemeContext.Provider>
  )
}

export default App
