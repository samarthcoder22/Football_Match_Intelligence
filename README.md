# ⚽ Football Match Intelligence

## Manchester City vs Queens Park Rangers — 2011/12 Premier League

An interactive football analytics dashboard analyzing Manchester City's dramatic
3–2 comeback against Queens Park Rangers on 13 May 2012 at the Etihad Stadium.

The project combines match statistics, event analysis, attacking pressure,
score evolution and interactive visualizations to turn historical football
data into meaningful match insights.

---

## 📊 Project Overview

This project explores the tactical and statistical story behind one of the
most dramatic finishes in Premier League history.

Manchester City recorded:

- 81.3% possession
- 44 total shots
- 15 shots on target
- 19 corners
- 710 passes

Despite falling behind 2–1, City scored twice in stoppage time through
Edin Džeko and Sergio Agüero to complete a 3–2 comeback.

---

## 🎯 Objectives

- Analyze match statistics and event data
- Visualize the progression of the match
- Examine Manchester City's attacking pressure
- Analyze the late-game comeback
- Compare attacking efficiency
- Build an interactive football analytics dashboard

---

## 🖥️ Dashboard Features

### Overview
- Match header with team logos
- Score and match information
- Key performance indicators
- Score evolution
- Attacking pressure analysis
- Shot efficiency comparison
- City shot-volume visualization
- Key match insights

### Match Events
- Interactive event timeline
- Goal and disciplinary event filtering
- Match event log
- Comeback analysis
- Late-game impact analysis

### Statistics
- Possession comparison
- Attacking output
- Full match statistics table

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Matplotlib
- mplsoccer
- Pillow
- Streamlit
- Jupyter Notebook

---

## 📁 Project Structure

```text
Football_Match_Intelligence/
│
├── app/
│   └── app.py
│
├── assets/
│   ├── city.png
│   └── qpr.png
│
├── data/
│   ├── raw/
│   │   ├── city_qpr_events.csv
│   │   └── city_qpr_match_stats.csv
│   │
│   ├── processed/
│   │   ├── city_qpr_events_processed.csv
│   │   ├── city_qpr_shot_pressure.csv
│   │   ├── city_qpr_attacking_efficiency.csv
│   │   └── city_qpr_match_intelligence.csv
│   │
│   └── data_dictionary.csv
│
├── notebooks/
│   └── City_QPR_Analytics.ipynb
│
├── requirements.txt
└── README.md