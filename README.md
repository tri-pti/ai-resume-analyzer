![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-black)
![React](https://img.shields.io/badge/Frontend-React-61DAFB)
![NLP](https://img.shields.io/badge/NLP-spaCy-green)
![Status](https://img.shields.io/badge/Project-Completed-success)
# AI Resume Analyzer & Career Recommendation System

An AI-powered web application that analyzes resumes, evaluates ATS compatibility, predicts suitable job roles, and provides improvement suggestions.

## Features

* Resume skill extraction using NLP (spaCy)
* ATS compatibility scoring
* Job role prediction
* Career role comparison
* Resume improvement suggestions
* Interactive dashboard (React)

## Tech Stack

* Frontend: React.js
* Backend: Flask (Python)
* NLP: spaCy
* API: REST Architecture

## System Workflow

Resume → Text Extraction → Skill Detection → ATS Scoring → Role Prediction → Suggestions → Visualization

## How It Works

1. Upload resume (PDF)
2. Extract skills using NLP
3. Calculate ATS score
4. Predict best job role
5. Suggest improvements

## Run Locally

1. Backend
* cd backend
* pip install -r requirements.txt
* python app.py
2. Frontend
* cd frontend
* npm install
* npm run dev

## Future Improvements

* LinkedIn job integration
* LLM-based resume rewriting
* Multi-format resume support
