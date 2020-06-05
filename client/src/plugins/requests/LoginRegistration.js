import axios from "axios"

export default class LoginRegistrations{
	login(requestData){
		var formdata = new FormData();
		formdata.append("username", requestData.login);
		formdata.append("password", requestData.password);
		return new Promise((res) => {
			axios({
				method: 'post',
				url: 'http://localhost:5000/login',
				headers: { 'content-type': 'multipart/form-data' },
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
	registration(requestData){
		var formdata = new FormData();
		formdata.append("username", requestData.login);
		formdata.append("password", requestData.password);
		return new Promise((res) => {
			axios({
				method: 'post',
				url: 'http://localhost:5000/registration',
				headers: { 'content-type': 'multipart/form-data' },
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
}

	// login: {
 //		login: null,
 //		password:null,
 //		login_token: null,
 //		refresh_token:null,
 //	},
	// registration (requestData) {
	// 	return new Promise((res, rej) => {
	// 		axios
	// 		.get(``)
	// 		.then(response => {
	// 			requestData.searchCountWords = response.data.count;
	// 			requestData.login_token = response. ;
	// 			requestData.refresh_token = response. ;
	// 		})
	// 		axios
	// 		.get(`/api/words/`)
	// 		.then(response => {
	// 			requestData.allCountWords = response.data.count;	
	// 			res(requestData.words);
	// 		})
	// 	})

	// }