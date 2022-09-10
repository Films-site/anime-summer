import { NextPage } from 'next'
import { ReactNode } from 'react'
import TheHeader from '../Header'

type LayoutProps = {
	children: ReactNode
}

const Layout: NextPage<LayoutProps> = ({ children }) => {
	return (
		<>
			<TheHeader />
			{children}
		</>
	)
}

export default Layout
