async function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;

    const response = await fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    alert('Registered! API Key: ' + data.api_key);
}

async function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const response = await fetch('/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ username, password }),
    });

    if (!response.ok) {
        alert('Login failed!');
        return;
    }

    const data = await response.json();
    localStorage.setItem('token', data.access_token);
    alert('Logged in! Token: ' + data.access_token);

    // Redirect to the home page
    window.location.href = '/static/home.html';
}

function enableApiButtons() {
    document.getElementById('api1').disabled = false;
    document.getElementById('api2').disabled = false;
    document.getElementById('api3').disabled = false;
    document.getElementById('api4').disabled = false;
}

async function callApi1() {
    alert('API 1 called! (Function not implemented)');
}

async function callApi2() {
    alert('API 2 called! (Function not implemented)');
}

async function callApi3() {
    alert('API 3 called! (Function not implemented)');
}

async function callApi4() {
    alert('API 4 called! (Function not implemented)');
}
