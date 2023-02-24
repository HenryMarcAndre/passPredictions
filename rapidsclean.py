# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

df = pd.read_csv("rapids.csv")

df['distanceFromBall'] = np.sqrt((df['PlayerX'] - df['BallX']) ** 2 + (df['PlayerY'] - df['BallY']) ** 2)
df['distanceFromGoal'] = np.sqrt((df['BallX'] - 58) ** 2 + df['BallY'] ** 2)

df['teammates_within_5'] = ((df['distanceFromBall'] <= 5) & (df['IsTM'] == 1) & (df['IsePlayer'] == 0)).astype(int)
df['opponents_within_5'] = ((df['distanceFromBall'] <= 5) & (df['IsTM'] == 0)).astype(int)
df['teammates_within_10'] = ((df['distanceFromBall'] <= 10) & (df['IsTM'] == 1) & (df['IsePlayer'] == 0)).astype(int)
df['opponents_within_10'] = ((df['distanceFromBall'] <= 10) & (df['IsTM'] == 0)).astype(int)
df['teammates_within_15'] = ((df['distanceFromBall'] <= 15) & (df['IsTM'] == 1) & (df['IsePlayer'] == 0)).astype(int)
df['opponents_within_15'] = ((df['distanceFromBall'] <= 15) & (df['IsTM'] == 0)).astype(int)
df['teammates_ahead_of_ball'] = ((df['PlayerX'] > df['BallX']) & (df['IsTM'] == 1) & (df['IsePlayer'] == 0)).astype(int)
df['opponents_ahead_of_ball'] = ((df['PlayerX'] > df['BallX']) & (df['IsTM'] == 0)).astype(int)

df.tail()
df.to_csv('rapidsNew.csv', index = False)

new_df = df.groupby('GameEventID')[['teammates_within_5','opponents_within_5','teammates_within_10','opponents_within_10','teammates_within_15','opponents_within_15','teammates_ahead_of_ball','opponents_ahead_of_ball']].sum()
new_df  = new_df.reset_index()

#new_df.to_csv('rapidsPassData.csv', index=False)