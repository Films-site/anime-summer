import { NextPage } from 'next'
import { IProps } from './DefaultLayout.interfaces'
import DefaultLayoutHeader from '../../components/layouts/DefaultLayout/DefaultLayoutHeader'

const DefaultLayout: NextPage<IProps> = ({ children }): JSX.Element => {
  return (
    <>
      <DefaultLayoutHeader />
      <div className={'container'}>{children}</div>
      <footer>footer</footer>
    </>
  )
}

export default DefaultLayout
