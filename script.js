// ===========================
// ESSENZA - JavaScript
// Interactive Features
// ===========================

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ===========================
    // MOBILE NAVIGATION TOGGLE
    // ===========================
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Toggle mobile menu
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
            
            // Prevent body scroll when menu is open
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });
    }

    // Close mobile menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // ===========================
    // DROPDOWN NAVIGATION (MOBILE)
    // ===========================
    const navDropdowns = document.querySelectorAll('.nav-dropdown');
    
    navDropdowns.forEach(dropdown => {
        const dropdownLink = dropdown.querySelector('.nav-link');
        
        dropdownLink.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    });

    // ===========================
    // SMOOTH SCROLLING
    // ===========================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ===========================
    // HEADER SCROLL EFFECT
    // ===========================
    const header = document.querySelector('.header');
    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        // Add shadow on scroll
        if (currentScroll > 100) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.15)';
        } else {
            header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        }

        lastScroll = currentScroll;
    });

    // ===========================
    // FORM VALIDATION & SUBMISSION
    // ===========================
    
    // Customization Form
    const customizationForm = document.getElementById('customizationForm');
    if (customizationForm) {
        customizationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                product: document.getElementById('product').value,
                preferences: document.getElementById('preferences').value
            };

            // Validate form
            if (validateForm(formData)) {
                // Show success message
                showNotification('¡Solicitud enviada! Nos pondremos en contacto contigo pronto.', 'success');
                
                // Reset form
                customizationForm.reset();
                
                // In a real application, you would send this data to a server
                console.log('Customization request:', formData);
            }
        });
    }

    // Contact Form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = {
                name: document.getElementById('contact-name').value,
                email: document.getElementById('contact-email').value,
                subject: document.getElementById('subject').value,
                message: document.getElementById('message').value
            };

            // Validate form
            if (validateForm(formData)) {
                // Show success message
                showNotification('¡Mensaje enviado! Te responderemos pronto.', 'success');
                
                // Reset form
                contactForm.reset();
                
                // In a real application, you would send this data to a server
                console.log('Contact message:', formData);
            }
        });
    }

    // Newsletter Form
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = this.querySelector('input[type="email"]').value;
            
            if (validateEmail(email)) {
                showNotification('¡Gracias por suscribirte!', 'success');
                this.reset();
                console.log('Newsletter subscription:', email);
            } else {
                showNotification('Por favor, ingresa un email válido.', 'error');
            }
        });
    }

    // ===========================
    // VALIDATION FUNCTIONS
    // ===========================
    
    function validateForm(data) {
        // Check if all required fields are filled
        for (let key in data) {
            if (!data[key] || data[key].trim() === '') {
                showNotification('Por favor, completa todos los campos.', 'error');
                return false;
            }
        }

        // Validate email
        if (data.email && !validateEmail(data.email)) {
            showNotification('Por favor, ingresa un email válido.', 'error');
            return false;
        }

        return true;
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // ===========================
    // NOTIFICATION SYSTEM
    // ===========================
    
    function showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotification = document.querySelector('.notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;

        // Style the notification
            notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            padding: 1rem 2rem;
            background-color: ${type === 'success' ? '#790000' : '#d32f2f'};
            color: white;
            border-radius: 4px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            z-index: 10000;
            animation: slideIn 0.3s ease-out;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.95rem;
            max-width: 400px;
        `;        // Add animation styles
        if (!document.querySelector('#notification-styles')) {
            const style = document.createElement('style');
            style.id = 'notification-styles';
            style.textContent = `
                @keyframes slideIn {
                    from {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                @keyframes slideOut {
                    from {
                        transform: translateX(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }

        // Add to page
        document.body.appendChild(notification);

        // Remove after 5 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 5000);
    }

    // ===========================
    // SCROLL ANIMATIONS
    // ===========================
    
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.product-card, .feature, .store-card');
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(element);
    });

    // ===========================
    // PRODUCT CARD INTERACTIONS
    // ===========================
    
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.zIndex = '10';
        });

        card.addEventListener('mouseleave', function() {
            this.style.zIndex = '1';
        });
    });

    // ===========================
    // ACTIVE NAVIGATION LINK
    // ===========================
    
    // Highlight active section in navigation
    const sections = document.querySelectorAll('section[id]');
    
    function highlightNavigation() {
        const scrollPosition = window.pageYOffset + 150;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => link.classList.remove('active'));
                if (navLink) {
                    navLink.classList.add('active');
                    navLink.style.color = '#790000';
                }
            }
        });
    }

    // Add active style
    const style = document.createElement('style');
    style.textContent = `
        .nav-link.active::after {
            width: 100%;
        }
    `;
    document.head.appendChild(style);

    window.addEventListener('scroll', highlightNavigation);

    // ===========================
    // IMAGE LAZY LOADING FALLBACK
    // ===========================
    
    // For browsers that don't support native lazy loading
    if ('loading' in HTMLImageElement.prototype) {
        // Native lazy loading is supported
        console.log('Native lazy loading supported');
    } else {
        // Fallback for browsers that don't support lazy loading
        const images = document.querySelectorAll('img[loading="lazy"]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.add('loaded');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    // ===========================
    // CONSOLE MESSAGE
    // ===========================
    
    console.log('%cESSENZA', 'font-size: 24px; font-weight: bold; color: #790000;');
    console.log('%cBellezza Italiana', 'font-size: 14px; font-style: italic; color: #6B6B6B;');
    console.log('Website loaded successfully');
});

// ===========================
// UTILITY FUNCTIONS
// ===========================

// Debounce function for performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ===========================
// 3D IMAGE EFFECT - Mouse Tracking
// ===========================
document.querySelectorAll('.product-card').forEach(card => {
    const productImage = card.querySelector('.product-3d');
    
    if (productImage) {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Calculate rotation based on mouse position
            const rotateX = ((y - centerY) / centerY) * -15;
            const rotateY = ((x - centerX) / centerX) * 15;
            
            const img = productImage.querySelector('img');
            if (img) {
                img.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.08)`;
                img.style.transition = 'transform 0.1s ease-out';
            }
            
            // Move the shine effect to follow mouse
            const percentX = (x / rect.width) * 100;
            const percentY = (y / rect.height) * 100;
            
            const shineElement = productImage.querySelector('::after');
            if (productImage) {
                productImage.style.setProperty('--mouse-x', `${percentX}%`);
                productImage.style.setProperty('--mouse-y', `${percentY}%`);
            }
            
            // Dynamic shadow based on tilt
            const shadowX = rotateY * 2;
            const shadowY = -rotateX * 2;
            card.style.boxShadow = `${shadowX}px ${shadowY}px 40px rgba(0, 0, 0, 0.3)`;
            
            // Add parallax effect to card
            card.style.transform = `translateZ(20px)`;
        });
        
        card.addEventListener('mouseleave', () => {
            const img = productImage.querySelector('img');
            if (img) {
                img.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
                img.style.transition = 'transform 0.6s cubic-bezier(0.23, 1, 0.32, 1)';
            }
            card.style.transform = 'translateZ(0)';
            card.style.boxShadow = '';
        });
    }
});

