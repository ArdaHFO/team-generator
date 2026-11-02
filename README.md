This app divides a list of people into randomly chosen teams.

<h1 align="center">Team Generator</h1>

<p align="center"><strong>One participant list. A fresh set of teams.</strong></p>
<p align="center">A Python and Flask application that shuffles comma-separated names and distributes them across a chosen number of teams.</p>

<p align="center">
  <strong>English</strong> · <a href="README.tr.md">Türkçe</a><br />
  <a href="#run-locally"><strong>Run locally</strong></a> ·
  <a href="#create-teams">Create teams</a> ·
  <a href="#validation-and-current-limits">Current limits</a>
</p>

---

Team Generator explores a simple form-to-result workflow. Enter participant names, choose a team count and submit the form. The server shuffles the list, then assigns participants in turn so team sizes differ by at most one for a valid positive team count.

**The app focuses on participant entry and team assignment.** The interface mixes Turkish and English labels. The form and result templates are stored at the repository root, and the application explicitly loads them from there.

## Run locally

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Development environment |
| Flask 3.0.0 | Form handling and HTML templates |
| Web browser | Participant form and team results |

```text
git clone https://github.com/ArdaHFO/team-generator.git
cd team-generator
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 5000
```

Open [localhost:5000](http://127.0.0.1:5000). You can also use `python app.py`, which starts one local server with debug mode disabled.

## Create teams

1. Enter names separated by commas, for example `Ada,Deniz,Ece,Mert,Selin,Can`.
2. Enter a positive whole number of teams, for example `3`.
3. Select **Generate Teams** to view the assignments.

Each submitted entry is assigned once. With six entries and three teams, each team contains two entries. Submitting again can produce a different grouping.

## Inside the project

- **Short form workflow.** One page collects participants and the desired team count.
- **Randomized order.** Python's `random.shuffle` reorders the submitted list.
- **Balanced counts.** Round-robin assignment distributes the shuffled entries across teams.
- **Simple result page.** A Jinja template renders each team and its participants.
- **Small dependency footprint.** The application uses Flask and Python's standard library. It implements no database or account system.

## Validation and current limits

The source has been reviewed statically. Application execution, automated tests and browser checks were not performed for these changes.

- The server rejects invalid team counts, empty participant lists and more teams than participants. Names are trimmed and empty entries are removed.
- A person entered twice is still treated as two entries. The algorithm balances counts, not skill, role or other participant attributes.
- No automated test suite, persistent team history or export function is included.
- The interface is designed for local use. Static corrections are not evidence of tested browser behavior.

The randomization is intended for informal grouping. The implementation does not provide an auditable draw or seeded reproducibility.

## Project map

```text
app.py            Form processing, shuffle and team assignment
views.py          Alternate /views/ page
index.html        Participant and team-count form
teams.html        Jinja results template
requirements.txt  Pinned Flask environment
```

## Development and contributions

Keep the form, input validation and assignment logic easy to follow. Future changes should preserve positive bounded team counts, nonempty entries and balanced assignment. Deterministic tests for those rules would improve confidence.

For a bug report, include the team count and a small set of fictional names. Avoid posting real participant lists.

## License

No project license file is included in this repository. Do not infer a permissive code license from its public visibility. Flask and other dependencies retain their own licenses.
