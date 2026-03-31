from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def read_root():
    html_content = '''
    <html>
    <head>
    <title>Santos Gómez - Field IT Specialist</title>
    <style>
    body { background-color: #2f2f2f; color: #ffffff; font-family: Arial, sans-serif; }
    .navbar { position: fixed; top: 0; left: 0; width: 100%; background-color: #333333; padding: 10px; }
    .hero { background-color: #444444; padding: 50px; text-align: center; }
    .about { padding: 20px; }
    .experience { padding: 20px; }
    .skills { padding: 20px; }
    .certifications { padding: 20px; }
    .contact { padding: 20px; }
    </style>
    </head>
    <body>
    <div class='navbar'>
    <h1>Santos Gómez - Field IT Specialist</h1>
    </div>
    <div class='hero'>
    <h1>Santos Gómez</h1>
    <h2>Field IT Specialist</h2>
    </div>
    <div class='about'>
    <h2>About</h2>
    <p>Descripción profesional</p>
    </div>
    <div class='experience'>
    <h2>Experience</h2>
    <ul>
    <li>2023: bioMérieux</li>
    <li>2022-2023: Docaposte</li>
    <li>2022: Siemens</li>
    </ul>
    </div>
    <div class='skills'>
    <h2>Skills</h2>
    <span class='badge'>HL7</span>
    <span class='badge'>FHIR</span>
    <span class='badge'>Docker</span>
    <span class='badge'>AWS</span>
    <span class='badge'>Python</span>
    <span class='badge'>Windows Server</span>
    <span class='badge'>Ubuntu</span>
    </div>
    <div class='certifications'>
    <h2>Certifications</h2>
    <ul>
    <li>AWS Cloud Practitioner</li>
    <li>Docker Certified Associate</li>
    <li>HL7 Spain</li>
    </ul>
    </div>
    <div class='contact'>
    <h2>Contact</h2>
    <p>santos.ggvazquez@gmail.com</p>
    </div>
    </body>
    </html>
    '''
    return HTMLResponse(content=html_content, status_code=200)