import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#The following function will create a baseline using the dummy classifier.
def get_baseline(X_train, y_train):
    #Find the mode of 'churn' values
    mode = y_train.value_counts().idxmax()

    baseline = DummyClassifier(strategy = 'constant', constant = mode)
    baseline.fit(X_train, y_train)
    
    return baseline.score(X_train, y_train)

#The following function will create and test many different Random Forest Classifier models.
#The final output will be a dataframe displaying results.
def compare_models(X_train, y_train, X_validate, y_validate):
    model_dicts = []

    #Starting from 2 in order to avoid warnings
    for num in range(2, 11):
        #Now create a new loop that runs through different min_samples_leaf values
        for val in range(1, 26):
            #Instantiate new model
            clf = RandomForestClassifier(random_state = 123, max_depth = num, min_samples_leaf = val)
        
            #Fit the model
            clf.fit(X_train, y_train)
        
            #Score the model on training data
            train_score = clf.score(X_train, y_train)
        
            #Make predictions on validate data to use in confusion matrix
            clf_preds = clf.predict(X_validate)
            
            #Use confusion matrix to find TP, FP, TN, FN
            tp = confusion_matrix(y_validate, clf_preds)[1][1]
            fp = confusion_matrix(y_validate, clf_preds)[0][1]
            tn = confusion_matrix(y_validate, clf_preds)[0][0]
            fn = confusion_matrix(y_validate, clf_preds)[1][0]
            #Score the model on validate data
            validate_score = clf.score(X_validate, y_validate)
        
            #Create a dictionary for model values
            output = {
                'max_depth':num,
                'min_samples_leaf': val,
                'True Positves': tp,
                'False Positives': fp,
                'True Negatives': tn,
                'False Negatvies': fn,
                'Precision': tp / (tp + fp),
                'Recall': tp / (tp + fn),
                'Training Score': train_score,
                'Validate Score': validate_score,
                'Score Difference': train_score - validate_score
            }
            
            model_dicts.append(output)

    return pd.DataFrame(model_dicts)

#The following function will evaluate the chosen model on the test data set and return the clf model.
def test_model(X_train, y_train, X_validate, y_validate, X_test, y_test):
    #Instantiate the model
    clf = RandomForestClassifier(random_state = 123, max_depth = 5, min_samples_leaf = 15)

    #Fit the model
    clf.fit(X_train, y_train)

    #Score the model on training data
    train_score = clf.score(X_train, y_train)

    #Score the model on validate data
    validate_score = clf.score(X_validate, y_validate)

    #Score the model on test data
    test_score = clf.score(X_test, y_test)

    #Make predictions on test data to use in confusion matrix
    clf_preds = clf.predict(X_test)

    #Use confusion matrix to find TP, FP, TN, FN
    tp = confusion_matrix(y_test, clf_preds)[1][1]
    fp = confusion_matrix(y_test, clf_preds)[0][1]
    tn = confusion_matrix(y_test, clf_preds)[0][0]
    fn = confusion_matrix(y_test, clf_preds)[1][0]


    #Create a dictionary for model values
    output = {
        'max_depth':5,
        'min_samples_leaf': 15,
        'True Positves': tp,
        'False Positives': fp,
        'True Negatives': tn,
        'False Negatvies': fn,
        'Precision': tp / (tp + fp),
        'Recall': tp / (tp + fn),
        'Training Score': train_score,
        'Validate Score': validate_score,
        'Test Score': test_score,
        'Score Difference': validate_score - test_score
    }

    test_set = []
    test_set.append(output)
    pd.DataFrame(test_set)

    return clf

#The following function will create and return a df of predictions for the final deliverable.
#You can take the returned data frame and turn it into a .csv file.
def get_preds_df(test_explore, clf, X_test):
    #Build a df containing churn proba
    churn_proba = clf.predict_proba(X_test)
    proba_df = pd.DataFrame(churn_proba, columns = ['probability_not_churned', 'probability_churned'])

    #Add each column one at a time
    reset_test = test_explore.reset_index()
    reset_test['probability_not_churned'] = proba_df['probability_not_churned']
    reset_test['probability_churned'] = proba_df['probability_churned']

    #Now add the test predictions
    reset_test['predicted'] = clf_preds

    #Now select only the columns required in a new data frame.
    csv_df = reset_test[['customer_id', 'probability_not_churned', 'probability_churned', 'predicted']]

    return csv_df
