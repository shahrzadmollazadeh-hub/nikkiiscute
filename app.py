from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Happy Birthday Nikki</title>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#ff69b4,#ffe4ec);
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
    border-radius:15px;
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

</style>
</head>

<body>

<div class="card">

<h1>🎂 Happy Birthday Nikki 🎂</h1>

<img src="/static/image.jpg">

<p>
Wishing you a wonderful birthday filled with happiness and success.
</p>

<button onclick="window.location.href='/surprise'">
Open your Gift 🎁
</button>

</div>

</body>
</html>
"""

@app.route('/surprise')
def surprise():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Surprise!</title>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background:#ffe4ec;
    font-family:Arial,sans-serif;
    text-align:center;
}

h1{
    color:#ff4d6d;
    font-size:42px;
}

.cat{
    width:350px;
    border-radius:15px;
}

p{
    font-size:26px;
    color:#ff4d6d;
}

</style>
</head>

<body>

<h1>🎉 SURPRISE! 🎉</h1>

<img class="cat" src="/static/dancingcat.gif">

<p>
💖 Happy Birthday Nikki! 💖
</p>

<audio controls autoplay loop>
    <source src="/static/music.mp3" type="audio/mpeg">
</audio>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
