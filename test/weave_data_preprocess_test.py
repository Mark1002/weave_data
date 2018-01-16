# -*- coding: utf-8 -*-
import unittest
import pandas as pd
from weave_data_preprocess import WeaveDataPreprocessService

class WeaveTestCase(unittest.TestCase):
    
    def setUp(self):
        self.number_df = pd.read_csv('data/number_data/VIEW_TEXTILE_NUMBER_DATA(2)_517.csv')
        self.string_df = pd.read_csv('data/string_data/VIEW_TEXTILE_STRING_DATA(2)_71.csv')
        
    def test_merge_device_data(self):
        service = WeaveDataPreprocessService()
        device_data_list = service.merge_device_data(self.number_df, self.string_df)
        self.assertIsNotNone(device_data_list)

if __name__ == '__main__':
    unittest.main()
