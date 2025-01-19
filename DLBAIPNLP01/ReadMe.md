# Sentiment Analysis on Movie Reviews  
A comprehensive sentiment analysis project using the IMDB dataset. This project applies both traditional machine learning models (Logistic Regression, Random Forest, and SVM) and a deep learning model (LSTM) to classify movie reviews as positive or negative.  

Link to my Medium Post: https://medium.com/@fatimakhongulomova/from-logistic-regression-to-lstm-a-sentiment-analysis-case-study-on-movie-reviews-66fabd8cfaaf
## Overview  
This project demonstrates the use of various machine learning and deep learning techniques to perform binary sentiment classification on movie reviews. The IMDB dataset, a balanced and widely-used dataset for sentiment analysis, is used for this task. The models are evaluated using key metrics such as accuracy, precision, recall, and F1-score.  

## Dataset  
- **Source**: The IMDB dataset, containing 50,000 labeled movie reviews (25,000 positive and 25,000 negative).  
- **Purpose**: Binary classification of sentiment as positive or negative.  

## Process  

### 1. Data Preprocessing  
To prepare the raw text data for model training, the following preprocessing steps were applied:  
- **Text Cleaning**: Removal of HTML tags, special characters, and numbers.  
- **Tokenization**: Splitting reviews into individual words.  
- **Stop Words Removal**: Removing common words like "and," "the," and "is."  
- **Lemmatization**: Reducing words to their base form.  

### 2. Model Training and Testing  
The following models were implemented and tested:  
1. **Logistic Regression**: A simple yet effective baseline for binary classification.  
2. **Random Forest**: Combines multiple decision trees for robust classification.  
3. **Support Vector Machines (SVM)**: Handles high-dimensional data and creates hyperplanes for separation.  
4. **Long Short-Term Memory (LSTM)**: A deep learning model designed for sequential data, addressing the vanishing gradient problem.  

### 3. Evaluation Metrics  
The models were evaluated using the following metrics:  
- **Accuracy**: Percentage of correct predictions.  
- **Precision**: Proportion of correctly predicted positive observations.  
- **Recall**: Proportion of actual positive observations that were correctly predicted.  
- **F1-Score**: Harmonic mean of precision and recall.  

## Results  
| **Model**            | **Accuracy** | **Precision** | **Recall** | **F1-Score** |  
|-----------------------|--------------|---------------|------------|--------------|  
| Logistic Regression   | 88%          | 88%           | 88%        | 88%          |  
| Random Forest         | 85%          | 85%           | 85%        | 85%          |  
| SVM                   | 90%          | 91%           | 90%        | 90%          |  
| LSTM                  | 88%          | 89%           | 88%        | 88%          |  

### Key Observations  
- **SVM** achieved the highest accuracy (90%) but had a long runtime.  
- **Logistic Regression** provided competitive performance with the shortest runtime, making it efficient for large datasets.  
- **LSTM** excelled in handling sequential data and offered competitive performance.  

## Key Learnings  
- **Preprocessing Matters**: Techniques like TF-IDF significantly impact model performance.  
- **Understanding Model Behavior**: Each model has strengths and weaknesses, and their suitability depends on the dataset and application.  

## Future Work  
- Experiment with advanced embedding techniques like Word2Vec and BERT.  
- Apply this framework to a multiclass sentiment analysis task.  
- Optimize model parameters further for improved performance.  

## How to Run the Code  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/your-repository-name.git  
