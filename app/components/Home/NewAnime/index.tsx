import React, { useEffect, useState } from 'react'
import styled from 'styled-components'
import Link from 'next/link'
import Image, { ImageLoaderProps } from 'next/image'
import Star from '../../../assets/images/star.svg'
import animeApi from '../../../api/anime/anime.api'
import { AnimeListResponseType } from '../../../api/anime/anime.types'

const StyledNewAnime = styled.div`
	max-width: 900px;
	width: 100%;
	margin-right: 30px;
`

const SeasonItem = styled.div`
	position: relative;
	margin-bottom: 16px;

	.wrapper {
		display: flex;
	}

	.link {
		span,
		img {
			width: 160px !important;
			height: 225px !important;
		}
	}

	.rating {
		display: flex;
		align-items: center;
		position: absolute;
		z-index: 2;
		top: 20px;
		left: -8px;
		width: 80px;
		height: 22px;
		background: #eb9c62;

		&__image {
			margin-left: 4px;
			width: 20px;
			height: 20px;
		}

		&__text {
			font-weight: 600;
			margin-top: 2px;
			margin-left: 8px;
		}
	}
`

const myLoader = ({ src }: ImageLoaderProps): string => {
	return decodeURI(src)
}

const NewAnime = () => {
	const [anime, setAnime] = useState<AnimeListResponseType[]>([
		{
			description: '',
			id: 0,
			preview: '',
			title: ''
		}
	])

	const getAnimeList = async (): Promise<void> => {
		const [error, data] = await animeApi.getAnimeList()

		if (!error && data) {
			setAnime(data)
		}
	}

	useEffect(() => {
		getAnimeList()
	}, [])

	return (
		<StyledNewAnime className='new-anime'>
			<h2 className='heading-2 mb-24'>Новые аниме на сайте</h2>
			{anime &&
				anime.map(({ id, preview, title, description }) => (
					<SeasonItem key={id}>
						<div className='wrapper'>
							<Link href={`/anime/:${id}`} prefetch passHref>
								<a className='link mr-12'>
									<Image
										loader={myLoader}
										src={encodeURI(preview)}
										width={160}
										height={225}
										quality={100}
										alt={title}
									/>
								</a>
							</Link>
							<div className='info'>
								<Link href={`/anime/${id}`} prefetch passHref>
									<a>
										<h3 className='heading-2'>{title}</h3>
									</a>
								</Link>
								<div className='info__description'>{description}</div>
							</div>
						</div>
						<div className='rating'>
							<div className='rating__image'>
								<Image src={Star} alt='star' />
							</div>
							<p className='rating__text'>5.3</p>
						</div>
					</SeasonItem>
				))}
		</StyledNewAnime>
	)
}

export default NewAnime
