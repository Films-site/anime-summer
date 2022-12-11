import { FC, ReactElement, useContext } from 'react'
import { Switch } from '@mui/material'
import { ThemeContext } from '@/app/contexts/ThemeContext'

const CommonToggleTheme: FC = (): ReactElement => {
  const colorMode = useContext(ThemeContext)

  return (
    <Switch onChange={colorMode.toggleColorMode} />
  )
}

export default CommonToggleTheme