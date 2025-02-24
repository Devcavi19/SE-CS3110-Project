window.onload = function() {
    document.getElementById('password').value = '';
}

function checkInputs() {
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const signinButton = document.getElementById('signinButton');
    
    signinButton.disabled = !(email && password);
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('email').addEventListener('input', checkInputs);
    document.getElementById('password').addEventListener('input', checkInputs);

    document.getElementById('loginForm').addEventListener('submit', function() {
        setTimeout(() => {
            document.getElementById('password').value = '';
            checkInputs();
        }, 100);
    });
});

function signup() {
    window.location.href = "/signup";
}