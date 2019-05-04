from joblib import load
    
agg_clf = load(r'text_clf_api\clf_model\\aggressive model.pkl')
obs_clf = load(r'text_clf_api\clf_model\obscene model.pkl')
spm_clf = load(r'text_clf_api\clf_model\spam model.pkl')
clf_list = [agg_clf, obs_clf, spm_clf]

def predict(x):
    results = []
    for clf in clf_list:
        result = []

        pred_y = clf.predict([x])[0]
        pred_y_proba = clf.predict_proba([x])[0]

        result.append(pred_y)
        result.append([sci_to_decimals(pred_y_proba[0]), sci_to_decimals(pred_y_proba[1])])

        results.append(result)
    
    return results

def sci_to_decimals(sci_num):
    return "{:.4f}".format(float(str(sci_num*100)))