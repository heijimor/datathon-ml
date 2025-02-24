import pandas as pd
import glob
import os

def pre_processing():
  df = mergeTrainFilesToDf()
  df_converted = convertRightValues(df)
  print(df_converted.head(5))
  # df_normalized = normalize(df_converted)
  print("Pre processing initialized!")

def mergeTrainFilesToDf() -> pd.DataFrame:
  pattern = "./data/files/treino/treino_parte*.csv"
  train_files_path = os.path.abspath(pattern)
  csv_files = glob.glob(train_files_path)
  df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
  return df

def convertRightValues(df) -> pd.DataFrame:
  # df['history'] = df['history'].apply(lambda x: x.split(', '))
  # df['timestampHistory'] = df['timestampHistory'].apply(lambda x: list(map(int, x.split(', '))))
  # df['numberOfClicksHistory'] = df['numberOfClicksHistory'].apply(lambda x: list(map(int, x.split(', '))))
  # return df.explode('history')
  return df.apply(lambda row: pd.Series({
      'userId': row['userId'],
      'userType': row['userType'],
      'articleId': row['history'].split(','),
      'timestamp': row['timestampHistory'].split(','),
      'clicks': row['numberOfClicksHistory'].split(','),
      'timeOnPage': row['timeOnPageHistory'].split(','),
      'scrollPercentage': row['scrollPercentageHistory'].split(','),
      'pageVisits': row['pageVisitsCountHistory'].split(','),
      'timestamp_new': row['timestampHistory_new'].split(',')
  }), axis=1)

def normalize(df):
  cols_to_normalize = [
    'numberOfClicksHistory',
    'timeOnPageHistory',
    'scrollPercentageHistory',
    'pageVisitsCountHistory'
  ]
  for col in cols_to_normalize:
      df[col] = df[col].apply(lambda x: list(map(float, x.split(', '))) if isinstance(x, str) else [])