// jctjzhinan.xyz Client JavaScript Utilities

document.addEventListener('DOMContentLoaded', function() {
  // Mobile Nav Drawer Toggle
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const closeBtn = document.getElementById('mobile-menu-close');
  const drawer = document.getElementById('mobile-nav-menu');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', function() {
      drawer.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      toggleBtn.setAttribute('aria-expanded', 'true');
    });
  }

  if (closeBtn && drawer) {
    closeBtn.addEventListener('click', function() {
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      toggleBtn.setAttribute('aria-expanded', 'false');
    });
  }

  // Coupon Copy Functionality
  const copyButtons = document.querySelectorAll('.btn-copy-coupon');
  copyButtons.forEach(button => {
    button.addEventListener('click', function() {
      const couponCode = this.getAttribute('data-coupon');
      if (couponCode) {
        navigator.clipboard.writeText(couponCode).then(() => {
          const originalText = this.innerText;
          this.innerText = '已复制!';
          this.style.background = '#86efac';
          setTimeout(() => {
            this.innerText = originalText;
            this.style.background = '';
          }, 2000);
        }).catch(err => {
          console.error('Failed to copy: ', err);
        });
      }
    });
  });

  // Track Affiliate Clicks
  const affLinks = document.querySelectorAll('a[rel*="sponsored"]');
  affLinks.forEach(link => {
    link.addEventListener('click', function() {
      const href = this.getAttribute('href');
      if (window.gtag) {
        window.gtag('event', 'affiliate_click', {
          'event_category': 'outbound',
          'event_label': href,
          'transport_type': 'beacon'
        });
      }
    });
  });
});
