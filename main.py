from flask import Flask, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "bornfree_secret_key"
DEVELOPER_MODE = False

def get_votes():
    conn = sqlite3.connect("poll.db")
    cursor = conn.cursor()

    cursor.execute("SELECT option, count FROM votes")

    votes = {}
    for option, count in cursor.fetchall():
        votes[option] = count

    conn.close()

    return votes


@app.route("/")
def home():

    votes = get_votes()

    total = sum(votes.values())

    if total == 0:
        loved_percent = 0
        good_percent = 0
        notforme_percent = 0
    else:
        loved_percent = round(votes["loved"] / total * 100)
        good_percent = round(votes["good"] / total * 100)
        notforme_percent = round(votes["notforme"] / total * 100)

    return render_template(
        "index.html",
        loved=loved_percent,
        good=good_percent,
        notforme=notforme_percent,
        loved_votes=votes["loved"],
        good_votes=votes["good"],
        notforme_votes=votes["notforme"],
        total_votes=total,
        has_voted=session.get("voted", False)
    )

@app.route("/vote/<option>")
def vote(option):

    if not DEVELOPER_MODE and session.get("voted"):
        return redirect(url_for("home"))

    conn = sqlite3.connect("poll.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE votes SET count = count + 1 WHERE option = ?",
        (option,)
    )

    conn.commit()
    conn.close()

    session["voted"] = True

    return redirect(url_for("home"))

@app.route("/developer-reset-bornfree")
def reset():

    conn = sqlite3.connect("poll.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE votes SET count = 0")

    conn.commit()
    conn.close()

    session.pop("voted", None)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
