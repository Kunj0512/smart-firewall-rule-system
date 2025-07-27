from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(df):
    X = df[['port']]
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    joblib.dump(clf, 'models/decision_tree.pkl')
