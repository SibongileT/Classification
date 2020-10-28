from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report,confusion_matrix,plot_confusion_matrix
from sklearn.metrics import roc_curve , roc_auc_score
from sklearn.model_selection import GridSearchCV
import pickle

#Import all the models that I will use
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier, VotingClassifier
import xgboost as xgb

def get_metrics(X,y,X_val,y_val,model,name):
    model = model.fit(X,y)
    y_pred = model.predict(X_val)
    print('{} train score: {:.3f}'.format(name,model.score(X,y)))
    print('{} test score: {:.3f}'.format( name, model.score(X_val,y_val)))
    print(classification_report(y_val, y_pred))
    fig, ax = plt.subplots(figsize=(7, 7))
    print(plot_confusion_matrix(model, X_val, y_val, ax=ax))
    return model

def voting_classifier(model_list,voting):
    voting_classifier= VotingClassifier(estimators=model_list,
                                    voting=voting, #<-- sklearn calls this hard voting
                                    n_jobs=-1)
    voting_classifier.fit(X_train_scaled, y_train)
    y_pred = voting_classifier.predict(X_val_scaled)
    print(accuracy_score(y_val, y_pred))
    print(classification_report(y_val, y_pred))
    fig, ax = plt.subplots(figsize=(7, 7))
    print(plot_confusion_matrix(voting_classifier, X_val_scaled, y_val, ax=ax))
    return voting_classifier
