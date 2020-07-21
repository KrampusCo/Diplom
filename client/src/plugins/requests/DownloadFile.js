import axios from "axios"

export default class DownloadFile{
	FileInfo(sharing_links){
		return new Promise((res) => {
			axios.get('http://localhost:5000/download', {
				params: {
					sharing_link: sharing_links
				}
			})
			.then(response => {
				res(response);
			})	
		})
	}
	downloadFile(file_id){
		return new Promise((res) => {
			var formdata = new FormData();
			formdata.append("file_id", file_id);
			axios({
				method: 'post',
				url: 'http://localhost:5001/DownloadFile',
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
	// CreateFile(token, name, size, key){
	// 	return new Promise((res) => {
	// 		var formdata = new FormData();
	// 		formdata.append("name", name);
	// 		formdata.append("size", size);
	// 		formdata.append("key", key);
	// 		axios({
	// 			method: 'post',
	// 			url: 'http://localhost:5000/addfile',
	// 			headers: {"Authorization": "Bearer " + token, 'content-type': 'multipart/form-data'},
	// 			data: formdata
	// 		}).then(response => {
	// 			res(response);
	// 		})	
	// 	})
	// }
}