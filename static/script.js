// Smooth scrolling function
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Print/PDF function
function printPage() {
    // Show print dialog
    window.print();
}

// Scroll Animation Trigger
function triggerScrollAnimations() {
    const rightCards = document.querySelectorAll('.right-card');
    
    rightCards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (cardTop < windowHeight * 0.85) {
            card.classList.add('in-view');
        }
    });
}

// Add animations on page load
document.addEventListener('DOMContentLoaded', function() {
    triggerScrollAnimations();
    
    // Add click handler to scroll navigation buttons
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetSection = this.getAttribute('onclick');
            if (targetSection.includes('rights')) {
                scrollToSection('rights');
            } else if (targetSection.includes('reflection')) {
                scrollToSection('reflection');
            } else if (targetSection.includes('print')) {
                printPage();
            }
        });
    });
});

// Handle keyboard shortcuts
document.addEventListener('keydown', function(event) {
    // Ctrl+P or Cmd+P for print
    if ((event.ctrlKey || event.metaKey) && event.key === 'p') {
        event.preventDefault();
        printPage();
    }
});

// Trigger animations on scroll
window.addEventListener('scroll', function() {
    triggerScrollAnimations();
});
