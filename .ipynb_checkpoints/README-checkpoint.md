# disaster_tweet_classifier

## Recent Updates
- Yielded 0.81% accuracy with BERT pretrained model
- Removed duplicates from training data

7/25/24

- Added metafeatures. I can now convert them into parts of speech and append them to the text, or something...

6/25/24

- applied BERT pretrained model using Kaggle user [Mexwell's binary NLP classification notebook](https://www.kaggle.com/code/mexwell/bert-for-binary-classification?kernelSessionId=164569436)

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

