import { PaletteMode } from '@mui/material'
import { ThemeOptions } from '@mui/material/styles/createTheme'
import { ColorConstants } from '@/app/constants/color.constant'

export const getColorsByTheme = (mode: PaletteMode): ThemeOptions => ({
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
