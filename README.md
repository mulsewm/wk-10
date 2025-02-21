Here is the updated README.md based on the project instructions and deliverables:

# 10 Academy: Artificial Intelligence Mastery - Week 10 Challenge  
**Change Point Analysis and Statistical Modelling of Time Series Data**  

## Date: 19 Feb - 25 Feb 2025  

### Business Objective  

The primary goal of this project is to analyze how significant political and economic events influence **Brent oil prices** over time. This involves identifying key events, detecting price changes, and quantifying their impacts. The analysis will provide **data-driven insights** to assist **investors, policymakers, and energy companies** in making informed decisions.  

Key aspects include:  
- **Detecting and analyzing price fluctuations** using statistical and Bayesian models.  
- **Understanding the impact of major events**, such as political decisions, conflicts, sanctions, and OPEC policy changes.  
- **Developing an interactive dashboard** to visualize the analysis results.  

---

## Situational Overview  

You are a **data scientist at Birhan Energies**, a leading consultancy firm specializing in providing **data-driven insights** to stakeholders in the **energy sector**. The oil market is highly volatile, making it difficult for:  
- **Investors** to make informed decisions and manage risk.  
- **Policymakers** to create strategies for **economic stability and energy security**.  
- **Energy companies** to forecast **prices, plan operations, and optimize supply chains**.  

Your task is to:  
1. **Identify key historical events** that have impacted Brent oil prices.  
2. **Measure their effects** using change point analysis and Bayesian inference.  
3. **Generate insights** to guide investment, policy development, and operational planning.  

---

## Dataset  

The dataset contains **historical Brent oil prices** from **May 20, 1987, to September 30, 2022**.  

### Data Fields:  
- **Date:** The date of the recorded Brent oil price (formatted as ‘day-month-year’, e.g., 20-May-87).  
- **Price:** Brent oil price in **USD per barrel** on the corresponding date.  

---

## Learning Outcomes  

### **Skills Gained:**  
- Statistical Modelling & Change Point Detection  
- Bayesian Inference using **PyMC3**  
- Monte Carlo Markov Chain (MCMC)  
- Model comparison & evaluation  
- Policy impact analysis  

### **Knowledge Areas:**  
- Understanding **probability distributions** for time series data  
- **Bayesian modeling techniques** and model selection  
- **Time series econometrics**, including ARIMA, GARCH, and regime-switching models  
- **Policy analysis techniques** for interpreting economic and regulatory impacts  

---

## **Project Objectives & Tasks**  

### **Task 1: Defining the Data Analysis Workflow & Understanding the Data**  
- Establish a **step-by-step workflow** for analyzing Brent oil prices.  
- Understand how **time series models** such as ARIMA, GARCH, and Bayesian models fit the data.  
- Identify key **assumptions, parameters, and limitations** of the models.  
- Explore **historical events** that may correlate with price changes.  

### **Task 2: Analyzing Brent Oil Prices Using Change Point Analysis & Bayesian Modelling**  
- Use **change point detection** techniques to **identify significant price shifts**.  
- Apply **advanced time series models** such as:  
  - **ARIMA/GARCH** for volatility modeling  
  - **Vector Autoregression (VAR)** for multivariate analysis  
  - **Markov-Switching Models** to capture different market conditions  
  - **LSTM (Long Short-Term Memory) models** for deep learning-based forecasting  
- Investigate **economic, political, and technological** factors influencing oil prices, such as:  
  - **GDP growth, inflation, and unemployment**  
  - **Exchange rate fluctuations**  
  - **Trade policies, environmental regulations, and energy transitions**  
- **Validate models** using **backtesting, cross-validation, and performance metrics** (e.g., RMSE, MAE).  

### **Task 3: Developing an Interactive Dashboard to Visualize Insights**  
**Goal:** Create a **Flask (backend) and React (frontend) dashboard** to explore how different events impact Brent oil prices.  

**Key Features:**  
- **Historical trends and forecasts**  
- **Event-based visualization** to highlight price changes  
- **Interactive filters** (date range, event types, statistical indicators)  
- **Performance metrics and model accuracy displays**  

#### **Tech Stack:**  
- **Backend:** Flask, REST API  
- **Frontend:** React, Chart.js, D3.js  
- **Data Processing:** Pandas, NumPy, PyMC3  
- **Machine Learning:** Scikit-learn, TensorFlow/Keras (for LSTM)  

---

## **Key Deadlines & Submission Guidelines**  

| **Event**                 | **Date**                  | **Notes**  |
|---------------------------|--------------------------|------------|
| **Case Discussion**        | Wednesday, 19 Feb 2025   | Use Slack #all-week10 for pre-questions |
| **Interim Submission**     | Friday, 21 Feb 2025 (20:00 UTC) | Covers Task 1 |
| **Final Submission**       | Tuesday, 25 Feb 2025 (20:00 UTC) | Full project deliverables |

### **Submission Requirements:**  
1. **GitHub Repository:** Codebase with README, scripts, and Jupyter Notebooks.  
2. **Interim Submission:** Interim report covering Task 1, with GitHub link.  
3. **Final Submission:**  
   - A **blog post or PDF report** explaining findings, methods, and insights.  
   - **GitHub repository** with documented code.  
   - Screenshots or recorded demos of the **interactive dashboard**.  

---

## **Team & Instructors**  

### **Tutors & Instructors:**  
- **Mahlet** – Data Science Workflow  
- **Rediet** – Data Analysis Techniques  
- **Kerod** – Change Point Analysis  
- **Elias** – Bayesian Inference  
- **Emitinan** – React Dashboard Development  
- **Rehmet** – Policy Analysis  

---

## **References & Learning Resources**  

### **Data Science Workflow**  
- [Mastering the Data Science Workflow](https://towardsdatascience.com/mastering-the-data-science-workflow-2a47d8b613c4)  
- [Data Science Workflow Guide](https://www.datascience-pm.com/data-science-workflow/)  

### **Change Point Analysis**  
- [Bayesian Change Point Detection](https://towardsdatascience.com/change-point-detection-a-bayesian-approach-8eb3cfca4a6e)  
- [Fraunhofer: Change Point Detection](https://www.iese.fraunhofer.de/blog/change-point-detection/)  

### **Bayesian Inference & Monte Carlo Methods**  
- [Markov Chain Monte Carlo Explained](https://towardsdatascience.com/monte-carlo-markov-chain-mcmc-explained-94e3a6c8de11)  
- [Bayesian Structural Time Series](https://towardsdatascience.com/bayesian-structural-time-series-interruption-method-5018761db92b)  

### **React Dashboard Development**  
- [React Dashboard Templates](https://github.com/flatlogic/react-dashboard)  
- [Light Bootstrap Dashboard React](https://github.com/creativetimofficial/light-bootstrap-dashboard-react)  

---

## **How to Run This Project**  

### **1. Clone the Repository**  
```sh
git clone <REMOTE_REPO_URL>
cd <PROJECT_DIR>

2. Install Dependencies

Backend (Flask)

cd src/dashboard/backend
pip install -r requirements.txt

Frontend (React)

cd src/dashboard/frontend
npm install

3. Run the Application

Start Backend API

cd src/dashboard/backend
python app.py

Start Frontend Dashboard

cd src/dashboard/frontend
npm start

License

This project is for educational purposes as part of 10 Academy’s Artificial Intelligence Mastery program.


