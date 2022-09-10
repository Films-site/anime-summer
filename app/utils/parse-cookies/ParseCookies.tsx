import cookie from 'cookie'

export function parseCookies(req: any) {
	console.log(req)
	return cookie.parse(req ? req.headers.cookie || '' : document.cookie)
}
