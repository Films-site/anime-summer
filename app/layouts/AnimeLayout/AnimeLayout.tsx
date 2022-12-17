import { NextPage } from 'next'
import AnimeLayoutHeader
  from '@/app/components/layouts/AnimeLayout/AnimeLayoutHeader'
import AnimeLayoutSidebar
  from '@/app/components/layouts/AnimeLayout/AnimeLayoutSidebar'
import { ReactNode } from 'react'

interface IProps {
  children: ReactNode
}

const AnimeLayout: NextPage<IProps> = (
  {
    children,
  }): JSX.Element => {
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
