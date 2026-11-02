from flask import Flask, render_template, request
import random
from views import views

app = Flask(__name__, template_folder=".")
app.register_blueprint(views, url_prefix="/views")


@app.route("/", methods=["GET", "POST"])
def random_team_generator():
    if request.method == "POST":
        members = [
            member.strip()
            for member in request.form.get("members", "").split(",")
            if member.strip()
        ]
        try:
            num_teams = int(request.form.get("num_teams", ""))
        except (TypeError, ValueError):
            return render_template(
                "index.html", error="Takım sayısı pozitif bir tam sayı olmalıdır."
            ), 400

        if not members or not 1 <= num_teams <= len(members):
            return render_template(
                "index.html",
                error="İsim girin ve katılımcı sayısını aşmayan pozitif bir takım sayısı seçin.",
            ), 400

        random.shuffle(members)
        teams = {f"Team {i}": [] for i in range(1, num_teams + 1)}
        for i, member in enumerate(members):
            teams[f"Team {i % num_teams + 1}"].append(member)
        return render_template("teams.html", teams=teams)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
