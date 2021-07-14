import pandas as pd
import os
from utils.logger import create_error_log
from config.constants import OUTPUT_FOLDERNAME


def create_csv(csv_filepath):
    try:
        rows = pd.read_csv(csv_filepath, chunksize=1000)
        for i, chuck in enumerate(rows):
            chuck.to_csv(os.path.join(os.getcwd(), OUTPUT_FOLDERNAME, 'out_{}.csv'.format(
                i+1)), index=False)  # i is for chunk number of each iteration
        return True
    except Exception as e:
        create_error_log(e)
