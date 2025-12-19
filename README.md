# Hypotension Early Warning System

This project implements a **clinical decision support system**
for early prediction of hypotension using vital signs.

## Pipeline
Vitals → Feature Extraction → Gate → ML Model → Alarm (A/B/C)

## Alarm Levels
- **A**: Rapid & severe hypotension
- **B**: Gradual hypotension
- **C**: Intermittent hypotension

## Deployment
Built with Streamlit and deployed via Streamlit Cloud.
