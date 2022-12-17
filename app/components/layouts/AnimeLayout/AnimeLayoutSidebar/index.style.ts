import styled from '@emotion/styled'
import { Box, Button } from '@mui/material'
import { ThemeOptions } from '@mui/material/styles/createTheme'
import { transform } from "@babel/core";

interface ICustomTheme extends ThemeOptions {
  palette: {
    primary: {
      main: string,
      secondary: string
    },
    background: {
      default: string
      light: string
    },
    text: {
      primary: string
    }
  }
}

export const StyledSidebar = styled(Box)(
  (
    { theme }: { theme?: ICustomTheme }
  ) => ({
    position: 'relative',
    height: 'calc(100vh - 32px)',
    display: 'flex',
    alignItems: 'center',
    borderBottomLeftRadius: '8px',
    borderTopLeftRadius: '8px',
    translate: 'transformX(0)',
    backgroundColor: theme?.palette?.background?.light,
    boxShadow: '-15px 0px 40px 9px rgba(178, 142, 221, 0.1)',
    transition: 'all 0.3s ease-in-out',

    '&.hide': {
      padding: '0',
      translate: 'transformX(-100px)',
      transition: 'all 0.3s ease-in-out',

      '.MuiList-root': {
        width: '60px',
      },

      '.MuiListItem-root': {
        justifyContent: 'center'
      },

      '.item': {
        padding: '8px',
        justifyContent: 'center'
      },

      '.text': {
        display: 'none'
      },

      '.MuiListItemIcon-root': {
        marginRight: '0'
      },

      '.MuiTouchRipple-root': {
        width: '0',
        display: 'none'
      },

      '.app-icon': {
        marginRight: '0 !important',
      },

      '.MuiSwitch-root': {
        position: 'absolute',
        left: '0'
      },

      '.MuiSwitch-track': {
        position: 'relative',
        left: '3px',
        height: '12px',
      },

      '.MuiSwitch-thumb': {
        width: '16px',
        height: '16px',
        transform: 'translate(5px, 1px)'
      },

      '.expand-button': {
        left: '-35px'
      }
    },
  })
)

export const StyledExpand = styled(Button)(
  (
    { theme }: { theme?: ICustomTheme }
  ) => ({
    position: 'absolute',
    borderRadius: '50%',
    left: '-25%',
    color: theme?.palette.primary.main,
    backgroundColor: theme?.palette.primary.secondary,
    height: '36px',
    width: '36px',
    minWidth: '36px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',

    'svg': {
      position: 'absolute',
      left: '2px',
      top: '4px',

      '&.reverse': {
        left: '11px',
        top: '9px'
      }
    }
  })
)

