document.addEventListener('DOMContentLoaded', function() {

    /* =========================================
       1. SECURITY: GET DJANGO CSRF TOKEN
       ========================================= */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    /* =========================================
       2. NAVBAR LOGIC (Mobile Menu)
       ========================================= */
    const menuBtn = document.querySelector('.checkbtn');
    const navLinks = document.querySelector('.navbar ul');
    
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        document.querySelectorAll('.navbar ul li a').forEach(link => {
            link.addEventListener('click', () => {
                document.getElementById('check').checked = false;
                navLinks.classList.remove('active');
            });
        });
    }

});