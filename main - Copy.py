from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style="background-color:black;;color:#d4af37;font-family:Arial;padding:40px;text-align:center;">
        <h1 style="font-size:60px;">BORN FREE?</h1>
        <p><em>Freedom Has A Price.</em></p>
        
        <img src="/static/fire_still.jpeg" width="500">
        
        <p style="font-size:24px;">A short film about Freedom, Historical injustice, and Resistance.</p>

        <hr>

        <h2>Synopsis</h2>
        <div style="width:70%; margin:auto;">
        <p>
        A young woman dives into the depths of her mind to interrogate the true meaning of "Freedom" in a democratic South Africa.
        </p>
        </div>
        
        <hr>
        <img src="/static/poster.jpeg" width="300">
        <img src="/static/BORN FREE ALT POSTER.png" width="677">
        <hr>

        <h2>Trailer</h2>
        <p>Coming Soon</p>

        <h2>Gallery</h2>
        <p>Production photos coming soon.</p>

        <h2>Contact</h2>
        <p>greatecutengqwarushe@gmail.com</p>
    </body>
    """

if __name__ == "__main__":
    app.run(debug=True)