# House-loan-prediction

Abstract 

With the rapid evolution of financial technology, accurately predicting the approval of home mortgage loan applications has become crucial for banks and financial institutions to optimize their core operations. This project is a quintessential binary classification challenge, aiming to employ the HMDA (Home Mortgage Disclosure Act) dataset to build machine learning models that forecast the success rate of loan applications. The binary classification task hinges on determining whether a loan will be approved or not, based on a range of features provided by the HMDA dataset, including applicant information, loan amounts, property details, and geographical locations.

The project commences with thorough data preprocessing, which involves addressing missing values, encoding categorical variables, and normalizing features to create a robust foundation for the modeling process. Subsequent to preprocessing, a slew of machine learning algorithms—such as Random Forests, Gradient Boosting Trees, and Logistic Regression—are deployed to tackle this binary classification task. The efficacy of these models is meticulously gauged using metrics like accuracy, recall, and F1 score, which are particularly vital in evaluating binary classifiers. In addition, an analysis of feature importance is conducted to shed light on the predictive power of each feature, thereby offering invaluable guidance for the formulation of future credit policies.

The anticipated outcome of this project is the enhancement of financial institutions' capabilities to make precise loan approval decisions, effectively mitigate risks, and consequently, elevate customer satisfaction. Moreover, an in-depth analysis of the HMDA dataset is projected to uncover significant trends and patterns within the mortgage market, which can yield actionable insights for policy-making. In essence, the research findings are expected to further the advancement of inclusive financial services, contributing to the establishment of a fair and transparent housing loan market landscape.

Methodology

1. Data Acquisition & Description:
In this phase, we will collect and import the HMDA dataset, followed by a comprehensive description of each attribute within the data. This includes understanding the variables related to loan applicants, loan characteristics, property details, and loan outcomes. The main objective is to develop a thorough familiarity with the data, including its structure, coverage, and potential limitations that could impact the analysis.

2. Data Pre-processing:
Pre-processing involves cleaning the dataset by handling missing values, outliers, and errors that may skew the results. We will standardize and normalize numerical data to ensure uniformity across different scales. Categorical variables will be encoded appropriately, converting them into a format that can be provided to machine learning models. This stage is crucial for preparing the dataset for reliable and accurate modeling.

3. Exploratory Data Analysis (EDA):
The EDA phase will delve into visual and statistical examinations of the data to uncover patterns, detect anomalies, identify significant variables, and test underlying assumptions. This step is essential for gaining insights into the data's distribution and relationships between variables.

4. Post Data Processing & Feature Selection:
After EDA, we will perform additional data processing based on insights gained. This includes feature engineering where new features may be constructed and feature selection where irrelevant or less important features may be removed. The goal is to refine the dataset so that the models can focus on the most informative attributes.

5. Model Development & Evaluation:
We will develop multiple machine learning models to predict loan approval outcomes and evaluate their performance using appropriate metrics.

    5.1 Baseline Models:
    As a starting point, we will implement the following baseline models without any oversampling techniques:

    5.1.1 Logistic Regression:
    We will use logistic regression as a probabilistic approach to model the binary outcome of loan approval.

    5.1.2 Decision Tree Classifier:
    This model will allow us to interpret the decision-making process with a series of rule-based conditions.

    5.1.3 Random Forest Classifier:
    A robust ensemble method that improves predictive accuracy by combining the decisions of multiple decision trees.

    5.2 Oversampling Models:
    To address class imbalance in the dataset, we will implement oversampling techniques and then apply the same set of models to compare the performance improvements:

    5.2.1 Logistic Regression:
    The oversampled dataset will be used to train a logistic regression model to see if model performance improves with a balanced dataset.

    5.2.2 Decision Tree Classifier:
    A decision tree classifier will be applied to the balanced dataset to identify how class proportions affect the tree's decisions.

    5.2.3 Random Forest Classifier:
    Finally, the random forest model will be trained on the oversampled data, anticipating an improvement in handling minority class predictions.

Each model's performance will be assessed using metrics such as accuracy, precision, recall, F1-score, and AUC-ROC curves. We will also analyze the trade-offs between model complexity and predictive power, ensuring that the final models are both accurate and interpretable.
