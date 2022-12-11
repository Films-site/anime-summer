import type { AppProps } from 'next/app'

import AnimeLayout from '@/app/layouts/AnimeLayout/AnimeLayout'
import { requireSvg } from '@/app/utils/loadSvg'

import '@/app/styles/main.scss'
import { useMemo, useState } from 'react'
import {
  ThemeProvider,
  createTheme,
} from '@mui/material/styles'
import { CssBaseline, PaletteMode } from '@mui/material'
import { ThemeOptions } from '@mui/material/styles/createTheme'
import { ColorConstants } from '@/app/constants/color.constant'
import { ThemeContext } from '@/app/contexts/ThemeContext'

requireSvg()

const getDesignTokens = (mode: PaletteMode): ThemeOptions => ({
  palette: {
    mode,
    ...(mode === 'light'
      ? {
        // palette values for light mode
        primary: {
          main: ColorConstants.PRIMARY_DARK,
        },
        secondary: {
          light: '#0066ff',
          main: '#0044ff',
          contrastText: '#ffcc00',
        },
      }
      : {
        // palette values for dark mode
        primary: {
          main: ColorConstants.PRIMARY,
        },
      }),
  },
})

const App = ({ Component, pageProps }: AppProps): JSX.Element => {
  const [mode, setMode] = useState<'light' | 'dark'>('light')

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
      createTheme(getDesignTokens(mode)),
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
