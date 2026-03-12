import os

keyword_files = ['Electric Service keywards.txt', 'cctv keywards.txt', 'school keywards.txt']
all_keywords = []

for f_name in keyword_files:
    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                k = line.strip()
                if k and not k.isnumeric() and len(k) > 3:
                    all_keywords.append(k)

unique_keywords = list(set(all_keywords))
unique_keywords = [k for k in unique_keywords if not (":" in k and k.split(":")[0].isdigit())]
keywords_comma_separated = ", ".join(unique_keywords)

seo_keywords_html = f"""
<div class="seo-footer-keywords" style="font-size: 10px; color: #888; text-align: justify; padding: 20px 10%; background: #1a1a24; word-wrap: break-word;">
    <strong>Service Areas & Keywords:</strong> {keywords_comma_separated}
</div>
"""

pages = [
    ('index.html', 'Electrician & Home Electrical Service in Unnao | Vijay Electronics', 'Best electrician, home electrical repair, CCTV installation, and smart school bell service in Unnao.'),
    ('about.html', 'About Us | Vijay Electronics Unnao', 'Learn about Vijay Electronics, your trusted provider for home electrical services, CCTV security, and smart school bell systems in Unnao.'),
    ('electrician-service.html', 'Professional Electrician Service in Unnao', 'Expert electrician services in Unnao. We handle all electrical repairs, installations, and maintenance.'),
    ('house-wiring-service.html', 'House Wiring Service in Unnao | Safe & Reliable', 'Complete house wiring and rewiring services in Unnao. Get safe, professional wiring solutions.'),
    ('electrical-repair-service.html', 'Electrical Repair Service in Unnao | 24/7 Experts', 'Fast and reliable electrical repair services in Unnao. Short circuit repair, switchboard fixing.'),
    ('cctv-installation.html', 'CCTV Camera Installation in Unnao | NVR & IP Setup', 'Top-rated CCTV installation in Unnao. Protect your property with advanced NVR and IP cameras.'),
    ('smart-school-bell-system.html', 'Smart School Bell System | Automatic Bell Timer Unnao', 'Automatic smart school bell systems with MP3, voice announcements, and IoT features.'),
    ('contact.html', 'Contact Us | Vijay Electronics Unnao', 'Contact Vijay Electronics for the best electrician, CCTV, and school bell services in Unnao.'),
    ('electrician-in-unnao.html', 'Best Electrician in Unnao | Local Electrical Experts', 'Looking for the best electrician in Unnao? We provide 24/7 emergency electrical services.'),
    ('home-electrical-repair-unnao.html', 'Home Electrical Repair Unnao | Fix Wiring & Appliances', 'Specialized in home electrical repair in Unnao. Doorstep service for fans, wiring, etc.'),
    ('house-wiring-service-unnao.html', 'House Wiring Service Unnao | Expert Contractors', 'Professional house wiring service in Unnao for new construction and renovation.'),
    ('faq.html', 'Frequently Asked Questions | Vijay Electronics Unnao', 'Find answers to common questions about our electrical, CCTV, and school bell services.')
]

def generate_header(active_page):
    return f"""
    <header class="header">
        <div class="container header-container">
            <a href="index.html" class="logo">
                <img src="logo.png" alt="Vijay Electronics Logo">
            </a>
            <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Menu">
                ☰
            </button>
            <nav class="nav" id="navMenu">
                <ul>
                    <li><a href="index.html" class="{'active' if active_page=='index.html' else ''}">Home</a></li>
                    <li><a href="about.html" class="{'active' if active_page=='about.html' else ''}">About</a></li>
                    <li class="dropdown">
                        <a href="javascript:void(0)" class="dropdown-toggle">Services <span class="arrow">▼</span></a>
                        <ul class="dropdown-menu">
                            <li><a href="electrician-service.html">Electrician Service</a></li>
                            <li><a href="house-wiring-service.html">House Wiring</a></li>
                            <li><a href="electrical-repair-service.html">Electrical Repair</a></li>
                            <li><a href="cctv-installation.html">CCTV Installation</a></li>
                            <li><a href="smart-school-bell-system.html">Smart School Bell</a></li>
                            <li><a href="electrician-in-unnao.html">Local Electician</a></li>
                            <li><a href="home-electrical-repair-unnao.html">Home Repair</a></li>
                        </ul>
                    </li>
                    <li><a href="faq.html" class="{'active' if active_page=='faq.html' else ''}">FAQ</a></li>
                    <li><a href="contact.html" class="{'active' if active_page=='contact.html' else ''}">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>
    """

footer_content = f"""
    <footer class="footer">
        <div class="container footer-content-grid">
            <div class="footer-col">
                <h3>Vijay Electronics</h3>
                <p>Your trusted local service provider in Unnao for all home electrical, CCTV security, and smart automation needs.</p>
                <div class="social-links">
                    <a href="https://www.instagram.com/vijayelectronics1" target="_blank">Instagram</a>
                    <a href="https://www.facebook.com/VijayChaurasiya" target="_blank">Facebook</a>
                    <a href="https://www.youtube.com/@vijayelectronics-v6e" target="_blank">YouTube</a>
                    <a href="https://x.com/unnao_vija41667" target="_blank">Twitter</a>
                </div>
            </div>
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                    <li><a href="faq.html">FAQ</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>Contact Info</h3>
                <p><strong>📞 Phone:</strong> +91 8090090051</p>
                <p><strong>📍 Location:</strong> Unnao, Uttar Pradesh</p>
                <p><strong>✉️ Email:</strong> contact@vijayelectronics.in</p>
            </div>
        </div>
        
        {seo_keywords_html}
        
        <div class="footer-bottom">
            <p>&copy; 2026 Vijay Electronics. All Rights Reserved.</p>
        </div>
    </footer>
    
    <div class="floating-ctas">
        <a href="tel:+918090090051" class="cta-call">📞 Call Us</a>
        <a href="https://wa.me/918090090051" class="cta-whatsapp" target="_blank">💬 WhatsApp</a>
    </div>
"""

for filename, title, desc in pages:
    page_specific_content = ""
    if filename == "index.html":
        page_specific_content = """
        <!-- Hero Video Section (Video Only, NO text) -->
        <section class="hero-video-wrapper">
            <video src="hero video.mp4" autoplay loop muted playsinline class="hero-video" id="heroVideo"></video>
        </section>
        
        <!-- Text below the Hero Video -->
        <section class="hero-text-section container">
            <h1 class="gradient-text">Best Electrician & Home Electrical Service in Unnao</h1>
            <p class="hero-subtitle">Professional House Wiring, Electrical Repair, CCTV Installation & Smart School Bell Systems.</p>
            <div class="trust-badges-container">
                <span class="trust-badge">✅ 100% Satisfaction</span>
                <span class="trust-badge">🛡️ Verified Experts</span>
                <span class="trust-badge">⚡ Fast Response</span>
            </div>
            <div class="hero-actions">
                <a href="tel:+918090090051" class="btn btn-primary pulse-anim">Book Service Now</a>
                <a href="contact.html" class="btn btn-outline">Contact Us</a>
            </div>
        </section>

        <!-- Services Preview -->
        <section class="services-preview container section-spacing">
            <h2 class="section-title text-center">Our Premium Services</h2>
            <div class="grid-cards mt-4">
                <div class="card glass-card">
                    <img src="home-electrician-service-unnao-india.png.png" alt="Home Electrician Service Unnao" loading="lazy">
                    <div class="card-body">
                        <h3>Home Electrician</h3>
                        <p>Complete home electrical solutions, switchboard repair, LED fitting, and wiring maintenance.</p>
                        <a href="electrician-service.html" class="btn-link">Learn More <span>→</span></a>
                    </div>
                </div>
                <div class="card glass-card">
                    <img src="Professional CCTV Camera Installation.png.png" alt="Professional CCTV Installation Unnao" loading="lazy">
                    <div class="card-body">
                        <h3>CCTV Installation</h3>
                        <p>High-quality NVR & DVR IP camera setup for homes, shops, and schools for maximum security.</p>
                        <a href="cctv-installation.html" class="btn-link">Learn More <span>→</span></a>
                    </div>
                </div>
                <div class="card glass-card">
                    <img src="smart-school-bell-system-india.png.png" alt="Smart School Bell System" loading="lazy">
                    <div class="card-body">
                        <h3>Smart School Bell</h3>
                        <p>Automatic smart timer bells with voice announcements for educational institutes.</p>
                        <a href="smart-school-bell-system.html" class="btn-link">Learn More <span>→</span></a>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="why-choose-us section-spacing container">
            <div class="flex-wrap align-center">
                <div class="flex-content">
                    <h2 class="section-title text-left">Why Choose Vijay Electronics?</h2>
                    <ul class="feature-list mt-4">
                        <li><strong>✓ Experienced Professionals:</strong> Highly trained and certified technicians.</li>
                        <li><strong>✓ Transparent Pricing:</strong> No hidden costs, affordable rates.</li>
                        <li><strong>✓ Fast Service:</strong> Quick response time within Unnao.</li>
                        <li><strong>✓ Genuine Parts:</strong> We use only premium electrical components.</li>
                    </ul>
                </div>
                <div class="flex-img text-center">
                    <img src="electric-repair-service-india.png.png" alt="Electric Repair Service" class="img-fluid rounded shadow" loading="lazy">
                </div>
            </div>
        </section>
        """
        
    elif "cctv" in filename:
        page_specific_content = """
        <div class="page-banner">
            <div class="container">
                <h1 class="gradient-text">Top-Rated CCTV Camera Installation in Unnao</h1>
            </div>
        </div>
        <section class="main-article container section-spacing">
            <div class="flex-wrap">
                <div class="article-text">
                    <h2>Protect Your Property with Advanced Security</h2>
                    <div class="ai-summary">
                        <h3>Key Takeaways:</h3>
                        <ul>
                            <li>High 1080p and 4K resolution camera setups.</li>
                            <li>Remote mobile viewing capability from anywhere via app.</li>
                            <li>Smart AI features like face detection and motion alerts.</li>
                            <li>Professional installation by certified experts.</li>
                        </ul>
                    </div>
                    <p>आज के समय में सुरक्षा (Security) हर घर, दुकान, ऑफिस, स्कूल और फैक्ट्री के लिए बहुत जरूरी हो गई है। हम NVR और IP Camera Security System का प्रोफेशनल इंस्टॉलेशन प्रदान करते हैं।</p>
                    
                    <h3>Our CCTV Services:</h3>
                    <ul class="styled-list">
                        <li>IP Camera Installation</li>
                        <li>DVR/NVR Setup</li>
                        <li>WiFi Camera Configuration</li>
                        <li>Maintenance and AMC Services</li>
                    </ul>
                </div>
                <div class="article-sidebar text-center">
                    <img src="NVR IP Camera Security System.png.png" alt="NVR IP Camera System" class="img-fluid rounded shadow mb-3" loading="lazy">
                    <img src="CCTV Camera Product Showcase.png" alt="CCTV Showcase" class="img-fluid rounded shadow" loading="lazy">
                </div>
            </div>
        </section>
        """
        
    elif "school" in filename:
        page_specific_content = """
        <div class="page-banner">
            <div class="container">
                <h1 class="gradient-text">Smart School Bell System Automation</h1>
            </div>
        </div>
        <section class="main-article container section-spacing">
            <div class="video-container shadow rounded mb-4" style="background:#000; overflow:hidden;">
                <!-- Using the provided smart school bell video -->
                <video src="smart school bell video.mp4" controls class="img-fluid" autoplay muted loop style="max-height:600px; width:100%; display:block;"></video>
            </div>
            
            <div class="flex-wrap mt-4">
                <div class="article-text">
                    <h2>Automate Your School's Schedule with AI Smart Bells</h2>
                    <div class="ai-summary">
                        <h3>Key Takeaways:</h3>
                        <ul>
                            <li>Fully automatic timer-based ringing.</li>
                            <li>Custom MP3 and voice announcements (Hindi/English).</li>
                            <li>Multi-schedule support (Summer, Winter, Exams).</li>
                            <li>Smartphone and app control support.</li>
                        </ul>
                    </div>
                    <p>We provide the best automatic school bell systems in Unnao. Perfect for schools, colleges, and factories to easily manage periods and shifts with zero human error.</p>
                </div>
                <div class="article-sidebar text-center">
                    <img src="school bell img.png" alt="School Bell Image" class="img-fluid rounded shadow mb-3" loading="lazy">
                    <img src="smart school voice bell .png.png" alt="Smart Voice Bell" class="img-fluid rounded shadow" loading="lazy">
                </div>
            </div>
        </section>
        """
        
    elif "contact" in filename or "about" in filename:
        title_text = "Contact Us" if "contact" in filename else "About Us"
        page_specific_content = f"""
        <div class="page-banner">
            <div class="container">
                <h1 class="gradient-text">{title_text}</h1>
            </div>
        </div>
        <section class="container section-spacing text-center main-article mt-4">
            <h2>Vijay Electronics</h2>
            <p class="mt-3" style="font-size: 1.2rem; color: #555;">Your premium and reliable service partner in Unnao for electrician services, CCTV setups, and smart automation.</p>
            <div class="mt-4" style="padding: 20px; background: #f8fafc; border-radius: 12px; display: inline-block;">
                <p style="font-size: 1.4rem;"><strong>Mobile:</strong> <a href="tel:+918090090051" style="color: #2563EB; text-decoration:none;">+91 8090090051</a></p>
                <div style="margin-top: 20px; display: flex; gap: 15px; justify-content: center;">
                    <a href="tel:+918090090051" class="btn btn-primary pulse-anim">Call Now</a>
                    <a href="https://wa.me/918090090051" target="_blank" class="btn" style="background: #25d366; color: white;">WhatsApp</a>
                </div>
            </div>
            <br>
            <img src="logo.png" alt="Vijay Electronics Logo" class="mt-4" style="max-width: 200px;">
        </section>
        """
        
    else:
        page_specific_content = f"""
        <div class="page-banner">
            <div class="container">
                <h1 class="gradient-text">{title.split('|')[0]}</h1>
            </div>
        </div>
        <section class="main-article container section-spacing mt-4">
            <div class="flex-wrap">
                <div class="article-text">
                    <h2>Reliable and Safe Electrical Services in Unnao</h2>
                    <div class="ai-summary">
                        <h3>Key Takeaways:</h3>
                        <ul>
                            <li>Expert electrical repair and new installation.</li>
                            <li>House wiring, switchboard fixing, and appliance setup.</li>
                            <li>Safety-first approach using certified tools.</li>
                            <li>Fast doorstep service anywhere in Unnao.</li>
                        </ul>
                    </div>
                    <p>घर की लाइट, पंखा, कूलर, टीवी, और सुरक्षा सिस्टम सब बिजली पर निर्भर करते हैं। Vijay Electronics provides top-notch home electrical repair, wiring, and servicing to ensure your appliances run smoothly and safely without short circuits.</p>
                    
                    <h3>What We Cover:</h3>
                    <ul class="styled-list">
                        <li>Complete House Wiring Installation</li>
                        <li>Fan, Tube Light, and LED Fitting</li>
                        <li>Inverter and Generator Setup</li>
                        <li>MCB, ELCB & Distribution Board Fixing</li>
                        <li>Earthing Work & Short Circuit Repair</li>
                    </ul>
                </div>
                <div class="article-sidebar text-center">
                    <img src="house-wiring-electrician-unnao.png.png" alt="Electrician Work Unnao" class="img-fluid rounded shadow mb-3" loading="lazy">
                    <img src="electrical-maintenance-service-unnao.png.png" alt="Electrical Maintenance Unnao" class="img-fluid rounded shadow" loading="lazy">
                </div>
            </div>
        </section>
        """

    if filename == "faq.html":
        page_specific_content = """
        <div class="page-banner">
            <div class="container">
                <h1 class="gradient-text">Frequently Asked Questions</h1>
            </div>
        </div>
        <section class="faq-container container section-spacing" itemscope itemtype="https://schema.org/FAQPage">
            <!-- FAQ 1 -->
            <div class="faq-card" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                <div class="faq-question">
                    <h3 itemprop="name">What areas in Unnao do you serve?</h3>
                    <span class="icon" style="font-size: 24px;">+</span>
                </div>
                <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">We provide professional electrical and CCTV services across all major areas in Unnao including Awas Vikas, Civil Lines, Kalyani, Shuklaganj, and surrounding regions.</p>
                </div>
            </div>
            <!-- FAQ 2 -->
            <div class="faq-card" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                <div class="faq-question">
                    <h3 itemprop="name">Do you provide emergency electrician services?</h3>
                    <span class="icon" style="font-size: 24px;">+</span>
                </div>
                <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">Yes, we understand electrical issues can occur anytime. Contact us at 8090090051 for emergency quick response.</p>
                </div>
            </div>
            <!-- FAQ 3 -->
            <div class="faq-card" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                <div class="faq-question">
                    <h3 itemprop="name">What types of CCTV cameras do you install?</h3>
                    <span class="icon" style="font-size: 24px;">+</span>
                </div>
                <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">We setup both DVR and modern NVR IP Camera systems from top brands like CP Plus, Hikvision, and Dahua.</p>
                </div>
            </div>
            <!-- FAQ 4 -->
            <div class="faq-card" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                <div class="faq-question">
                    <h3 itemprop="name">How does the smart school bell system work?</h3>
                    <span class="icon" style="font-size: 24px;">+</span>
                </div>
                <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                    <p itemprop="text">It operates automatically based on a pre-programmed schedule. The system connects to speakers and can play regular ring tones, voice announcements, or prayers at precise times without manual intervention.</p>
                </div>
            </div>
        </section>
        """
        
    schema_script = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Vijay Electronics",
      "image": "https://raw.githubusercontent.com/vijay-unnao/site/main/logo.png",
      "@id": "https://vijayelectronics.in",
      "url": "https://vijayelectronics.in",
      "telephone": "+91 8090090051",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Unnao City",
        "addressLocality": "Unnao",
        "addressRegion": "UP",
        "postalCode": "209801",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 26.5393,
        "longitude": 80.4878
      },
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
          "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        "opens": "00:00",
        "closes": "23:59"
      }
    }
    </script>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Electrical Services & CCTV Installation",
        "provider": {
            "@type": "LocalBusiness",
            "name": "Vijay Electronics Unnao"
        }
    }
    </script>
"""

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <!-- All exact user keywords injected automatically -->
    <meta name="keywords" content="{keywords_comma_separated}">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Outfit:wght@400;700&display=swap" rel="stylesheet">
    {schema_script}
</head>
<body>
    {generate_header(filename)}
    
    <main class="fade-in">
        {page_specific_content}
    </main>

    {footer_content}

    <script src="script.js" defer></script>
</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as pf:
        pf.write(html_template)

css_content = """
:root {
    --primary: #2563EB;
    --primary-hover: #1D4ED8;
    --secondary: #F59E0B;
    --gradient-start: #1E3A8A;
    --gradient-end: #3B82F6;
    --dark: #0F172A;
    --darker: #020617;
    --light: #F8FAFC;
    --background: #EFF6FF;
    --white: #ffffff;
    --text: #334155;
    --text-light: #64748B;
    --radius: 12px;
    --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
body { background-color: var(--background); color: var(--text); line-height: 1.6; overflow-x: hidden; }
h1, h2, h3, h4 { font-family: 'Outfit', sans-serif; color: var(--dark); line-height: 1.2; }
.container { width: 90%; max-width: 1280px; margin: 0 auto; }
.section-spacing { padding: 80px 0; }
.text-center { text-align: center; }
.mt-3 { margin-top: 1rem; }
.mt-4 { margin-top: 1.5rem; }
.mb-3 { margin-bottom: 1rem; }
.mb-4 { margin-bottom: 1.5rem; }
img.img-fluid { max-width: 100%; height: auto; display: block; margin: 0 auto; }
.rounded { border-radius: var(--radius); }
.shadow { box-shadow: var(--shadow); }

.btn { display: inline-flex; align-items: center; justify-content: center; padding: 14px 32px; font-size: 1.1rem; font-weight: 600; border-radius: 50px; cursor: pointer; transition: all 0.3s ease; text-decoration: none; border: none; }
.btn-primary { background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end)); color: var(--white); box-shadow: 0 4px 14px 0 rgba(37, 99, 235, 0.39); }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5); }
.btn-outline { background: transparent; border: 2px solid var(--primary); color: var(--primary); }
.btn-outline:hover { background: var(--primary); color: var(--white); }

.header { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }
.header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; }
.logo img { height: 60px; width: auto; }
.nav ul { list-style: none; display: flex; align-items: center; gap: 24px; }
.nav a { text-decoration: none; color: var(--text); font-weight: 600; font-size: 1rem; transition: color 0.2s ease; }
.nav a:hover, .nav a.active { color: var(--primary); }

.dropdown { position: relative; }
.dropdown-menu { position: absolute; top: 150%; left: 0; background: var(--white); min-width: 220px; border-radius: 8px; box-shadow: var(--shadow); opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.3s ease; flex-direction: column; padding: 10px 0; z-index: 100; }
.dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
.dropdown-menu li { padding: 0; }
.dropdown-menu a { padding: 10px 20px; display: block; font-weight: 400; }
.dropdown-menu a:hover { background: var(--background); }
.mobile-menu-btn { display: none; background: transparent; border: none; color: var(--dark); font-size: 28px; cursor: pointer; }

/* Hero sections */
.hero-video-wrapper { width: 100%; background: #000; }
.hero-video { width: 100%; height: auto; max-height: 70vh; object-fit: cover; display: block; margin: 0 auto; }
.hero-text-section { padding: 60px 20px 40px; text-align: center; background: var(--white); border-radius: 20px; margin-top: -30px; position: relative; z-index: 10; box-shadow: var(--shadow); }
.page-banner { background: var(--white); padding: 60px 0 40px; text-align: center; border-bottom: 1px solid rgba(0,0,0,0.05); }
.gradient-text { background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem; font-weight: 800; margin-bottom: 20px; }
.hero-subtitle { font-size: 1.25rem; color: var(--text-light); max-width: 800px; margin: 0 auto 30px; }
.trust-badges-container { display: flex; justify-content: center; flex-wrap: wrap; gap: 15px; margin-bottom: 40px; }
.trust-badge { background: var(--background); color: var(--primary); padding: 8px 20px; border-radius: 20px; font-weight: 600; font-size: 0.95rem; border: 1px solid rgba(37,99,235,0.1); }
.hero-actions { display: flex; gap: 20px; justify-content: center; }

/* Cards & Text content */
.grid-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; }
.glass-card { background: rgba(255, 255, 255, 0.95); border: 1px solid rgba(255,255,255,0.5); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); transition: transform 0.4s; }
.glass-card:hover { transform: translateY(-10px); }
.glass-card img { width: 100%; height: 220px; object-fit: cover; border-bottom: 1px solid rgba(0,0,0,0.05); }
.card-body { padding: 24px; }
.card-body h3 { font-size: 1.5rem; margin-bottom: 12px; color: var(--dark); }
.btn-link { display: inline-block; margin-top: 15px; color: var(--primary); font-weight: 600; text-decoration: none; font-size: 1.05rem; }
.btn-link:hover { color: var(--primary-hover); }

.main-article { background: var(--white); border-radius: var(--radius); padding: 40px; box-shadow: var(--shadow); position: relative; z-index: 5; }
.flex-wrap { display: flex; flex-wrap: wrap; gap: 40px; }
.flex-content, .article-text { flex: 1 1 500px; }
.flex-img, .article-sidebar { flex: 1 1 400px; }
.ai-summary { background: var(--background); padding: 20px; border-left: 5px solid var(--primary); border-radius: 0 var(--radius) var(--radius) 0; margin: 25px 0; }
.ai-summary ul { margin-left: 20px; margin-top: 10px; }
.styled-list { list-style: none; margin-top: 15px; }
.styled-list li { position: relative; padding-left: 30px; margin-bottom: 10px; font-size: 1.05rem; }
.styled-list li::before { content: '⚡'; position: absolute; left: 0; color: var(--secondary); }
.feature-list { list-style: none; margin-top: 20px; }
.feature-list li { font-size: 1.1rem; margin-bottom: 15px; padding: 15px; background: var(--background); border-radius: 8px; }

/* FAQ */
.faq-container { max-width: 800px; margin: 40px auto; }
.faq-card { background: var(--white); margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid #e2e8f0; }
.faq-question { padding: 20px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 600; color: var(--dark); user-select: none; }
.faq-question:hover { background: var(--background); }
.faq-answer { padding: 0 20px 20px; display: none; color: var(--text-light); border-top: 1px solid #eee; padding-top: 15px; }

/* Animations */
.fade-in { animation: fadeIn 0.8s ease-in; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.pulse-anim { animation: pulse 2s infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.4); } 70% { box-shadow: 0 0 0 15px rgba(37, 99, 235, 0); } 100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); } }

/* Footer */
.footer { background: var(--darker); color: var(--white); padding: 60px 0 0; margin-top: 60px; }
.footer-content-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; margin-bottom: 40px; }
.footer-col h3 { color: var(--secondary); margin-bottom: 20px; }
.footer-col a { color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 10px; transition: color 0.3s; }
.footer-col a:hover { color: var(--primary); }
.social-links { display: flex; gap: 15px; flex-wrap: wrap; margin-top: 20px; }
.social-links a { background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 5px; display: inline-block; color: white; }
.social-links a:hover { background: var(--primary); }
.footer-bottom { background: #000; text-align: center; padding: 20px; font-size: 0.9rem; color: #64748B; }

.seo-footer-keywords { max-height: 150px; overflow-y: auto; scrollbar-width: thin; }

/* Fixed CTAs */
.floating-ctas { position: fixed; bottom: 30px; right: 30px; display: flex; flex-direction: column; gap: 15px; z-index: 999; }
.floating-ctas a { text-decoration: none; color: white; padding: 14px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); text-align: center; transition: all 0.3s; }
.floating-ctas a:hover { transform: translateY(-3px) scale(1.05); }
.cta-call { background: var(--primary); }
.cta-whatsapp { background: #25d366; }

/* Responsive */
@media (max-width: 768px) {
    .nav { position: absolute; top: 100%; left: 0; width: 100%; background: var(--white); flex-direction: column; padding: 20px; box-shadow: var(--shadow); border-top: 1px solid #eee; display: none; }
    .nav.show { display: flex; }
    .nav ul { flex-direction: column; width: 100%; gap: 15px; }
    .nav ul li { width: 100%; border-bottom: 1px solid #f1f5f9; padding-bottom: 10px; }
    .mobile-menu-btn { display: block; }
    .dropdown-menu { position: static; box-shadow: none; opacity: 1; visibility: visible; transform: none; display: none; margin-top: 10px; background: var(--background); }
    .dropdown.active .dropdown-menu { display: flex; }
    .gradient-text { font-size: 2rem; }
    .hero-text-section { padding: 40px 15px; margin-top: -20px; margin-left:10px; margin-right: 10px; }
    .hero-actions { flex-direction: column; }
    .main-article { padding: 25px 15px; margin-top:-20px; margin-left:10px; margin-right: 10px;}
    .floating-ctas { bottom: 20px; right: 20px; }
    .floating-ctas a { padding: 12px 18px; font-size: 0.9rem; }
}
"""
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

js_content = """
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
"""
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated HTML, CSS, JS")
