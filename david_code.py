import datetime as dt
import pandas as pd

def get_days(timedelta_obj):
    obj = str(timedelta_obj)
    return int(obj.split(' ')[0])#get just the days

def make_dummies(test_col, train_unique_vals, col_name):

    """
    Return a df containing len(train_unique_vals) columns for 
    each unique value in train_unique_vals. If the test_col has more 
    unique values that are not seen in train_unique_vals, value
    will be 0
    """

    dummies = {}
    for val in train_unique_vals:
        dummies[col_name + '_' + val] = (test_col == val).astype(int)
    return pd.DataFrame(dummies, index = test_col.index)

def make_dummies_dataframe(data, categories):

    """
    creates dummy variables for multiple categories
    ex categories = ['city', 'phone'], make_dummies_dataframe(data, categories)

    """
    dummy_dfs = []
    for category in categories:
        temp_df = make_dummies(data[category], data[category].unique(), category)
        dummy_dfs.append(temp_df)
    for i in dummy_dfs:
        data_transformed = pd.concat([data, i], axis=1)
        data = data_transformed
    return data_transformed


def datetime_cleans(df):
    df['License.Issue.Date'] = pd.to_datetime(df.loc[:, 'License.Issue.Date'], )
    df['Graduation.Date'] = pd.to_datetime(df.loc[:, 'Graduation.Date'], )
    df['approach.date'] = pd.to_datetime(df.loc[:, 'approach.date'], )

    date_today = dt.datetime.now()
    df['years_in_state'] = df['License.Issue.Date'].apply(lambda x: date_today - x)
    df['years_in_state'] = round(df['years_in_state'].apply(lambda x: get_days(x)) / 365, 2)

    df['years_in_practice'] = df['Graduation.Date'].apply(lambda x: date_today - x)
    df['years_in_practice'] = round(df['years_in_practice'].apply(lambda x: get_days(x)) / 365, 2)

    categories = ['broker.ID', 'City']
    df = make_dummies_dataframe(df, categories)
    df.drop(columns = categories, inplace=True)

    return df

