import { PaletteMode } from '@mui/material'
import { ThemeOptions } from '@mui/material/styles/createTheme'
import { ColorsDark, ColorsLight } from '@/app/constants/color.constant'

interface ICustomTheme extends ThemeOptions {
  palette: {
    mode: PaletteMode,
    primary: {
      main: ColorsDark | ColorsLight,
      secondary: ColorsDark | ColorsLight
    },
    background: {
      default: ColorsDark | ColorsLight
      light: ColorsDark | ColorsLight
    },
    text: {
      primary: ColorsDark | ColorsLight
    }
  }
}
export const getColorsByTheme = (
  mode: PaletteMode
): ICustomTheme => <ICustomTheme>({
  palette: {
    mode,
    ...(mode === 'light'
      ? {
        // palette values for light mode
        primary: {
          main: ColorsLight.BACKGROUND_DARK,
          secondary: ColorsLight.BACKGROUND_LIGHT
        },
        background: {
          light: ColorsLight.BACKGROUND_LIGHT,
        },
      }
      : {
        // palette values for dark mode
        primary: {
          main: ColorsDark.PRIMARY_DARK,
        },
        text: {
          primary: ColorsDark.TEXT,
        },
        background: {
          light: ColorsDark.BACKGROUND_LIGHT,
        },
      }),
  },
})
