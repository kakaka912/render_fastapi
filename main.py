from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>マスターのホームページ</title>
        </head>
        <body style="background-color:#eef; text-align:center; padding-top:50px; font-family:sans-serif;">
            <h1 style="color:#333;">ようこそ！ここは24FI094の FastAPI ホームページ</h1>
            <p>これは課題 9-1 の Web ページです。</p>
            <p>HTML は自由に編集できます。</p>
            <hr style="margin:40px;">
            <p style="color:#666;">Powered by FastAPI × Render</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
