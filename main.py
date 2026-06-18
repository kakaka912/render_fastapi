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
            <title>間違い探しぢゃよ</title>
            <script>
                function correct() {
                    alert("正解！");
                }
            </script>
        </head>
        <body style="background-color:#eef; text-align:center; padding-top:50px; font-family:sans-serif;">
            <h1 style="color:#333;">間違い探しを始めるよ</h1>
            <p style="cursor: pointer;">束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <p>束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <p>束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <p>束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <p>束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <!-- 正解） -->
            <p>束束<body style="background-color:#eef; text-align:center; padding-top:50px; font-family:sans-serif; cursor: pointer;" onclick="correct()">東</b><body style="background-color:#eef; text-align:center; padding-top:50px; font-family:sans-serif;">束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <p>束束束束束束束束束束束束束束束束束束束束束束束束束束束束束束</p>
            <hr style="margin:40px;">
            <p style="color:#666;">Powered by FastAPI × Render</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
