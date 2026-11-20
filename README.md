# Accessible Route Planner — Project Root

## How to run (for anyone you share this with)
1. **Extract the zip fully first** (right-click → Extract All). Don't run it from inside the zip preview.
2. Install Python 3 if missing: https://www.python.org/downloads/ (tick "Add Python to PATH").
3. Double-click **START HERE (Windows).bat** — or on Mac/Linux run `./"START HERE (Mac-Linux).sh"`.
   Your browser opens the app at http://localhost:8000. An internet connection is required (map tiles, address search, road data).
4. Do NOT double-click `index.html` directly: opened as `file://`, address search and GPS get blocked.

Two folders, per the research plan:

## Original Implementation/
Your working application, frozen as a backup. Open THIS folder in VS Code
to run the app (see its own README.md inside for exact run steps).
Don't edit files here unless you're fixing a real bug — this is the
known-good copy the experiments are run against.

## Research Experiments/
Where the experiment/paper work happens:
- `experiment_tracker.xlsx` — Test Cases, Results Log, and Baseline
  Comparison sheets (Steps 3–7 of the plan).
- `screenshots/` — put your Step 8 evidence here (normal route,
  accessibility-aware route, different profiles, barrier avoidance).

## Suggested workflow
1. Open `Original Implementation/` in VS Code, run it with Live Server.
2. Pick 10–20 fixed routes, add them to `Research Experiments/experiment_tracker.xlsx` (Test Cases sheet).
3. For each route, run every profile (Wheelchair / Elderly / Visually
   Impaired / Normal baseline) in the app, click "Log this result" after
   each, then "Download log (CSV)" and paste the rows into the
   Results Log sheet.
4. Screenshot notable runs into `screenshots/` (Step 8).
5. Fill in the Baseline Comparison sheet using matched Normal vs
   accessibility-aware runs for the same route.
