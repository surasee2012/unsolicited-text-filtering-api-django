from joblib import load

agg_clf = load(r'text_clf_api\clf_model\\aggressive model.pkl')
obs_clf = load(r'text_clf_api\clf_model\obscene model.pkl')
spm_clf = load(r'text_clf_api\clf_model\spam model.pkl')
clf_list = [agg_clf, obs_clf, spm_clf]


def predict(x):
    results = []
    for clf in clf_list:
        pred = clf.predict(x)
        results.append(pred)
    return results


def predict_proba(x):
    results = []
    for clf in clf_list:
        proba = clf.predict_proba(x)
        proba_deci = []
        for p in proba:
            proba_deci.append([sci_to_decimals(p[0]), sci_to_decimals(p[1])])
        results.append(proba_deci)
    return results


def sci_to_decimals(sci_num):
    return "{:.4f}".format(float(str(sci_num*100)))
