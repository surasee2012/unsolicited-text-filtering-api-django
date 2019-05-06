from joblib import load

agg_clf = load(r'text_clf_api\clf_model\\aggressive model.pkl')
obs_clf = load(r'text_clf_api\clf_model\obscene model.pkl')
spm_clf = load(r'text_clf_api\clf_model\spam model.pkl')
clf_dict = {"agg": agg_clf, "obs": obs_clf, "spm": spm_clf}


def predict(clfs, x):
    results = []
    for clf in clfs:
        pred = clf_dict[clf].predict(x)
        results.append(pred)
    return results


def predict_proba(clfs, x):
    results = []
    for clf in clfs:
        proba = clf_dict[clf].predict_proba(x)
        proba_deci = []
        for p in proba:
            proba_deci.append([sci_to_decimals(p[0]), sci_to_decimals(p[1])])
        results.append(proba_deci)
    return results


def sci_to_decimals(sci_num):
    return "{:.4f}".format(float(str(sci_num*100)))
