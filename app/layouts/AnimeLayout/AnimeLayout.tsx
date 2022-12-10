import { NextPage } from 'next'
import { IProps } from './AnimeLayout.interfaces'
import AnimeLayoutHeader
  from '@/app/components/layouts/AnimeLayout/AnimeLayoutHeader'
import AnimeLayoutSidebar
  from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar'

const AnimeLayout: NextPage<IProps> = ({ children }): JSX.Element => {
  return (
    <div className={'container'}>
      <AnimeLayoutHeader />
      <div className={'d-f w-100 jc-sb'}>
        <div>{children}</div>
        <AnimeLayoutSidebar />
      </div>
      <footer>footer</footer>
    </div>
  )
}

export default AnimeLayout
