
document.addEventListener("DOMContentLoaded", function() {
    const menuBtn = document.getElementById("mobileMenuBtn");
    const navMenu = document.getElementById("navMenu");
    
    if(menuBtn && navMenu) {
        menuBtn.addEventListener("click", function() {
            navMenu.classList.toggle("show");
        });
    }

    const dropdownToggle = document.querySelector(".dropdown-toggle");
    if (dropdownToggle && window.innerWidth <= 768) {
        dropdownToggle.addEventListener("click", function(e) {
            e.preventDefault();
            this.parentElement.classList.toggle("active");
        });
    }

    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(q => {
        q.addEventListener('click', () => {
            const answer = q.nextElementSibling;
            const isOpen = answer.style.display === 'block';
            
            document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = 'none');
            document.querySelectorAll('.faq-question .icon').forEach(icon => icon.textContent = '+');
            
            if (!isOpen) {
                answer.style.display = 'block';
                q.querySelector('.icon').textContent = '-';
            }
        });
    });
});
