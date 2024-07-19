document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                alert('Please fill out all required fields.');
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Button hover effect
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(90deg, #00ff6a, #00d2ff, #7f00ff, #ee0979, #ff6a00)';
        });
        button.addEventListener('mouseleave', function() {
            this.style.background = 'linear-gradient(90deg, #ff6a00, #ee0979, #7f00ff, #00d2ff, #00ff6a)';
        });
    });

    // Example of additional interactive feature: Toggle content
    const toggleButtons = document.querySelectorAll('.toggle-btn');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const content = document.querySelector(this.dataset.target);
            if (content) {
                content.classList.toggle('hidden');
            }
        });
    });
});
