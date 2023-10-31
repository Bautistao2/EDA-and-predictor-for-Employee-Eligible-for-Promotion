# Employee Elegible for Promotion  APP (E.E.P)

HR analytics is revolutionising the way human resources departments operate, leading to higher efficiency and better results overall. Human resources has been using analytics for years; however, the collection, processing, and analysis of data has been largely manual. Given the nature of human resources dynamics and HR KPIs, the manual approach has been constraining HR. Therefore, it is surprising that HR departments opened up to the utility of machine learning so late in the game. Here is an opportunity to use predictive analytics in identifying the employees most likely to be promoted through the use of an app fed with the relevant HR information.

## Description

The client is a large MNC with 9 broad verticals across the organisation. The client faces a challenge in identifying the right people for promotion and preparing them in time. Under the current process, the final promotions are only announced after a first round of training and evaluation; and this leads to delay in employees' transition to their new roles. Hence, the company needs help in identifying the best candidates at an earlier juncture, in order to expedite the entire promotion cycle.

The company has provided the following employee datasets:

- **Emp_ID:** Unique ID for each employee
- **Department:** The department in which the employee works
- **No of Region:** Region of employment (unordered)
- **Level of Education:** Education Level
- **Gender:** Gender of employee
- **Recruitment_channel:** Channel through which employee was recruited
- **No_of_trainings_completed:** Number of other training sessions completed in previous year on soft skills, technical skills, etc.; but after which promotion did not occur.
- **Age:** Age of employee
- **Performance score:** Employee rating for the previous year
- **Length_of_service:** Length of service (in years)
- **High KPIS:** If percentage of KPIs > 80%, then 1; else 0.
- **Awards won:** If awards won during previous year, then 1; else 0.
- **Average score evaluation:** Average score in current training evaluations
- **Is_promoted:** Employee was actually promoted (this is our target variable). 1 if promoted; else 0.
## Code and Resources Used

Python Version: 3.8 Packages: pandas, numpy, datetime, scipy, sklearn, matplotlib, seaborn

## 1. Data cleaning and feature engineering:

- The "level of education" and "performance score" columns contained null values, which were addressed.
- Column labels were renamed for ease of understanding.
- Exploratory analysis was performed on the data, creating several charts to visualize the important trends.
- Extract and create new features, also the reason behind them
- Split the data into training and testing with optional portion
- Build the models with matching hyperparameter tune, choose the best model
- Encoded all categorical features

## 2. Exploratory Data Analysis:

**I used data analysis to answer a group of possible questions.**
### What percentage of employees have been promoted?
Only 8% of workers have been promoted. ![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/promotee%20employess.png)

### Are male and female employees promoted with equal frequency?
No, more men have been promoted than women. ![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/gender%20and%20promotee.png)

Although the number of trained female employees that passes is greater than that of men, this means that from a group of women and men, promotion in women is more effective.![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/ratio%20of%20promoted%20by%20gender.png)

### Which recruitment channel provides the greatest number of employees who receive promotions?
"Other" sources provide the greatest number of employees who receive promotions.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/RecruitmentChannelvsPromotee.png)

### Does the age of promoted employees have the same trend for both men and women?
Yes, employees between 26 and 39 are more likely to be promoted than other ages, for both men and women.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Ageandpromoted.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Age2.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/age3.png)

### Is there a correlation between the number of unsuccessful training sessions and employee promotion?
Yes, employees with only 1 or 2 unsuccessful training sessions are mostly promoted.![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/No%20of%20training%202.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/No_of_trainings.png)

### Is there a correlation between the employee's current performance score and being promoted?
Yes, the most common performance score for employees who were promoted is 3 or 5.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore1.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore2.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore3.png)
## 3. Building and training the prediction model
I built the model to predict which employees are likely to be promoted, based on certain employee characteristics.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Matrix_Confusion.png)

### Data preprocessing

- Changed categorical variables to numerical variables.
- Dropped the 'Emp_ID' column from the DataFrame to create the feature matrix.
- "Is promoted" is the target vector for the prediction model.
- Split the data into training and testing subsets
### Building the model
- Explored the model performance of different ML classification algorithms.
- The metric used to decide the best algorithm was accuracy.
- The most promising algorithm () was chosen, and adjusted as necessary.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/RandonForestClModel.png)
### Training the Model
- The characteristics that have the greatest impact on the prediction were calculated.
![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/FeaturesModel.png)

### 4. Insights

- The employees who were recruited via referrals from existing employees were the least often promoted, with 3% of the total promotions. Conversely, almost 42% of promoted employees were sourced via an external company. Other recruitment channels, such as internet sites, contributed 55% of the employees who were promoted. 

- At least 95% percent of promoted employees have had no more than two training sessions without promotion, and this applies for employees from all 3 hiring streams. Thus, employees who have failed only one or two training sessions should be preferred; more than two are not potentially promotable. 

- Employees between ages 26 and 39 are more likely to be promoted than other ages, for both men and women. 

- Employees with performance scores of 3 and 5 have been those most often promoted. Employees with 1, 2, and even 4 are not promoted as frequently. 

- Regarding the level of education; 67% of promoted employees have a bachelor's degree, 37% have a master's degree, and 2% have less than a high school degree. Consequently, having a degree superior to a bachelor's degree does not represent a determining factor to be promoted. 

- 56% of promoted employees have less than 5 years of experience, 33% have between 5 and 10 years, and the remaining 11% have between 10 and 20 years of experience. Thus, it can be seen that employees with 1 to 10 years of experience are those most promoted. This trends holds true for employees from all 3 hiring streams. 

- High KPIs are correlated with promotion, as at least 69% of promoted employees have high KPIs; however the opposite effect exists for awards, as 88% of promoted employees have not won any prize before.
 
- A considerable number of employees have been promoted from 4 current evaluation score groups; from 48 - 52, 58 - 61, 70 - 73, and 80 - 84. This finding implies that an employee with a low average or high average score can be promoted.

- From the correlation matrix, it can be concluded that the employee characteristics most relevant to promotion are:
- Performance score, high KPIs, length of service, age, number of previous training sessions completed without promotion, and recruitment channel.

### 5. APP 

- The application in streamlit predicts upon the introduction of certain employee information by the user or worker of the human resources department, whether an employee will be promoted or not, and in turn, it is possible for the user to make different graphs in order to analyze information in a more interactive way.
- On the left side [1] of the application the user will have the option to choose what they want to do, whether to make the prediction directly, or go to graphs, which is to view the history of promotions and create, for example, bar diagrams that allow analyzing information quickly.
- In addition, it has a section [2] that contains a link that leads to the application development company, in order to offer technical support if necessary.
- On the left side [3] is where the option that the user has chosen to perform is executed.

### 6. Dashboard POWER BI

[To view click ](https://app.powerbi.com/view?r=eyJrIjoiNmMyMDljZWMtYmRhYy00NGE4LWEyODctZGY1NDYyYjRmMDA1IiwidCI6IjMzNTQwNzQ2LTViYmMtNDRlOS04MDBmLTRjOGQ1MTJkNjQ1YyIsImMiOjl9)
![](https://github.com/Bautistao2/Potential-employee-promoted-Predictor-EDA-and-APP/blob/main/images/Screen%20Dashboard%20Power%20BI.png)


















