import { AxiosService } from '../axios-service/axiosService'
import { AxiosRequestConfig } from 'axios'
import { AnimeListResponseType } from './anime.types'

class AnimeApi extends AxiosService {
	constructor(config?: AxiosRequestConfig) {
		super(config)
	}

	getAnimeList() {
		return this.axiosCall<AnimeListResponseType[]>({
			method: 'get',
			url: 'http://localhost:8000/api/v1/anime/'
		})
	}
}

export default new AnimeApi({
	baseURL: '',
	withCredentials: false
})
