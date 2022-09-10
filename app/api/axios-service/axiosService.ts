import axios, { AxiosInstance, AxiosRequestConfig } from 'axios'
import { ChMessage } from 'cheetah-react-ui'
import { AxiosResponseType } from './axiosService.type'

export class AxiosService {
	axiosInstance: AxiosInstance

	constructor(config?: AxiosRequestConfig) {
		this.axiosInstance = axios.create(config)

		this.axiosInstance.interceptors.request.use((config) => {
			// const token = Cookies.get('token_for_admin_panel')

			// config.xsrfCookieName = 'XSRF-TOKEN'
			// config.xsrfHeaderName = 'X-XSRF-TOKEN'

			// config.headers = {
			// 	Authorization: `Bearer ${token}`,
			// }

			return config
		})

		this.axiosInstance.interceptors.response.use(
			(response) => {
				if (response.data.message) {
					ChMessage({
						message: response.data.message || 'Error',
						mode: 'success'
					})
				}
				return response
			},
			(error) => {
				const response = error?.response?.data
				switch (error?.response?.status) {
					case 401:
						break
					case 404:
						break
					case 422:
						if (process.env.NODE_ENV !== 'production') {
							ChMessage({
								message: response.code.message || 'Неверный логин или пароль!',
								mode: 'error'
							})
						}
						break

					default:
						if (response.code.message) {
							ChMessage({
								message: response.code.message,
								mode: 'error'
							})
						}
						break
				}
				return Promise.reject(response.code ? response.code : response)
			}
		)
	}

	async axiosCall<T = any>(
		config: AxiosRequestConfig
	): Promise<AxiosResponseType<T>> {
		try {
			const { data } = await this.axiosInstance.request<T>(config)
			return [null, data]
		} catch (error: any) {
			return [error]
		}
	}
}
