This app splits a list of names into random teams of roughly equal size.

# Team Generator

[English](README.md) · [Türkçe](README.tr.md)

Enter comma-separated names, choose how many teams you want and submit the form. Python shuffles the list and distributes names in turn, so team sizes differ by at most one.

## Run locally

You need Python 3 with pip and venv, and a web browser.

```text
git clone https://github.com/ArdaHFO/team-generator.git
cd team-generator
python -m venv .venv
```

Activate the environment with `.venv\Scripts\activate` in Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 5000
```

Open [localhost:5000](http://127.0.0.1:5000). You can also start the local server with `python app.py`; debug mode is disabled.

## Create teams

Try `Ada, Deniz, Ece, Mert, Selin, Can` with `3` teams, then select **Generate Teams**. Each team will have two names. Submitting again reshuffles the list.

- The team count must be a positive integer no larger than the number of participants.
- Leading and trailing spaces are removed, and empty entries are ignored.
- Duplicate names count as separate entries.
- Teams are balanced by size only. Skills, roles and other attributes are not considered.

There is no saved history, export function or reproducible seeded draw. The interface mixes Turkish and English labels, and the repository has no automated test suite.

## Code

[app.py](app.py) handles the form and assignment. The templates, [index.html](index.html) and [teams.html](teams.html), live in the repository root. [views.py](views.py) provides an alternate entry at `/views/`.

## License

No project license is included. Flask and other dependencies retain their own licenses.
