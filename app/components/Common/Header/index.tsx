import React from 'react'
import Link from 'next/link'
import styled from 'styled-components'
import { useRouter } from 'next/router'

type navItemType = {
	name: string,
	url: string
}

const navItems: navItemType[] = [
	{
		name: 'Аниме',
		url: '/anime'
	},
	{
		name: 'Манга',
		url: '/manga'
	},
	{
		name: 'Музыка',
		url: '/music'
	}
]

const StyledLink = styled.a`
	color: ${(props: { active: boolean }) =>
		props.active ? "['$color--accent']" : '#6f0606'};

	&:hover {
		color: #ef893f;
	}
`

const TheHeader = () => {
	const router = useRouter()

	return (
		<>
			<div className='container'>
				<header className='the-header'>
					<Link href='/'>Home</Link>
					<nav>
						<ul className='d-flex ai-center ml-16'>
							{navItems.map(({ name, url }, index) => (
								<li key={index}>
									<Link prefetch href={url} passHref>
										<StyledLink active={router.pathname === url}>
											{name}
										</StyledLink>
									</Link>
								</li>
							))}
						</ul>
					</nav>
				</header>
			</div>
		</>
	)
}

export default TheHeader
