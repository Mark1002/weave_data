# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:52:16 2018

@author: mark
"""

import pandas as pd
from data_preprocess.weave_data_preprocess import WeaveDataPreprocessService
import os

num_dir_path = 'D:/libon/VIEW_TEXTILE_NUMBER_DATA(2)'
num_csv_list = os.listdir(num_dir_path)
str_dir_path = 'D:/libon/VIEW_TEXTILE_STRING_DATA(2)'
str_csv_list = os.listdir(str_dir_path)

column_names = ['LISTID', 'DEVICEID', 'REPORTTIME', 'ATTRID', 'VALUE']
total_number_df = pd.DataFrame()
for i in range(len(num_csv_list[:2])):
    if i == 0:
        number_df = pd.read_csv(num_dir_path + '/' + num_csv_list[i])
    else:
        number_df = pd.read_csv(num_dir_path + '/' + num_csv_list[i], names = column_names)
    total_number_df = total_number_df.append(number_df, ignore_index=True)

string_df = pd.read_csv(str_dir_path + '/' + str_csv_list[5], names = column_names)
service =  WeaveDataPreprocessService()

string_df = service.fliter_device_by_weave_feature(string_df)
string_df['REPORTTIME'] = pd.to_datetime(string_df['REPORTTIME'].str.replace(':000000', ''))
number_df = service.fliter_device_by_weave_feature(number_df)
number_df['REPORTTIME'] = pd.to_datetime(number_df['REPORTTIME'].str.replace(':000000', ''))

number_df_preprocess = service.perform_attr_mapping(number_df)
string_df_preprocess = service.perform_attr_mapping(string_df)

merge_df = pd.merge(number_df_preprocess, string_df_preprocess, how='outer')
merge_df = merge_df.dropna()
