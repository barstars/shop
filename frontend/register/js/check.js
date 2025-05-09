let repass = false;
function repassword_check() {
	let repassword = document.getElementById('repassword').value;
	let password = document.getElementById('password').value;
	if (password === repassword){
		console.log(true);
		repass = true;
	} else{
		console.log(false);
		repass = false;
	}
}

function is_check() {
	if (repass){
		return true;
	} else{
		return false;
	}
}