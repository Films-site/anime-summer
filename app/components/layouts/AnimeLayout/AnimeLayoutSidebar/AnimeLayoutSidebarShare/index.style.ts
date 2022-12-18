import styled from '@emotion/styled'
import { ListItem } from '@mui/material'

export const StyledShare = styled.div`
  position: relative;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

export const StyledMenuItem = styled(ListItem)`
  transition: 0.15s ease-in-out;
  position: absolute;
  left: calc(50% - 18px);
  top: calc(50% - 36px);
`

export const StyledMenu = styled.nav`
  .MuiListItem-root {
    opacity: 0;
    visibility: hidden;

    &:nth-child(1) {
      transition-delay: 0.05s;
    }

    &:nth-child(2) {
      transition-delay: 0.1s;
    }

    &:nth-child(3) {
      transition-delay: 0.15s;
    }
  }

  &.menu--active {
    .MuiListItem-root {
      opacity: 1;
      visibility: visible;

      &:nth-child(1) {
        transform: translate(-150%, -25px);
      }

      &:nth-child(2) {
        transform: translate(-125%, 25px);
      }

      &:nth-child(3) {
        transform: translate(-60%, 70px);
      }
    }
  }
`