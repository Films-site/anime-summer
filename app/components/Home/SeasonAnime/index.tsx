import React, { FC } from 'react'
import styled from 'styled-components'
import Image from 'next/image'
import Overload from '../../../assets/images/overlord.jpg'
import Star from '../../../assets/images/star.svg'
import Link from 'next/link'

const ItemImage = styled.div`
	position: relative;
	width: 160px;
	height: 225px;
`

const Border = styled.div`
	border-bottom: 1px solid #000;
	padding-top: 12px;
`

const SeasonItem = styled.div`
	position: relative;

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

const SeasonAnime: FC = () => {
	return (
		<>
			<Border />
			<div className='container pb-12'>
				<div className='season-anime'>
					<h2 className='heading-2 mb-24 pt-12'>Аниме летнего сезона</h2>
					<div className='d-flex ai-center jc-between'>
						<SeasonItem>
							<Link href='/anime/12'>
								<ItemImage className='mb-12'>
									<a>
										<Image
											src={Overload}
											layout='fill'
											objectFit='none'
											quality={100}
											alt='Overload'
										/>
									</a>
								</ItemImage>
							</Link>
							<Link href='/anime/12' prefetch passHref>
								<a>
									<h3 className='heading-3'>Повелитель 4</h3>
								</a>
							</Link>
							<div className='rating'>
								<div className='rating__image'>
									<Image src={Star} alt='star' />
								</div>
								<p className='rating__text'>5.3</p>
							</div>
						</SeasonItem>
					</div>
				</div>
			</div>
			<Border />
		</>
	)
}

export default SeasonAnime
