# Panda
import os
from time import sleep

import pandas
from csv import reader
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# coulm result
coulm_result = []

# trainSet

csv_path = "train.csv"


# train set result
class Result:
    HOME = "HOME"
    AWAY = "AWAY"
    Draw = "DRAW"


# data frame one , data frame away
def get_winner(home_frame, away_frame):
    result = "draw"
    m_data_frame = []
    for i in range(0, len(home_frame)):
        away = away_frame[i]
        home = home_frame[i]
        if away > home:
            result = Result.AWAY
        elif home > away:
            result = Result.HOME
        else:
            result = Result.Draw
        m_data_frame.append(result)
    dict = {"winner": m_data_frame}
    return pandas.DataFrame(dict)


def train():
    global csv_path
    col_updated = ['Division', 'Time', 'home_team', 'away_team', 'Referee', 'home_coef', 'draw_coef', 'away_coef']
    Match_set = pandas.read_csv(csv_path, nrows=25)
    Match_set['winner'] = (get_winner(Match_set['full_time_home_goals'], Match_set['full_time_away_goals']))
    match_set = Match_set.copy()
    match_set = pandas.get_dummies(match_set, columns=col_updated)
    # split for train and predict
    X = match_set.drop(['winner'], axis=1)
    Y = match_set['winner']
    # MARK:-
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20, random_state=0)
    DT_model = DecisionTreeRegressor(max_depth=5).fit(X_train, Y_train)
    DT_predict = DT_model.predict(X_test)  # Predictions on Testing data
    print(DT_predict)


if __name__ == '__main__':
    # read()
    train()
# supervised learning
# buildResult()

