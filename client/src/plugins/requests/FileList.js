import axios from "axios"

export default class FileList{
	AllUserFile(token){
		return new Promise((res) => {
			axios({
				method: 'get',
				url: 'http://localhost:5000/AllUserFile',
				headers: {"Authorization": "Bearer " + token},
			}).then(response => {
				res(response);
			})	
		})
	}
	CreateFile(token, name, size, key){
		return new Promise((res) => {
			var formdata = new FormData();
			formdata.append("name", name);
			formdata.append("size", size);
			formdata.append("key", key);
			axios({
				method: 'post',
				url: 'http://localhost:5000/addfile',
				headers: {"Authorization": "Bearer " + token, 'content-type': 'multipart/form-data'},
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
	SharingFile(token, server_id , file_id){
		return new Promise((res) => {
			var formdata = new FormData();
			formdata.append("server_id", server_id);
			formdata.append("file_id", file_id);
			axios({
				method: 'post',
				url: 'http://localhost:5000/sharingFile',
				headers: {"Authorization": "Bearer " + token, 'content-type': 'multipart/form-data'},
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
	uploadFile(token, server_ip, file_id, content){
		return new Promise((res) => {
			var formdata = new FormData();
			formdata.append("file_id", file_id);
			formdata.append("byte", content);
			axios({
				method: 'post',
				url: 'http://'+server_ip+'/UploadFile',
				headers: {"Authorization": "Bearer " + token, 'content-type': 'multipart/form-data'},
				data: formdata
			}).then(response => {
				res(response);
			})	
		})
	}
}