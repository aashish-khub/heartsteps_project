# HeartSteps Project
For the ORIE 5160-030: Statistical Principles for Data Science midterm


## Overview
The HeartSteps Project investigates the effect of personalized fitness suggestions on increasing physical activity levels. Using data from the HeartSteps V1 study, where 37 participants were monitored over six weeks, we assessed how tailored prompts influence step counts. The project combines statistical analysis and machine learning models to understand the conditions under which these interventions are most effective and to predict future engagement levels.

## Motivation
Generic fitness app suggestions often fail to engage users because they don’t take into account individual lifestyles, motivations, or preferences. This project aims to improve user engagement and health outcomes through personalized, context-aware interventions. We explore how different conditions—such as user location, activity level, and demographics—impact the effectiveness of notifications.

## Project Objectives
1. **Analyze the Effectiveness of Personalized Suggestions**: Identify when and under what circumstances fitness suggestions lead to a significant increase in physical activity.
2. **User Segmentation**: Group participants by activity levels to enable more effective and tailored health interventions.
3. **Predict Future Engagement**: Develop models to forecast step counts, enabling proactive and data-driven health interventions.

---

## Project Structure
The repository is organized into the following directories and files:




---

## Data Description
### 1. **Data Sources**
The HeartSteps V1 study provided four main datasets:
- **gfsteps.csv**: Minute-by-minute step counts recorded by Google Fit devices.
- **jbsteps.csv**: Minute-by-minute step counts recorded by Jawbone devices.
- **suggestions.csv**: Information on 8,274 personalized fitness suggestions, including suggestion type and timestamps.
- **users.csv**: Demographic details of the 37 participants, including gender, age, and parental status.

### 2. **Data Cleaning**
We followed the PCS (Predictability, Computability, Stability) framework to ensure data quality:
- **Handling Missing Data**: Removed columns with more than 40% missing values and imputed missing values using median or mode.
- **Feature Alignment**: Matched step count data with suggestion times and created features like step count differences before and after suggestions.
- **Stability Checks**: Introduced random missing data to validate model performance.

### 3. **Data Splits**
The data was split into training (80%) and test (20%) sets while preserving the time-series nature to simulate real-world predictions.

---

## Methods
### 1. Feature Engineering
We engineered several features to capture relationships between step counts and suggestions:
- **Time-based Features**: Extracted features like hour of the day, day of the week, and month.
- **Lag Features**: Created lagged step counts to model trends in user activity.
- **Response Features**: Calculated step count differences before and after suggestions.

### 2. Hypothesis Testing
We conducted statistical tests to evaluate the effectiveness of suggestions:
- **Permutation Tests**: Used two-sample permutation tests to assess differences in step counts before and after receiving notifications. We tested the impact across various conditions, including:
  - User location (home, work, elsewhere)
  - User activity level (active or sedentary)
  - Demographics (gender, age group, parental status)
- **Multiple Comparisons**: Controlled for false discovery rates using the Benjamini-Hochberg procedure to prevent Type I errors.

### 3. Predictive Modeling
We used two models for forecasting future engagement:
- **ARIMA (Auto-Regressive Integrated Moving Average)**: Time-series model for sequential step count predictions.
- **XGBoost**: Gradient boosting model that performed better by capturing complex, non-linear patterns.

---

## Key Findings
1. **Hypothesis Testing Results**: 
   - Notifications significantly increased step counts for users at work, males, those under 30, active users, and users without children.
   - Significant p-values (controlled using Benjamini-Hochberg) for key conditions:
     - **At Work**: p-value = 0.001
     - **Male Users**: p-value = 0.001
     - **Under 30**: p-value = 0.0002
     - **Already Active**: p-value = 0.004
     - **No Children**: p-value = 0.004

2. **Model Performance**:
   - **ARIMA**: RMSE of 18.7
   - **XGBoost**: RMSE of 15.2, outperforming ARIMA by capturing non-linear relationships more effectively.

---

## Limitations
- **Sample Size**: With only 37 participants, the results may not generalize well to larger populations.
- **Device Variability**: Differences in data capture between Jawbone and Google Fit trackers could introduce biases, which were not fully explored.

---

## Future Work
1. **Longitudinal Analysis**: Extending the study duration could reveal insights into long-term user engagement.
2. **Advanced Models**: Experimenting with LSTM (Long Short-Term Memory) networks for better handling of sequential data.
3. **Additional Contextual Factors**: Incorporating external data like weather conditions or social activities could improve model accuracy.

---
### Authors
Abhijay Rane (ar2536@cornell.edu)
Aashish Khubchandani (akk223@cornell.edu)

### Acknowledgments
We would like to thank Cornell Tech and the HeartSteps study for providing the data and the opportunity to work on this project.


