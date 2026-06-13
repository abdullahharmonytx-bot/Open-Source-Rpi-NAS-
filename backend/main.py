from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="ALPHA")

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return """
    <html>
        <head>
            <title>ALPHA</title>
        </head>
        <body>
            <h1>Welcome to ALPHA</h1>
            <p>Open Source Raspberry Pi NAS</p>

            <a href="/setup">
                <button>Start Setup</button>
            </a>
        </body>
    </html>
    """

@app.get("/setup", response_class=HTMLResponse)
async def setup():
    return """
    <html>
        <head>
            <title>ALPHA Setup</title>
        </head>
        <body>
            <h1>Create Administrator</h1>

            <form>
                <input placeholder="Name"><br><br>
                <input placeholder="Username"><br><br>
                <input type="password" placeholder="Password"><br><br>

                <button>Create Admin</button>
            </form>
        </body>
    </html>
    """
