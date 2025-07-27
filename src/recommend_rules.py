import joblib

def recommend_rule(port):
    clf = joblib.load('models/decision_tree.pkl')
    prediction = clf.predict([[port]])
    return "ALLOW" if prediction[0] == 1 else "BLOCK"
