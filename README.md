# Potencial Promote Employee  APP (P.P.E)


HR analytics is revolutionising the way human resources departments operate, leading to higher efficiency and better results overall. Human resources has been using analytics for years. However, the collection, processing and analysis of data has been largely manual, and given the nature of human resources dynamics and HR KPIs, the approach has been constraining HR. Therefore, it is surprising that HR departments woke up to the utility of machine learning so late in the game. Here is an opportunity to try predictive analytics in identifying the employees most likely to get promoted through the use of an app that, by entering some information, predicts whether an employee will be promoted or not.


## Goal

Build model to predict eligibility for an employee to be promoted or not

## Description

The client is a large MNC and they have 9 broad verticals across the organisation. One of the problem your client is facing is around identifying the right people for promotion (only for manager position and below) and prepare them in time. Currently the process, they are following is:

-They first identify a set of employees based on recommendations/ past performance
Selected employees go through the separate training and evaluation program for each vertical. These programs are based on the required skill of each vertical
At the end of the program, based on various factors such as training performance, KPI completion (only employees with KPIs completed greater than 60% are considered) etc., employee gets promotion.

-For above mentioned process, the final promotions are only announced after the evaluation and this leads to delay in transition to their new roles. Hence, company needs your help in identifying the eligible candidates at a particular checkpoint so that they can expedite the entire promotion cycle.

-They have provided multiple attributes around Employee's past and current performance along with demographics. Now, The task is to predict whether a potential promotee at checkpoint in the test set will be promoted or not after the evaluation process.

- **Emp_ID:** Unique ID for employee
- **Department:** Department of employee
- **No of Region:** Region of employment (unordered)
- **Level of Education:** Education Level
- **Gender:** Gender of Employee
- **Recruitment_channel:** Channel of recruitment for employee
- **No_of_trainings_completed:** no of other trainings completed in previous year on soft skills, technical skills etc.
- **Age:** Age of Employee
- **Performance score:** Employee Rating for the previous year
- **Length_of_service:** Length of service in years
- **High KPIS:** if Percent of KPIs(Key performance Indicators) >80% then 1 else 0
- **Awards won:** if awards won during previous year then 1 else 0
- **Average score evaluation:** Average score in current training evaluations
- **Is_promoted:** (Target) for promotion
## Code and Resources Used

Python Version: 3.7 Packages: pandas, numpy, datetime, scipy, sklearn, matplotlib, seaborn

## 1. Data cleaning and feature engineering:

-Null values were handled located in the level of education and performance score columns
-Column labels were renamed for ease of understanding the information.
-Exploratory analysis from the data, create some charts to describe and analyze the data
-Describe the pre-processing step, how to extract and create new features, also the reason behind them
-Split the data into training and testing with optional portion
-Build the models with matching hyperparameter tune, choose the best model
-Encoded all categorical features

## 2. Exploratory Data Analysis:

**Solving the following questions**

## What percentage of employees have been promoted?

![only 8% of workers have been promoted](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/promotee%20employess.png)

### Are promoted employees equally gendered?

![No, more men have been promoted than women](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/gender%20and%20promotee.png)

![Althought the number of trained female employees that passes is greater than that of men, this means that from a group of women and men, promotion in women is more effective.](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/ratio%20of%20promoted%20by%20gender.png)

### Regarding recruitment channels, which channel provides the greatest number of promoted employees?

![Source "Other" provides a greater number of promoted employees](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/RecruitmentChannelvsPromotee.png)


### Does the age of promoted employees have the same trend for both men and women?

![Employees between 26 and 39 are more likely to be promoted than other ages, both men and women]()

















