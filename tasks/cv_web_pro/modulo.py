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
                body {
                    font-family: Arial, sans-serif;
                    background-color: #2f2f2f;
                    color: #ffffff;
                }
                .hero {
                    background-color: #1a1a1a;
                    padding: 20px;
                    text-align: center;
                }
                .navbar {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    background-color: #1a1a1a;
                    padding: 10px;
                    display: flex;
                    justify-content: space-between;
                }
                .about {
                    padding: 20px;
                }
                .experience {
                    padding: 20px;
                }
                .skills {
                    padding: 20px;
                }
                .certifications {
                    padding: 20px;
                }
                .contact {
                    padding: 20px;
                }
            </style>
        </head>
        <body>
            <div class="navbar">
                <h1>Santos Gómez - Field IT Specialist</h1>
            </div>
            <div class="hero">
                <h1>Santos Gómez</h1>
                <h2>Field IT Specialist</h2>
            </div>
            <div class="about">
                <h2>About</h2>
                <p>Descripción profesional</p>
            </div>
            <div class="experience">
                <h2>Experience</h2>
                <ul>
                    <li>bioMérieux - 2023</li>
                    <li>Docaposte - 2022-2023</li>
                    <li>Siemens - 2022</li>
                </ul>
            </div>
            <div class="skills">
                <h2>Skills</h2>
                <ul>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">HL7</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">FHIR</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">Docker</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">AWS</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">Python</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">Windows Server</span></li>
                    <li><span style="background-color: #007bff; color: #ffffff; padding: 5px; border-radius: 5px;">Ubuntu</span></li>
                </ul>
            </div>
            <div class="certifications">
                <h2>Certifications</h2>
                <ul>
                    <li>AWS Cloud Practitioner</li>
                    <li>Docker Certified Associate</li>
                    <li>HL7 Spain</li>
                </ul>
            </div>
            <div class="contact">
                <h2>Contact</h2>
                <p>santos.ggvazquez@gmail.com</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
