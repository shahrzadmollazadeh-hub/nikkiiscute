from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday</title>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#ff69b4,#ffe4ec););
    font-family:Arial,sans-serif;
}
.card{
     background:white;
     padding:40px;
     border-radius:20px;
     text-align:center;
     box-shadow:0 0 25px rgba(0,0,0,0.2);
     max-width:700px;
}
h1{
   color:#ff4d6d;
}

img{
   width:350px;
   border-radius:15px
}

p{
    font-size:20px;
}
button{
      background:#ff4d6d;
      color:white;
      border:none;
      padding:15px 25px;
      border-radius:10px;
      cursor:pointer;
      font-size:18px;
}

button:hover{
   transform:scale(1.05);
}
#message{
    margin-top:20px;
    color:#ff4d6d;
    font-size:24px;
}

</style>
</head>

<body>

<div class='card'>

<h1> 🎂 Happy Birthday 🎂 </h1>

<img src="/static/image.jpg">

<p>
Wishing you a wonderful birthday filled with happiness and success Nikki.
</p>

<button onclick="showMessage()">
Open your Gift 🎁
</button>

<h2 id="message"></h2>

</div>

<script>
function showMessage(){

document.getElementById("message").innerHTML = 
"💖 You are my little yeoppo! Have the best birthday ever! 💖"

 confetti({
    particleCount: 200,
    spread: 120,
    origin: { y: 0.6 }
});
}

</script>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
