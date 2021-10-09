import yaml
import matplotlib.pyplot as plt
import numpy as np
#import joblib
from matplotlib.colors import ListedColormap
import os
import logging

def read_config(config_path):
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content

# def save_plot(df, file_name, model):
#     pass
