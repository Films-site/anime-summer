import React, { FC, ReactElement, useState } from 'react'
import CommonIcon from '@/app/components/Common/CommonIcon'
import { List, ListItemButton, ListItemIcon } from '@mui/material'
import {
  StyledMenu,
  StyledMenuItem,
  StyledShare
} from
  '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar/AnimeLayoutSidebarShare/index.style'
import { useOutsideClick } from '@/app/hooks/ui/ClickOutside'

const AnimeLayoutSidebarShare: FC = (): ReactElement => {
  const [isShareMenuVisible, setIsShareMenuVisible] = useState(false)

  const handleClickOutside = (): void => {
    setIsShareMenuVisible(false)
  }

  const buttonRef = useOutsideClick(handleClickOutside)

  const handleMenuShowChange = (): void => {
    setIsShareMenuVisible(!isShareMenuVisible)
  }

  return (
    <StyledShare>
      <ListItemButton
        ref={buttonRef}
        sx={{
          background: 'none',
          padding: 0,
          margin: 0,
          ':hover': {
            background: 'none'
          },
          ':focus': {
            background: 'none'
          },
          zIndex: '3',
          position: 'relative'
        }}
        disableRipple
        onClick={handleMenuShowChange}
      >
        <ListItemIcon
          sx={{
            minWidth: 32,
            width: 32,
            height: 32,
          }}
        >
          <CommonIcon name={'share'} width={32} height={32} />
        </ListItemIcon>
      </ListItemButton>

      <StyledMenu className={isShareMenuVisible ? 'menu--active' : 'menu'}>
        <List>
          <StyledMenuItem
            sx={{
              padding: '0',
              height: '32px',
              width: '32px',
              justifyContent: 'center'
            }}>
            <a
              href={'https://t.me/miirsery'}
              target={'_blank'}
              rel="noreferrer"
            >
              <ListItemIcon
                sx={{
                  minWidth: 36,
                  width: 36,
                  height: 36,
                }}
              >
                <CommonIcon
                  name={'telegram'}
                  width={36}
                  height={36}
                />
              </ListItemIcon>
            </a>
          </StyledMenuItem>
          <StyledMenuItem
            sx={{
              padding: '0',
              height: '32px',
              width: '32px',
              justifyContent: 'center'
            }}>
            <a
              href={'https://vk.com/miirsery'}
              target={'_blank'}
              rel="noreferrer"
            >
              <ListItemIcon
                sx={{
                  minWidth: 36,
                  width: 36,
                  height: 36,
                }}
              >
                <CommonIcon
                  name={'vk-circle'}
                  width={36}
                  height={36}
                />
              </ListItemIcon>
            </a>
          </StyledMenuItem>
          <StyledMenuItem
            sx={{
              padding: '0',
              height: '32px',
              width: '32px',
              justifyContent: 'center'
            }}>
            <a
              href={'https://instagram.com/miirsery'}
              target={'_blank'}
              rel="noreferrer"
            >
              <ListItemIcon
                sx={{
                  minWidth: 36,
                  width: 36,
                  height: 36,
                }}
              >
                <CommonIcon
                  name={'instagram-circle'}
                  width={36}
                  height={36}
                />
              </ListItemIcon>
            </a>
          </StyledMenuItem>
        </List>
      </StyledMenu>
    </StyledShare>
  )
}

export default AnimeLayoutSidebarShare