import { FC } from 'react'
import {
  menuItems
} from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar/index.constants'
import CommonToggleTheme from '@/app/components/Common/CommonToggleTheme'

const AnimeLayoutSidebar: FC = (): JSX.Element => {
  return (
    <aside>
      <nav>
        <ul>
          {
            menuItems.map(({ label }, index) => (<li key={index}>{label}</li>))
          }
          <li>
            <CommonToggleTheme />
          </li>
        </ul>
      </nav>
    </aside>
  )
}

export default AnimeLayoutSidebar