# Potencial Promote Employee  APP (P.P.E)


HR analytics is revolutionising the way human resources departments operate, leading to higher efficiency and better results overall. Human resources has been using analytics for years. However, the collection, processing and analysis of data has been largely manual, and given the nature of human resources dynamics and HR KPIs, the approach has been constraining HR. Therefore, it is surprising that HR departments woke up to the utility of machine learning so late in the game. Here is an opportunity to try predictive analytics in identifying the employees most likely to get promoted through the use of an APP that, by entering some information, predicts whether an employee will be promoted or not.

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

Python Version: 3.8 Packages: pandas, numpy, datetime, scipy, sklearn, matplotlib, seaborn

## 1. Data cleaning and feature engineering:

- Null values were handled located in the level of education and performance score columns
- Column labels were renamed for ease of understanding the information.
- Exploratory analysis from the data, create some charts to describe and analyze the data
- Describe the pre-processing step, how to extract and create new features, also the reason behind them
- Split the data into training and testing with optional portion
- Build the models with matching hyperparameter tune, choose the best model
- Encoded all categorical features

## 2. Exploratory Data Analysis:

**Solving the following questions**
## What percentage of employees have been promoted?

!["only 8% of workers have been promoted"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/promotee%20employess.png)

### Are promoted employees equally gendered?
!["No, more men have been promoted than women"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/gender%20and%20promotee.png)

!["Althought the number of trained female employees that passes is greater than that of men, this means that from a group of women and men, promotion in women is more effective."](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/ratio%20of%20promoted%20by%20gender.png)

### Regarding recruitment channels, which channel provides the greatest number of promoted employees?

!["Source "Other" provides a greater number of promoted employees"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/RecruitmentChannelvsPromotee.png)


### Does the age of promoted employees have the same trend for both men and women?

!["Employees between 26 and 39 are more likely to be promoted than other ages, both men and women"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Ageandpromoted.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Age2.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/age3.png)

### Is there a correlation between the number of missed training sessions and employee promotion?

!["Yes, employees with only 1 or 2 missed training sessions are mostly promoted"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/No%20of%20training%202.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/No_of_trainings.png)

### Is there a correlation between the employee's current performance score and the promotion?
!["Yes, employees with performance scores of 3 and 5 are mostly promoted"](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore1.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore2.png)

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/PerformanceScore3.png)

## 3. Build and training prediction model

I made the prediction model to know which employee will be promoted,, based on features of the employee, after having analyzed the data and the confusion matrix.

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/Matrix_Confusion.png)

To do this I follow the usual steps:

### Data preprocessing 

- Change categorical variables to numerical variables
- Dropped the 'Emp_ID' column from the DataFrame to create the feature matrix
- "Is promoted" is the target vector to the prediction model
- Split the data into training and testing subsets
### Build a model

- Exploring model performance of different ML clasification algorithms
- The metric used to decide the best algorithm was accuracy.
- The most promising algorithm () was adjusted.

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/RandonForestClModel.png)


### Training Model

- The characteristics that have the greatest impact on the prediction were calculated.

![](https://github.com/Bautistao2/Potential-employee-promoted-APP/blob/main/images/FeaturesModel.png)

### 4. Insights

- Regarding the recruitment channel, the recruitment channel that contributes the least promotions is    the  one in which company employees refer their acquaintances, with 3% of the total promotions, on the o other hand, using external companies has contributed close to 42% of promoted employees, while other types of recruitment such as internet pages have contributed 55% of the promotions, in conclusion hiring through referrals and external companies should be reduced and the search for candidates through internet pages that present more skills should be increased.
- Employees who have missed a maximum of two training sessions should be preferred; more than two are not potentially promotable.
- Employees between 26 and 39 are more likely to be promoted than other ages, both men and women.
- Employees with performance scores of 3 and 5 have mostly been promoted, employees with 1, 2 and even 4 are not potentially promotable.
- Employees with less than 8 years of seniority in the company are mostly promoted; the older they are, the lower the employee promotion, with seniority inversely proportional to the number of promotions.
- The number of employees promoted with high KPIS is twice the number of employees promoted without high KPIS, this means that the value of the KPIS measured on the employees directly affects the probability of being promoted.
- It is curious that the same does not happen with employees who have won awards in the company, there are much more promoted employees who have not won any awards than those who have won, this means that it does not represent an advantage when it comes to to promote but on the contrary, employees with awards may feel more relaxed and do not put as much effort into promotion tests.
- An employee with any average score evaluations can be promoted
- The age of the company's employees ranges between 20 and 60 years old and although there are promoted employees, employees aged between 25 and 40 are potentially promotable, the number of promoted employees increases from 27 to 35 years old.
- In relation to employees who apply for promotion and those who pass, training to be promoted is more effective in workers who have been employed through a referral, over sourcing and other recruitment channel
- The trend in the number of past trainings completed in promoted employees remains the same for the three recruitment channels used by the company.
- The trend in the length of service in promoted employees remains the same for the three recruitment channels used by the company.
- Regarding the level of education of the employees, the vast majority of employees promoted with only 1 and 2 training sessions missed only had a bachelor's degree, and not a master's degree, that is, having a master's degree does not indicate a greater probability of promotion.
- From the data matrix it can be concluded that of all the employee features, those that have the most relationship with employee promotion are:
- Performance score, High KPIS, Awards won and Average score evaluations.

### 5. APP 

- The application in streamlit predicts upon the introduction of certain employee information by the user or worker of the human resources department, whether an employee will be promoted or not, and in turn, it is possible for the user to make different graphs in order to analyze information in a more interactive way.
- On the left side [1] of the application the user will have the option to choose what they want to do, whether to make the prediction directly, or go to graphs, which is to view the history of promotions and create, for example, bar diagrams that allow analyzing information quickly.
- In addition, it has a section [2] that contains a link that leads to the application development company, in order to offer technical support if necessary.
- On the left side [3] is where the option that the user has chosen to perform is executed.



















