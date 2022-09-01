import { AxiosService } from '../axios-service/axiosService'
import { AxiosRequestConfig } from 'axios'

class PostApi extends AxiosService {
	constructor(config?: AxiosRequestConfig) {
		super(config)
	}

	public getAllNews() {
		return this.axiosCall<string[]>({
			method: 'get',
			url: 'https://jsonplaceholder.typicode.com/posts'
		})
	}
}


export default new PostApi({
	baseURL: '',
	withCredentials: true
})
