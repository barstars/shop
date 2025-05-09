async function loginned() {
	let username = document.getElementById('username').value;
	let password = document.getElementById('password').value;

	const response = await fetch("/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({username: username,
							password: password}),
	});

	if (!response.ok) {
		console.error("Ошибка при отправке запроса:", response.status);
	}

	const data = await response.json();
	console.log(data)
}