function validatePasswords() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm-password').value;
    var message = document.getElementById('password-match-message');

    if (password || confirmPassword) {
        message.style.display = 'block';
        if (password.length < 8) {
            message.textContent = 'Password must be at least 8 characters';
            message.style.color = 'red';
        } else if (confirmPassword && password !== confirmPassword) {
            message.textContent = 'Passwords do not match';
            message.style.color = 'red';
        } else if (confirmPassword && password === confirmPassword) {
            message.style.display = 'none';
        }
    } else {
        message.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('password').addEventListener('input', validatePasswords);
    document.getElementById('confirm-password').addEventListener('input', validatePasswords);

    document.querySelector('form').addEventListener('submit', function(event) {
        var password = document.getElementById('password').value;
        var confirmPassword = document.getElementById('confirm-password').value;
        var message = document.getElementById('password-match-message');

        if (password.length < 8 || password !== confirmPassword) {
            event.preventDefault();
            message.style.display = 'block';
            if (password.length < 8) {
                message.textContent = 'Password must be at least 8 characters';
            } else {
                message.textContent = 'Passwords do not match';
            }
            message.style.color = 'red';
        }
    });
});