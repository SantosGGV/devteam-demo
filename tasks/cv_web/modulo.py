from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def read_root():
    html_content = """
    <html>
        <head>
            <title>Santos Gómez - Field IT Specialist</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: Arial, sans-serif; background-color: #1a1a2e; color: #eee; }
                .navbar { position: fixed; top: 0; width: 100%; background: #16213e; padding: 15px 40px; display: flex; gap: 20px; z-index: 100; }
                .navbar a { color: #0f9b8e; text-decoration: none; font-weight: bold; }
                .hero { min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; background: linear-gradient(135deg, #16213e, #0f3460); text-align: center; padding: 20px; }
                .hero h1 { font-size: 3em; color: #0f9b8e; margin-bottom: 10px; }
                .hero h2 { font-size: 1.5em; color: #aaa; }
                section { padding: 60px 40px; max-width: 900px; margin: 0 auto; }
                h2 { color: #0f9b8e; font-size: 2em; margin-bottom: 30px; border-bottom: 2px solid #0f9b8e; padding-bottom: 10px; }
                .timeline-item { background: #16213e; border-left: 4px solid #0f9b8e; padding: 20px; margin-bottom: 20px; border-radius: 0 8px 8px 0; }
                .timeline-item h3 { color: #fff; font-size: 1.2em; }
                .timeline-item span { color: #0f9b8e; font-size: 0.9em; }
                .timeline-item p { color: #aaa; margin-top: 10px; }
                .skills-grid { display: flex; flex-wrap: wrap; gap: 10px; }
                .badge { background: #0f3460; color: #0f9b8e; border: 1px solid #0f9b8e; padding: 8px 16px; border-radius: 20px; font-size: 0.9em; }
                .cert-item { background: #16213e; padding: 15px 20px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #0f9b8e; }
                .contact-info { background: #16213e; padding: 30px; border-radius: 8px; text-align: center; }
                .contact-info a { color: #0f9b8e; text-decoration: none; font-size: 1.2em; }
            </style>
        </head>
        <body>
            <nav class="navbar">
                <a href="#about">About</a>
                <a href="#experience">Experience</a>
                <a href="#skills">Skills</a>
                <a href="#certifications">Certifications</a>
                <a href="#contact">Contact</a>
            </nav>
            <div class="hero">
                <h1>Santos Gómez</h1>
                <h2>Field IT Specialist | bioMérieux</h2>
                <p style="color:#aaa;margin-top:20px;max-width:600px;">IT professional specializing in healthcare interoperability, middleware integration and cloud infrastructure.</p>
            </div>
            <section id="about">
                <h2>About</h2>
                <p style="color:#aaa;line-height:1.8;">Field IT Specialist with expertise in laboratory middleware, HL7/FHIR integration, and critical server management. Currently pursuing a Computer Engineering degree while working at bioMérieux IBERIA managing complex hospital centralization projects.</p>
            </section>
            <section id="experience">
                <h2>Experience</h2>
                <div class="timeline-item">
                    <h3>Field IT Specialist — bioMérieux</h3>
                    <span>2023 – Present</span>
                    <p>Middleware expert for laboratory workflow. HL7 integration, VPN/AWS/VLAN networking, vulnerability management for electromedical equipment.</p>
                </div>
                <div class="timeline-item">
                    <h3>RVA Technician — Docaposte</h3>
                    <span>2022 – 2023</span>
                    <p>EDI partners management on ATLAS/ALLEGRO network. Electronic invoicing support, VAN interconnections monitoring.</p>
                </div>
                <div class="timeline-item">
                    <h3>System Administrator — Siemens</h3>
                    <span>2022</span>
                    <p>Windows/Ubuntu sysadmin, SQL database management, SAP order management, Office 365 administration.</p>
                </div>
                <div class="timeline-item">
                    <h3>Systems Technician — COS / Alcampo</h3>
                    <span>2020 – 2022</span>
                    <p>IT systems administration, Active Directory, Azure MFA, incident management via ServiceNow and Remedy.</p>
                </div>
            </section>
            <section id="skills">
                <h2>Skills</h2>
                <div class="skills-grid">
                    <span class="badge">HL7 v2 / FHIR R4</span>
                    <span class="badge">Docker</span>
                    <span class="badge">AWS</span>
                    <span class="badge">Python</span>
                    <span class="badge">Windows Server</span>
                    <span class="badge">Ubuntu</span>
                    <span class="badge">VPN / VLAN</span>
                    <span class="badge">SQL</span>
                    <span class="badge">Active Directory</span>
                    <span class="badge">Azure</span>
                    <span class="badge">LangGraph</span>
                    <span class="badge">FastAPI</span>
                </div>
            </section>
            <section id="certifications">
                <h2>Certifications</h2>
                <div class="cert-item"><strong>AWS Cloud Practitioner</strong> — 2024</div>
                <div class="cert-item"><strong>Docker Certified Associate</strong> — 2024</div>
                <div class="cert-item"><strong>HL7 Spain V2.8</strong> — 2024</div>
                <div class="cert-item"><strong>Streaming HL7 to FHIR — Google Healthcare API</strong> — 2024</div>
                <div class="cert-item"><strong>NSE 1/2/3 Fortinet</strong> — 2022</div>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <div class="contact-info">
                    <p style="margin-bottom:15px;">📧 <a href="mailto:santos.ggvazquez@gmail.com">santos.ggvazquez@gmail.com</a></p>
                    <p>📍 Tres Cantos, Madrid</p>
                </div>
            </section>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
