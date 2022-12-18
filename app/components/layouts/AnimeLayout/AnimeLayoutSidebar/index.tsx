import { FC, ReactElement, useState } from 'react'
import {
  menuItems
} from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar/index.constants'
import CommonToggleTheme from '@/app/components/Common/CommonToggleTheme'
import {
  List,
  ListItem,
  ListItemButton,
  ListItemIcon
} from '@mui/material'
import {
  StyledExpand,
  StyledSidebar
} from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar/index.style'
import CommonIcon from '@/app/components/Common/CommonIcon'
import Link from 'next/link'
import { BaseText } from '@/app/styles/general'
import AnimeLayoutSidebarShare
  from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar/AnimeLayoutSidebarShare'

const AnimeLayoutSidebar: FC = (): ReactElement => {
  const [isAuth, setIsAuth] = useState(true)
  const [isHide, setIsHide] = useState(false)
  
  return (
    <StyledSidebar p={1} className={isHide ? 'hide' : ''}>
      <List>
        {
          !isAuth
            ? (
              <ListItem className={'item'}>
                <Link href={'/profile'} passHref>
                  <a className={'d-f ai-c'}>
                    <ListItemIcon
                      sx={{
                        minWidth: 24,
                        width: 24,
                        height: 24,
                      }}
                    >
                      <CommonIcon
                        className={'mr-8'}
                        name={'profile'}
                        width={24}
                        height={24}
                      />
                    </ListItemIcon>
                    <BaseText className={'text'}>miirsery</BaseText>
                  </a>
                </Link>
              </ListItem>
            )
            : (
              <ListItem>
                <ListItemButton
                  sx={{
                    background: 'none',
                    padding: 0,
                    margin: 0,
                    ':hover': {
                      background: 'none'
                    },
                    ':focus': {
                      background: 'none'
                    }
                  }}
                  onClick={() => setIsAuth(!isAuth)}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 24,
                      width: 24,
                      height: 24,
                      marginRight: '8px',
                    }}
                  >
                    <CommonIcon name={'profile'} width={24} height={24} />
                  </ListItemIcon>
                  <BaseText className={'text'}>Войти</BaseText>
                </ListItemButton>
              </ListItem>
            )
        }
        {
          menuItems
            .map(({ label, iconName, url }, index) => (
              <ListItem key={index}>
                <Link href={url}>
                  <a className={'d-f ai-c jc-sb'}>
                    <ListItemIcon
                      sx={{
                        minWidth: 24,
                        width: 24,
                        height: 24,
                        marginRight: '8px',
                      }}
                    >
                      <CommonIcon
                        className={'mr-8'}
                        name={iconName}
                        width={24}
                        height={24}
                      />
                    </ListItemIcon>
                    <BaseText className={'text'}>{label}</BaseText>
                  </a>
                </Link>
              </ListItem>)
            )
        }
        <ListItem>
          <ListItemButton
            sx={{
              background: 'none',
              padding: 0,
              margin: 0,
              ':hover': {
                background: 'none'
              },
              ':focus': {
                background: 'none'
              }
            }}
          >
            <ListItemIcon
              sx={{
                minWidth: 24,
                width: 24,
                height: 24,
                marginRight: '8px',
              }}
            >
              <CommonIcon name={'notifications'} width={24} height={24} />
            </ListItemIcon>
            <BaseText className={'text'}>Уведомления</BaseText>
          </ListItemButton>
        </ListItem>
        {
          !isAuth && (
            (
              <ListItem>
                <ListItemButton
                  sx={{
                    background: 'none',
                    padding: 0,
                    margin: 0,
                    ':hover': {
                      background: 'none'
                    },
                    ':focus': {
                      background: 'none'
                    }
                  }}
                  onClick={() => setIsAuth(!isAuth)}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 24,
                      width: 24,
                      height: 24,
                      marginRight: '8px',
                    }}
                  >
                    <CommonIcon name={'logout'} width={24} height={24} />
                  </ListItemIcon>
                  <BaseText className={'text'}>Выйти</BaseText>
                </ListItemButton>
              </ListItem>
            )
          )
        }

        <div className={'anime-layout-sidebar__footer'}>
          <ListItem
            sx={{
              padding: 0,
              margin: 0,
              flexDirection: 'column'
            }}
          >
            <AnimeLayoutSidebarShare />
          </ListItem>
          <ListItem>
            <CommonToggleTheme />
          </ListItem>
        </div>

      </List>
      <StyledExpand
        className={'expand-button'}
        onClick={() => setIsHide(!isHide)}
      >
        <CommonIcon
          name={'arrow-light'}
          width={24}
          height={24}
          reverse={!isHide}
        />
      </StyledExpand>
    </StyledSidebar>
  )
}

export default AnimeLayoutSidebar