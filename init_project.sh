#!/bin/bash
# init_project.sh
# Usage: ./init_project.sh <REMOTE_REPO_URL>
#
# This script sets up the project structure for:
# "10 Academy: Artificial Intelligence Mastery - Week 10 Challenge"
# "Change Point Analysis and Statistical Modelling of Time Series Data"
#
# It creates directories and placeholder files for:
# - Data analysis workflow and model understanding (Task 1)
# - Analysis of Brent oil prices using change point analysis and Bayesian models (Task 2)
# - An interactive dashboard with a Flask backend and a React frontend (Task 3)
#
# Finally, it initializes a git repository, makes an initial commit,
# and pushes the commit to the specified GitHub repository.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <REMOTE_REPO_URL>"
    exit 1
fi

REMOTE_URL=$1

echo "Creating project directory structure..."

# Root-level files and directories
mkdir -p data/raw data/processed
mkdir -p notebooks
mkdir -p src/dashboard/backend src/dashboard/frontend/src
mkdir -p docs
mkdir -p scripts

echo "Creating README.md..."
cat <<EOL > README.md
# 10 Academy: Artificial Intelligence Mastery - Week 10 Challenge
## Change Point Analysis and Statistical Modelling of Time Series Data

**Business Objective:**  
Analyze how key events (political decisions, conflicts, sanctions, OPEC policy changes) impact Brent oil prices.

**Project Deliverables:**
- **Task 1:** Define a comprehensive data analysis workflow and understand the model/data.
- **Task 2:** Perform change point analysis and build statistical/Bayesian models to quantify event impacts.
- **Task 3:** Develop an interactive dashboard (Flask backend & React frontend) to visualize analysis results.

This repository contains all code, documentation, and scripts associated with this challenge.
EOL

echo "Creating .gitignore..."
cat <<EOL > .gitignore
# Python artifacts
__pycache__/
*.py[cod]
*.so

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Node modules and build artifacts
node_modules/
build/

# Data folders (raw and processed data should not be committed)
data/raw/
data/processed/

# Environment files
.env
EOL

echo "Creating root requirements.txt..."
cat <<EOL > requirements.txt
# Python dependencies for the analysis and dashboard backend
pymc3
flask
# Add additional dependencies as needed
EOL

echo "Creating sample Jupyter Notebook for analysis..."
cat <<EOL > notebooks/BrentOilChangePointAnalysis.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Brent Oil Price Change Point Analysis\n",
    "This notebook outlines the exploratory analysis and change point detection in Brent oil prices."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Starting analysis...')"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
EOL

echo "Creating analysis script (src/analysis.py)..."
cat <<EOL > src/analysis.py
#!/usr/bin/env python3
\"\"\"Main analysis script for Brent oil price evaluation.\"\"\"

def run_workflow():
    print("Running data collection, preprocessing, and exploratory analysis...")
    # Insert data analysis workflow here

if __name__ == '__main__':
    run_workflow()
EOL

echo "Creating model definitions (src/models.py)..."
cat <<EOL > src/models.py
#!/usr/bin/env python3
\"\"\"Model definitions for time series, change point detection, and Bayesian analysis.\"\"\"

def build_statistical_models():
    print("Building ARIMA/GARCH and other time series models...")

def run_bayesian_inference():
    print("Running Bayesian inference with PyMC3...")

if __name__ == '__main__':
    build_statistical_models()
    run_bayesian_inference()
EOL

echo "Creating dashboard backend (src/dashboard/backend/app.py)..."
cat <<EOL > src/dashboard/backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/brent-data', methods=['GET'])
def get_brent_data():
    # This endpoint will serve processed analysis data.
    return jsonify({"message": "Brent oil price analysis data goes here"})

if __name__ == '__main__':
    app.run(debug=True)
EOL

echo "Creating dashboard backend requirements (src/dashboard/backend/requirements.txt)..."
cat <<EOL > src/dashboard/backend/requirements.txt
Flask
EOL

echo "Creating dashboard frontend configuration (src/dashboard/frontend/package.json)..."
cat <<EOL > src/dashboard/frontend/package.json
{
  "name": "brent-oil-dashboard",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
EOL

echo "Creating dashboard frontend main file (src/dashboard/frontend/src/App.js)..."
cat <<EOL > src/dashboard/frontend/src/App.js
import React from 'react';

function App() {
  return (
    <div>
      <h1>Brent Oil Prices Dashboard</h1>
      <p>Visualizing change point analysis and model results.</p>
    </div>
  );
}

export default App;
EOL

echo "Creating placeholder for final report (docs/FinalReport.pdf)..."
touch docs/FinalReport.pdf

echo "Creating a helper script to run all analysis (scripts/run_all.sh)..."
cat <<EOL > scripts/run_all.sh
#!/bin/bash
echo "Executing full analysis pipeline..."
python3 src/analysis.py
python3 src/models.py
EOL
chmod +x scripts/run_all.sh

echo "Initializing git repository..."
git init
git branch -M main

echo "Adding all files to git..."
git add .

echo "Making initial commit..."
git commit -m "Initial commit: Project structure and initial files for Week 10 Challenge"

echo "Adding remote repository: $REMOTE_URL"
git remote add origin "$REMOTE_URL"

echo "Pushing to GitHub..."
git push -u origin main

echo "Project structure created, initial commit made, and pushed to GitHub successfully."
