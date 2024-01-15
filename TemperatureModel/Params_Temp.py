import pandas as pd
import numpy as np
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import numpy as np
import string
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from tensorflow.keras.utils import to_categorical
import itertools
import random
import pickle

mean_values = {'station': 13.014101212440696,
 'Present_Tmax': 29.748365840801263,
 'Present_Tmin': 23.195809172377437,
 'LDAPS_RHmin': 56.72496867696231,
 'LDAPS_RHmax': 88.3608233703677,
 'LDAPS_Tmax_lapse': 29.62012769006853,
 'LDAPS_Tmin_lapse': 23.511786156327094,
 'LDAPS_WS': 7.0940966991598575,
 'LDAPS_LH': 62.492606287988,
 'LDAPS_CC1': 0.36851020603927254,
 'LDAPS_CC2': 0.3555275409410912,
 'LDAPS_CC3': 0.3175460089503163,
 'LDAPS_CC4': 0.2982675804466131,
 'LDAPS_PPT1': 0.5890079784346336,
 'LDAPS_PPT2': 0.4807383624951239,
 'LDAPS_PPT3': 0.2750067244948603,
 'LDAPS_PPT4': 0.265372529469689,
 'lat': 37.54479229045862,
 'lon': 126.99142000527148,
 'DEM': 61.918136478650496,
 'Slope': 1.2597548892988932,
 'Solar radiation': 5343.724207856747}

std_dev_values = {'station': 7.21785759014952,
 'Present_Tmax': 2.967400528041638,
 'Present_Tmin': 2.4008798179654693,
 'LDAPS_RHmin': 14.626558912477066,
 'LDAPS_RHmax': 7.199456317596653,
 'LDAPS_Tmax_lapse': 2.9434960627280127,
 'LDAPS_Tmin_lapse': 2.342578872042559,
 'LDAPS_WS': 2.1770337242580364,
 'LDAPS_LH': 33.686157816162066,
 'LDAPS_CC1': 0.2622598031267863,
 'LDAPS_CC2': 0.2579216537142023,
 'LDAPS_CC3': 0.24983302499916893,
 'LDAPS_CC4': 0.25339209056101614,
 'LDAPS_PPT1': 1.927576685315817,
 'LDAPS_PPT2': 1.7433272181988837,
 'LDAPS_PPT3': 1.1460867273035549,
 'LDAPS_PPT4': 1.179661077543039,
 'lat': 0.05042819046361885,
 'lon': 0.07921972556984916,
 'DEM': 54.32352900241009,
 'Slope': 1.3727482718946689,
 'Solar radiation': 429.78256146513166}

param_ml_input = ['station', 'Present_Tmax', 'Present_Tmin', 'LDAPS_RHmin', 'LDAPS_RHmax', 'LDAPS_Tmax_lapse', 'LDAPS_Tmin_lapse', 'LDAPS_WS', 'LDAPS_LH', 'LDAPS_CC1', 'LDAPS_CC2', 'LDAPS_CC3', 'LDAPS_CC4', 'LDAPS_PPT1', 'LDAPS_PPT2', 'LDAPS_PPT3', 'LDAPS_PPT4', 'lat', 'lon', 'DEM', 'Slope', 'Solar radiation']

def getingX(value_list):
 X_scaled = pd.DataFrame()
 X_data = pd.DataFrame(value_list, columns=param_ml_input)
 for column in X_data.columns:
  X_scaled[column] = (X_data[column] - mean_values[column]) / std_dev_values[column]
 return np.array(X_scaled)
