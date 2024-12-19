const apiUrl = 'http://127.0.0.1:5000';

async function register() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${apiUrl}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
    });

    const data = await response.json();
    alert(data.message || data.error);
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${apiUrl}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
    });

    const data = await response.json();
    if (response.ok) {
        document.getElementById('auth').classList.add('hidden');
        document.getElementById('game').classList.remove('hidden');
        alert(data.message);
    } else {
        alert(data.error);
    }
}

async function hit() {
    const response = await fetch(`${apiUrl}/play`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'hit' }),
    });

    const data = await response.json();
    updateGameStatus(data);
}

async function stand() {
    const response = await fetch(`${apiUrl}/play`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action: 'stand' }),
    });

    const data = await response.json();
    updateGameStatus(data);
}

async function logout() {
    const response = await fetch(`${apiUrl}/logout`, {
        method: 'POST',
    });

    const data = await response.json();
    if (response.ok) {
        document.getElementById('game').classList.add('hidden');
        document.getElementById('auth').classList.remove('hidden');
        alert(data.message);
    }
}

function updateGameStatus(data) {
    const status = document.getElementById('status');
    const playerHand = document.getElementById('player-hand');
    const dealerHand = document.getElementById('dealer-hand');

    if (data.result) {
        status.innerText = `Result: ${data.result}`;
    }
    playerHand.innerText = `Player Hand: ${data.player_hand}`;
    if (data.dealer_hand) {
        dealerHand.innerText = `Dealer Hand: ${data.dealer_hand}`;
    }
}
