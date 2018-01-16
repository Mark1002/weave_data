# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:52:16 2018

@author: mark
"""

import pandas as pd
from data_preprocess.weave_data_preprocess import WeaveDataPreprocessService

number_df = pd.read_csv('data/number_data/VIEW_TEXTILE_NUMBER_DATA(2)_1.csv')
string_df = pd.read_csv('data/string_data/VIEW_TEXTILE_STRING_DATA(2)_1.csv')
service =  WeaveDataPreprocessService()

string_df = service.fliter_divice_by_weave_feature(string_df)
number_df = service.fliter_divice_by_weave_feature(number_df)

number_df.index = pd.to_datetime(number_df['REPORTTIME'].str.replace(':000000', ''))
number_df = number_df.sort_index()
