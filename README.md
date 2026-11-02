<h1 align="center">Python-W · Team Generator</h1>

<p align="center"><strong>One participant list. A fresh set of teams.</strong></p>
<p align="center">A small Python and Flask prototype that shuffles comma-separated names and distributes them across a chosen number of teams.</p>

<p align="center">
  <strong>English</strong> · <a href="README.tr.md">Türkçe</a><br />
  <a href="#run-locally"><strong>Run locally</strong></a> ·
  <a href="#create-teams">Create teams</a> ·
  <a href="#validation-and-current-limits">Current limits</a>
</p>

---

Python-W explores a simple form-to-result workflow. Enter participant names, choose a team count and submit the form. The server shuffles the list, then assigns participants in turn so team sizes differ by at most one for a valid positive team count.

**This is a minimal prototype.** The interface mixes Turkish and English labels. The source includes the form and result templates at the repository root, which requires the template-path adjustment shown below.

## Run locally

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Development environment |
| Flask 3.0.0 | Form handling and HTML templates |
| Web browser | Participant form and team results |

```text
git clone https://github.com/ArdaHFO/python-w.git
cd python-w
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux.

```text
python -m pip install -r requirements.txt
python -c "import app; app.app.template_folder = '.'; app.app.run(host='127.0.0.1', port=5000, debug=False)"
```

Open [localhost:5000](http://127.0.0.1:5000). The preview command points Flask at the existing root-level HTML templates for that process. It does not move or edit source files. A plain `python app.py` launch retains Flask's default `templates/` lookup and will not find the tracked HTML files.

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

The Python source, templates and dependency file were reviewed. No browser or runtime integration test was performed.

- Root-level templates need the preview override above or a future template-layout correction.
- Team count has no server-side validation. Zero, negative or nonnumeric input can fail or produce unsuitable output. Use a positive whole number no greater than the participant count.
- Names are split on commas without trimming, deduplication or removal of empty entries. Enter clean, nonempty values.
- A person entered twice is treated as two entries. The algorithm balances counts, not skill, role or other participant attributes.
- The application has overlapping GET routes for the home page. It also contains two consecutive development-server calls in its main entry point.
- No automated test suite, persistent team history or export function is included.

The randomization is intended for informal grouping. The implementation does not provide an auditable draw or seeded reproducibility.

## Project map

```text
app.py            Form processing, shuffle and team assignment
views.py          Home-page blueprint
index.html        Participant and team-count form
teams.html        Jinja results template
requirements.txt  Pinned Flask environment
```

## Development and contributions

Keep the form, input validation and assignment logic easy to follow. Useful changes include normalizing participant names, validating team counts, resolving the template layout and adding deterministic tests for assignment counts.

For a bug report, include the team count and a small set of fictional names. Avoid posting real participant lists.

## License

No project license file is included in this repository. Do not infer a permissive code license from its public visibility. Flask and other dependencies retain their own licenses.

