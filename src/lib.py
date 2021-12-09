import os
import json
import logging
import pandas as pd



def printJSON(obj):
    logging.info(json.dumps(obj, sort_keys=True, indent=2))

def formatSeconds(seconds):
    time = seconds
    units = 's'

    if time >= 60:
        time /= 60.0
        units = 'm'
    
        if time >= 60:
            time /= 60.0
            units = 'h'

            if time >= 24:
                time /= 24.0
                units = 'd'

    return f'{round(time, 1)} {units}'


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def load_dataframe(path, dtype = None):
    if os.path.isfile(path):
        with open(path, 'r', encoding = 'UTF-8') as f:
            return pd.read_csv(f, header = 0, index_col = False, dtype = dtype)

def load_series(path, name = None, dtype = None):
    if os.path.isfile(path):
        with open(path, 'r', encoding = 'UTF-8') as f:
            s = pd.read_csv(f, header = None, index_col = 0, squeeze = True, dtype = dtype)

            # Define series name
            s.name = name

            # Remove axis name
            s.axes[0].name = None

            return s



def store_json(obj, path):
    with open(path, 'w', encoding='UTF-8') as f:
        json.dump(obj, f, sort_keys=True, indent=2)

def store_dataframe(df, path):
    with open(path, 'w', encoding='UTF-8') as f:
        df.to_csv(f, index = False, header = True, line_terminator = '\n')

def store_series(s, path):
    with open(path, 'w', encoding='UTF-8') as f:
        s.to_csv(f, index = True, header = False, line_terminator = '\n')