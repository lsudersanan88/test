"""
Exercise 11 - sklearn and pickle
For this exercise you will be writing a class for several different generator functions.

1) Write a definition called "forest_predictor". This definition should:
    - accept one mandatory string argument, a string corresponding to the file path of the CSV file to be read
    - accept one mandatory integer argument, the column containing the classification values (0 based),
            this column should be removed from your training data and stored in its own list
    - accept **kwargs for the cases:
        - header = bool   -> if True: remove the first row after reading the CSV file
        - save = string   -> check if a file with the name exists, if so, load it with pickle and do not train
            a new classifier, if the file does not exist, train a classifier and save it to this location with pickle
        - test = 2d list  -> predict the classifications of this test data set and print the resulting list
    - always return the classifier object
    - check for **kwargs using kwargs.get() and default to False or None!
        EX: header_exists = kwargs.get('header', False)
        NOT: header_exists = kwargs['header']  # crashes if header was not specified
"""
import pickle
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path


def forest_predictor(file_path, class_column, **kwargs):

    with open(file_path, 'r') as infile:
        data = [line.replace('\n', '').split(',') for line in infile]

    save = kwargs.get('save', None)
     

    if kwargs.get('header', False):
        x = data[1:]
        y = data[1:]

    if save is not None and Path(save).is_file():
        with open(save, 'rb') as infile:
            clf = pickle.load(infile)

        if kwargs.get('test', None) is None:
            return clf
        else:
            print(clf.predict(kwargs.get('test', None)))
            return clf

    else:
        x = [line[:-1] for line in x]
        y = [line[class_column] for line in y]

        clf = RandomForestClassifier(n_estimators=500)
        clf = clf.fit(x, y)

        if save is not None:
            with open(save, 'wb') as outfile:
                pickle.dump(clf, outfile)

        if kwargs.get('test', None) is None:
            return clf
        else:
            print(clf.predict(kwargs.get('test', None)))
            return clf


if __name__ == '__main__':
    clf = forest_predictor('/Users/kimayadesai/Desktop/csvfile.csv', 2, header=True, save='/Users/kimayadesai/Desktop/random_forest.p', test=[[15, 0], [18, 60000], [80, 30000]])
    print(clf.feature_importances_)
    print(clf)

