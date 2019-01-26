from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import mean_squared_log_error, mean_squared_error
xgboost_model = XGBClassifier(learning_rate=0.005, max_depth=6, n_estimators=500)

def log_loss_comparisons(data, y):
    """
    input data (feature variables) and y (labels)
    return log_loss of random forest, gradient boosting, logistic, ensemble, and xgboost models
    """

    X_train, X_test, y_train, y_test = train_test_split(data,y)

    logistic_model = LogisticRegression()
    gradient_boost_model = GradientBoostingClassifier(learning_rate=0.005, max_depth=6, max_features='log2', min_samples_leaf=4, n_estimators=500, subsample=0.25)
    random_forest_model = RandomForestClassifier(n_estimators=300, max_depth=3, verbose=1)
    xgboost_model = XGBClassifier(learning_rate=0.005, max_depth=6, n_estimators=500)

    logistic_model.fit(X_train, y_train)
    gradient_boost_model.fit(X_train, y_train)
    random_forest_model.fit(X_train, y_train)
    xgboost_model.fit(X_train, y_train)

    p_random_forest = random_forest_model.predict_proba(X_test)
    p_gradient_boost =  gradient_boost_model.predict_proba(X_test)
    p_logistic = logistic_model.predict_proba(X_test)
    p_xgboost = xgboost_model.predict_proba(X_test)


    ensemble_p = (p_random_forest[:,1] + p_gradient_boost[:,1] + p_logistic[:,1]  + p_xg_boost[:, 1])/4

    random_forest_ll = log_loss(y_test, p_random_forest )
    gradient_boost_ll = log_loss(y_test, p_gradient_boost )
    logistic_ll = log_loss(y_test, p_logistic )
    ensemble_ll = log_loss(y_test, ensemble_p )
    xgboost_ll = log_loss(y_test, p_xgboost )

    print("Ensemble Log Loss " + str(ensemble_ll))
    print("Gradient Boost Log Loss " + str(gradient_boost_ll))
    print("Random Forest Log Loss " + str(random_forest_ll))
    print("Logistic Log Loss " + str(logistic_ll))
    print("XGBoost Log Loss " + str(xgboost_ll))