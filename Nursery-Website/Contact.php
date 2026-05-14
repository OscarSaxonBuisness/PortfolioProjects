<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Sylvia’s Happy Childcare — About Us</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;600;700&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">


    <!-- ✨ Shared animations & interactions for all pages -->
  <style>
        h1, h2, h3, h4, h5, h6, nav a, button {
  font-family: 'Josefin Sans', sans-serif;
}
    /* Smooth scrolling */
    html {
      scroll-behavior: smooth;
    }

    /* Animated nav links (no change needed to your existing <a> tags) */
    header nav a {
      position: relative;
      padding: 4px 2px;
      border-radius: 999px;
      transition:
        transform 0.18s ease,
        box-shadow 0.18s ease,
        background-color 0.18s ease;
    }

    header nav a::after {
      content: "";
      position: absolute;
      left: 12px;
      right: 12px;
      bottom: -4px;
      height: 2px;
      border-radius: 999px;
      background: #44B7AE;
      transform: scaleX(0);
      transform-origin: center;
      transition: transform 0.2s ease;
      opacity: 0.9;
    }

    header nav a:hover,
    header nav a:focus-visible {
      transform: translateY(-1px) scale(1.03);
      background: rgba(68, 183, 174, 0.08);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
      outline: none;
    }

    header nav a:hover::after,
    header nav a:focus-visible::after {
      transform: scaleX(1);
    }

    /* Gentle floating animation for slideshow images (works on any page with #slides) */
    #slides img {
      transform-origin: center;
      animation: heroFloat 22s ease-in-out infinite;
    }

    @keyframes heroFloat {
      0%   { transform: scale(1.02) translate3d(0, 0, 0); }
      50%  { transform: scale(1.07) translate3d(0, -8px, 0); }
      100% { transform: scale(1.02) translate3d(0, 0, 0); }
    }

    /* Hero title card pop-in + wiggle (JS will add these classes) */
    .hero-title-card {
      will-change: transform, box-shadow, opacity;
      transform: translateY(18px) scale(0.97);
      opacity: 0;
      transition:
        opacity 0.7s ease-out,
        transform 0.7s ease-out,
        box-shadow 0.7s ease-out;
    }

    .hero-title-card.hero-visible {
      opacity: 1;
      transform: translateY(0) scale(1);
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.14);
    }

    .hero-title-card.hero-wiggle {
      animation: heroWiggle 2.2s ease-in-out infinite;
    }

    @keyframes heroWiggle {
      0%, 100% { transform: translateY(0) scale(1); }
      45%      { transform: translateY(-3px) rotate(-0.6deg) scale(1.01); }
      55%      { transform: translateY(-3px) rotate(0.6deg) scale(1.01); }
    }

    /* Scroll reveal for all content sections (except the hero banner) */
    .reveal-section {
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }

    .reveal-section.reveal-visible {
      opacity: 1;
      transform: translateY(0);
    }

    /* Cute hover for the footer animal row */
    footer img[alt*="Animal Row"] {
      transition: transform 0.35s ease;
    }
    footer img[alt*="Animal Row"]:hover {
      transform: translateY(-4px) rotate(-1.5deg) scale(1.03);
    }
  </style>

  <script>
    window.addEventListener('DOMContentLoaded', function () {
      // 1. Tiny nav tweak so hovered link sits above neighbours
      var navLinks = document.querySelectorAll('header nav a');
      navLinks.forEach(function (link) {
        link.addEventListener('mouseenter', function () {
          link.style.zIndex = '1';
        });
        link.addEventListener('mouseleave', function () {
          link.style.zIndex = '';
        });
      });

      // 2. Hero title card: find the existing card and animate it
      var heroCard = document.querySelector('#hero div[style*="pointer-events:auto"]');
      if (heroCard) {
        heroCard.classList.add('hero-title-card');
        // Pop in
        setTimeout(function () {
          heroCard.classList.add('hero-visible');
        }, 150);
        // Gentle wiggle after it has appeared
        setTimeout(function () {
          heroCard.classList.add('hero-wiggle');
        }, 1200);
      }

      // 3. Scroll reveal for every <section> except the hero
      var sections = Array.prototype.slice.call(document.querySelectorAll('section'))
        .filter(function (sec) { return sec.id !== 'hero'; });

      if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('reveal-visible');
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.15 });

        sections.forEach(function (sec) {
          sec.classList.add('reveal-section');
          observer.observe(sec);
        });
      } else {
        // Old browsers: just show everything
        sections.forEach(function (sec) {
          sec.classList.add('reveal-visible');
        });
      }

      // 4. Fun hover effect for slideshow dots (if the page has them)
      var dots = document.querySelectorAll('#dots button');
      dots.forEach(function (dot) {
        dot.style.transition = 'transform 0.2s ease, box-shadow 0.2s ease';
        dot.addEventListener('mouseenter', function () {
          dot.style.transform = 'scale(1.4)';
          dot.style.boxShadow = '0 0 0 4px rgba(255,255,255,0.35)';
        });
        dot.addEventListener('mouseleave', function () {
          dot.style.transform = '';
          dot.style.boxShadow = '';
        });
      });
    });
  </script>

</head>

<body style="margin:0; font-family:'Montserrat', sans-serif; color:#44B7AE;">

<header 
  style="position:sticky; top:0; z-index:100; background:#ffffff; 
         box-shadow:0 1px 6px #6F6158; border-bottom:2px solid #6F6158;">
  <nav 
    style="max-width:1200px; margin:0 auto; display:flex; align-items:center; 
           justify-content:space-between; padding:20px 0px;">

    <!-- LOGO (LEFT) -->
    <a href="index.html" 
       style="display:flex; align-items:center; text-decoration:none; color:inherit;">
      <img src="Images/ChildcareMainLogo.png" 
           alt="Sylvia’s Happy Childcare Logo" 
           style="height:72px; width:auto; margin-right:12px;">
    </a>

    <!-- NAV LINKS (CENTER) -->
    <div style="flex:1; display:flex; justify-content:center; gap:30px;">
      <a href="index.html" style="text-decoration:none; color:#6F6158; font-weight:500; font-size:20px;">Home</a>
      <a href="AboutUs.html" style="text-decoration:none; color:#6F6158; font-weight:500; font-size:20px;">About us</a>
      <a href="Reviews.html" style="text-decoration:none; color:#6F6158; font-weight:500; font-size:20px;">Gallery & Reviews</a>
      <a href="Ofsted.html" style="text-decoration:none; color:#6F6158; font-weight:500; font-size:20px;">Ofsted</a>
      <a href="Contact.php" style="text-decoration:none; color:#44B7AE; font-weight:500; font-size:20px;">Contact Us</a>
    </div>

    <!-- LOGIN BUTTON (RIGHT, IMAGE) -->
    <div>
      <a href="login.html" style="display:inline-block;">
        <img src="Images/LogInButton.jpg" 
             alt="Log In" 
             style="height:72px; width:auto; display:block;">
      </a>
    </div>

  </nav>
</header>

<!-- ===== CONTENT ===== -->
<section style="background:#F9F6EE; border-bottom:2px solid #6F6158; padding:40px 0;">
  <div style="max-width:1000px; margin:0 auto; padding:0 16px;">

    <!-- Heading + intro -->
    <h2 style="margin:0 0 20px; font-size:32px; color:#44B7AE; text-align:center;">
      Contact Us
    </h2>

    <p style="text-align:center; max-width:750px; margin:0 auto 30px;
              font-size:18px; color:#6F6158; line-height:1.6;">
      Have any questions or would like to book a visit? Please contact us directly — we’d love to hear from you.
    </p>

    <!-- Contact details box -->
    <div style="background:#ffffff; border:1px solid #E7E2DA; border-radius:16px;
                box-shadow:0 4px 12px rgba(0,0,0,.06); padding:30px;
                max-width:700px; margin:0 auto 40px; text-align:center;">
      <h3 style="color:#44B7AE; margin-top:0; margin-bottom:12px;">Our Nursery</h3>
      <p style="margin:6px 0; color:#6F6158;">
        <strong>Address:</strong> 131 Salusbury Road, London NW6 6RG
      </p>
      <p style="margin:6px 0; color:#6F6158;">
        <strong>Phone:</strong>
        <a href="tel:+441234567890" style="color:#44B7AE; text-decoration:none;">
          01234 567 890
        </a>
      </p>
      <p style="margin:6px 0; color:#6F6158;">
        <strong>Email:</strong>
        <a href="mailto:info@sylviashappychildcare.co.uk"
           style="color:#44B7AE; text-decoration:none;">
          info@sylviashappychildcare.co.uk
        </a>
      </p>
    </div>

    <!-- Contact Form -->
<div style="background:#ffffff; border:1px solid #E7E2DA; border-radius:16px;
            box-shadow:0 4px 12px rgba(0,0,0,.06); padding:30px;
            max-width:700px; margin:0 auto 40px;">

  <h3 style="color:#44B7AE; margin-top:0; margin-bottom:20px; text-align:center;">
    Arrange a Visit
  </h3>

  <form action="send-email.php" method="POST" style="display:flex; flex-direction:column; gap:15px;">

    <input type="text" name="fullname" placeholder="Full Name" required
           style="padding:12px; border-radius:8px; border:1px solid #E7E2DA; font-size:16px;">

    <input type="email" name="email" placeholder="Email Address" required
           style="padding:12px; border-radius:8px; border:1px solid #E7E2DA; font-size:16px;">

    <textarea name="message" rows="6" placeholder="Please let us know when you would like to visit..."
              required
              style="padding:12px; border-radius:8px; border:1px solid #E7E2DA; font-size:16px;"></textarea>

    <button type="submit"
            style="background:#44B7AE; color:white; border:none; padding:14px;
                   border-radius:8px; font-size:16px; cursor:pointer;">
      Send Enquiry
    </button>

  </form>
</div>


    <!-- Map box -->
    <div style="background:#ffffff; border:1px solid #E7E2DA; border-radius:16px;
                box-shadow:0 4px 12px rgba(0,0,0,.06); padding:30px;
                max-width:700px; margin:0 auto 40px; text-align:center;">
      <h3 style="color:#44B7AE; margin-top:0; margin-bottom:12px;">Find Us</h3>
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d19843.50134797816!2d-0.21157054999999998!3d51.53422395!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761a9f1c81d7d3%3A0x3f3a0e7cdbb52c9e!2s131%20Salusbury%20Rd%2C%20London%20NW6%206RG!5e0!3m2!1sen!2suk!4v1730751600000!5m2!1sen!2suk"
        width="100%" height="300"
        style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy">
      </iframe>
    </div>

  </div>
</section>
    <!-- ===== FOOTER ===== -->
  <footer style="text-align:center; background:#ffffff; padding:40px 16px;">
    <!-- Cute animal logo row -->
    <div>
      <img src="Images/FooterGraphic.png" alt="Animal Row Illustration" 
           style="max-width:220px; height:auto; margin-bottom:10px;">
    </div>

    <!-- Slogan -->
    <h3 style="font-family:'Comic Neue', 'Patrick Hand', cursive; 
               font-weight:400; 
               font-size:22px; 
               margin:10px 0 6px; 
               color:#6F6158;">
      Learn, Play And Explore With Us
    </h3>

    <!-- Company info -->
    <p style="font-size:13px; color:#6F6158; max-width:700px; margin:10px auto 0;">
      Sylvia’s Happy Childcare Limited is registered in England and Wales No. 9383717<br>
      Registered Address: 131 Salusbury Road, London NW6 6RG
    </p>
  </footer>

  <!-- ===== SLIDESHOW SCRIPT ===== -->
  <script>
    (function () {
      // Get slides and dots
      const slides = Array.from(document.querySelectorAll('#slides .slide'));
      const dots   = Array.from(document.querySelectorAll('#dots button'));
      let i = 0, timer = null;

      // Show selected slide
      function show(n, manual) {
        i = (n + slides.length) % slides.length;
        slides.forEach((el, idx) => el.style.opacity = idx === i ? '1' : '0');
        dots.forEach((d, idx) => d.style.background = idx === i ? 'rgba(255,255,255,.9)' : 'rgba(255,255,255,.5)');
        if (!manual) restart();
      }

      // Go to next slide
      function next() { show(i + 1); }

      // Auto slideshow
      function restart() { clearInterval(timer); timer = setInterval(next, 4500); }

      // Manual slide selection
      dots.forEach(d => d.addEventListener('click', () => { show(+d.dataset.index, true); restart(); }));

      // Initialize slideshow
      show(0);
      restart();

      // Prevent horizontal scrollbars
      document.documentElement.style.overflowX = 'hidden';
      document.body.style.overflowX = 'hidden';
    })();
  </script>
</body>
</html>
