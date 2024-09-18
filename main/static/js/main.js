document.addEventListener('DOMContentLoaded', function() {
    const mainHeader = document.getElementById('mainHeader');
    const mainNav = document.getElementById('mainNav');
    const loginBtn = document.getElementById('loginBtn');
    const logoutBtn = document.getElementById('logoutBtn');
    const userIcon = document.getElementById('userIcon');
    const messageIcon = document.getElementById('messageIcon');
    const loginModal = document.getElementById('loginModal');
    const loginForm = document.getElementById('loginForm');

    // Gestion de la navigation fixe
    window.addEventListener('scroll', function() {
        if (window.scrollY > mainHeader.offsetHeight) {
            mainNav.classList.add('fixed');
            mainHeader.style.display = 'none';
        } else {
            mainNav.classList.remove('fixed');
            mainHeader.style.display = 'flex';
        }
    });

    // Gestion de la connexion
    loginBtn.addEventListener('click', function() {
        loginModal.style.display = 'block';
    });

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        fetch('/login/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loginBtn.style.display = 'none';
                logoutBtn.style.display = 'block';
                if (data.user_type === 'regular') {
                    messageIcon.style.display = 'block';
                } else if (data.user_type === 'special' || data.user_type === 'admin') {
                    userIcon.style.display = 'block';
                }
                loginModal.style.display = 'none';
            } else {
                alert('Échec de la connexion. Veuillez réessayer.');
            }
        });
    });

    // Gestion de la déconnexion
    logoutBtn.addEventListener('click', function() {
        fetch('/logout/', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loginBtn.style.display = 'block';
                logoutBtn.style.display = 'none';
                userIcon.style.display = 'none';
                messageIcon.style.display = 'none';
            }
        });
    });

    // Gestion des icônes utilisateur et message
    userIcon.addEventListener('click', function() {
        // Rediriger vers la page admin ou partenaire selon le type d'utilisateur
        window.location.href = '/admin/'; // ou '/partner-admin/' pour les partenaires
    });

    messageIcon.addEventListener('click', function() {
        // Afficher les messages ou rediriger vers une page de messages
    });
});