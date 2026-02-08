from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Be My Valentine 💖</title>

<style>
    body {
        margin: 0;
        height: 100vh;
        font-family: 'Courier New', monospace;
        text-align: center;
        overflow: hidden;

        /* 🎨 SVG background */
        background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAiIGhlaWdodD0iMTIwIj4KICA8cmVjdCB3aWR0aD0iMTIwIiBoZWlnaHQ9IjEyMCIgZmlsbD0iI2ZmZTZmMCIvPgogIDxwYXRoIGQ9Ik02MCAyMCBDMjAgLTEwIC0xMCAzMCA2MCA5MCBDMTMwIDMwIDEwMCAtMTAgNjAgMjAgWiIgZmlsbD0iI2ZmYjNjNiIgb3BhY2l0eT0iMC4zIi8+Cjwvc3ZnPg==");\
        <svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'>\
            <rect width='120' height='120' fill='%23ffe6f0'/>\
            <path d='M60 20 C20 -10 -10 30 60 90 C130 30 100 -10 60 20 Z' fill='%23ffb3c6' opacity='0.3'/>\
        </svg>");
        background-repeat: repeat;
    }

    h1 {
        margin-top: 40px;
        font-size: 3rem;
        color: #c9184a;
        text-shadow: 2px 2px #fff;
    }

    img {
        width: 280px;
        margin: 20px;
        image-rendering: pixelated;
    }

    /* 🕹️ Retro Button Base */
    button {
        font-family: 'Courier New', monospace;
        font-size: 1.3rem;
        padding: 15px 35px;
        margin: 20px;
        border: 4px solid black;
        box-shadow: 6px 6px 0 black;
        cursor: pointer;
        transition: all 0.1s ease;
        background: #fff;
    }

    button:active {
        box-shadow: 2px 2px 0 black;
        transform: translate(4px, 4px);
    }

    #yes {
        background: #ff4d6d;
        color: white;
    }

    #no {
        background: #adb5bd;
        color: black;
        position: absolute;
    }

    /* 🎊 Confetti */
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        top: -10px;
        animation: fall linear forwards;
    }

    @keyframes fall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }

    /* 💕 Floating Hearts */
    .heart {
        position: fixed;
        bottom: 0;
        font-size: 24px;
        animation: floatUp 3s linear forwards;
    }

    @keyframes floatUp {
        to {
            transform: translateY(-100vh);
            opacity: 0;
        }
    }
</style>
</head>

<body>

<h1 id="question">Will you be my Valentine, Nicole? </h1>

<img id="gif" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGVtN2JmcmlzNjUxNXRkcG50dXJsaXJzM2E1ZmR4OWp5amMzc3RpMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sXv0vaA4331Ti/giphy.gif">

<br>

<button id="yes" onclick="sayYes()">▶ YES</button>
<button id="no" onmouseover="moveNo()">◀ NO</button>

<script>
function moveNo() {
    const noBtn = document.getElementById("no");
    const maxX = window.innerWidth - noBtn.offsetWidth;
    const maxY = window.innerHeight - noBtn.offsetHeight;

    noBtn.style.left = Math.random() * maxX + "px";
    noBtn.style.top = Math.random() * maxY + "px";
}

function sayYes() {
    document.getElementById("question").innerText =
        "STAGE CLEARED! 💖💖💖 Thank you so much, my love 😙";
    document.getElementById("gif").src =
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTV1b2FzbndkaDR4NGY5MHVhNTljMzM0czg1ODkyYmFnbnFsd3h3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uiyXLcZBmbEGqaqQXz/giphy.gif";
    document.getElementById("no").style.display = "none";

    launchConfetti();
    startHearts();
}

function launchConfetti() {
    for (let i = 0; i < 150; i++) {
        const confetti = document.createElement("div");
        confetti.className = "confetti";
        confetti.style.left = Math.random() * window.innerWidth + "px";
        confetti.style.backgroundColor =
            ["#ff4d6d", "#ffb3c6", "#c9184a", "#ffd6e0"]
            [Math.floor(Math.random()*4)];
        confetti.style.animationDuration =
            (Math.random() * 2 + 2) + "s";
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 4000);
    }
}

function startHearts() {
    setInterval(() => {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = "💖";
        heart.style.left = Math.random() * window.innerWidth + "px";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 3000);
    }, 300);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
