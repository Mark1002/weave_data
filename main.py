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

string_df = service.fliter_device_by_weave_feature(string_df)
string_df['REPORTTIME'] = pd.to_datetime(string_df['REPORTTIME'].str.replace(':000000', ''))
number_df = service.fliter_device_by_weave_feature(number_df)
number_df['REPORTTIME'] = pd.to_datetime(number_df['REPORTTIME'].str.replace(':000000', ''))

number_df_preprocess = service.perform_attr_mapping(number_df)

device_id_list = list((string_df.groupby('DEVICEID').size()).index)
attr_id_list = list((string_df.groupby('ATTRID').size()).index)
string_df_preprocess = pd.DataFrame()

for device_id in device_id_list:
    device_df = string_df[string_df['DEVICEID']==device_id]
    for i in range(len(attr_id_list)):
        attr_df = device_df[device_df['ATTRID']==attr_id_list[i]]
        attr_name = service.get_attr_name(attr_id_list[i])
        attr_df = attr_df.rename(columns={"VALUE": attr_name})
        attr_df = attr_df.drop(columns=['LISTID', 'ATTRID'])
        attr_df = attr_df.sort_values('REPORTTIME')
        if i == 0:
            temp_df = attr_df
        else:
            temp_df[attr_name] = attr_df[attr_name].values
    string_df_preprocess = string_df_preprocess.append(temp_df, ignore_index=True)
