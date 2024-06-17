# disaster_tweet_classifier

## Recent Updates
- Yielded .68 accuracy with LogisticRegression model
- Began progress with deep learning model

6/17/24

- implemented count_digits, which did increase logistic and linear regression model results
- added differing words for feature matrix

6/11/24

- Implemented count_periods(), only to see a decrease in the baseline model results
- Implemented Guassian and Bernoulli Naive Bayes
    - Yielded .73 accuracy with Gaussian Naive Bayes
- Began deep learning model

  
6/10/24

- Updated the function tweet_processing() to use the new function from `funcs.py`, capitals_vs_sentence_len().
    - ran into issues with assigning a series to another series, not the values
- Began testing with GridSearchCV
- Yielded .67 accuracy with LogisticRegression model

  
## To Do
- Generate additional features
- [tune deep learning model](https://machinelearningmastery.com/binary-classification-tutorial-with-the-keras-deep-learning-library/)