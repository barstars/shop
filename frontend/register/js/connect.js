async function register() {
	if (is_check()){
		let username = document.getElementById('username').value;
		let email = document.getElementById('email').value;
		let password = document.getElementById('password').value;

		const response = await fetch("/login/reg", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({username: username,
								email: email,
								password: password}),
		});

		if (!response.ok) {
			console.error("Ошибка при отправке запроса:", response.status);
		}

		const data = await response.json();
		console.log(data)
	}
}