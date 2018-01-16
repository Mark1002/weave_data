class DeviceData:
    def __init__(self, device_id, report_time, 
                 device_type, machine_number):
        self.device_id = device_id
        self.report_time = report_time
        self.device_type = device_type
        self.machine_number = machine_number

class WeaveDataPreprocessService:
    _attr_mapping_dict = {
        '340100': 'WEAVE_MC_NO',
        '340200': 'WEAVE_CLOTH_NO',
        '340300': 'WEAVING_NO',
        '340400': 'WEAVE_STATUS_AVG',
        '340500': 'WEAVE_STATUS_LAST',
        '340600': 'WEAVE_BEATING_COUNT',
        '340700': 'WEAVE_STOP_COUNTER_AVG',
        '340800': 'WEAVE_STOP_COUNTER_LAST',
        '340900': 'WEAVE_STOP_SELVEDGE_AVG',
        '341000': 'WEAVE_STOP_SELVEDGE_LAST',
        '341100': 'WEAVE_STOP_FEELER_AVG',
        '341200': 'WEAVE_STOP_FEELER_LAST',
        '341300': 'WEAVE_STOP_CATCHING_AVG',
        '341400': 'WEAVE_STOP_CATCHING_LAST',
        '341500': 'WEAVE_MAINTEN_AREA',
        '341600': 'WEAVE_OPERATOR_AREA',
        '341700': 'WEAVE_CLASS',
        '341800': 'WEAVE_ROTATING_SPEED',
        '341900': 'WEAVE_PICKS_PER_INCH',
        '342000': 'WEAVE_TENSION',
        '342100': 'WEAVE_C_OPERATE_TIME',
        '342200': 'WEAVE_C_PRODUCE_TIME',
        '342300': 'WEAVE_C_PRODUCE_EFFECT',
        '342400': 'WEAVE_C_BEATING_COUNT',
        '342500': 'WEAVE_C_PRODUCE_LENGTH',
        '342600': 'WEAVE_C_TOTAL_STOP_TIME',
        '342700': 'WEAVE_C_BEAT_STOP_TIME',
        '342800': 'WEAVE_C_WARP_STOP_TIME',
        '342900': 'WEAVE_C_LENO_STOP_TIME',
        '343000': 'WEAVE_C_TOTAL_STOP_COUNT',
        '343100': 'WEAVE_C_BEAT_STOP_COUNT',
        '343200': 'WEAVE_C_WARP_STOP_COUNT',
        '343300': 'WEAVE_C_LENO_STOP_COUNT',
        '343400': 'WEAVE_C_DOFFING_STOP_TIME',
        '343500': 'WEAVE_C_BUTTON_STOP_TIME',
        '343600': 'WEAVE_C_ACHIEVE_STOP_TIME',
        '343700': 'WEAVE_C_DOFFING_STOP_COUNT',
        '343800': 'WEAVE_C_BUTTON_STOP_COUNT',
        '343900': 'WEAVE_C_ACHIEVE_STOP_COUNT',
        '344000': 'WEAVE_CLOTH_INDEX',
        '344100': 'WEAVE_W_SETTING_LENGTH',
        '344200': 'WEAVE_W_PRODUCE_LENGTH',
        '344300': 'WEAVE_W_PRODUCE_TIME',
        '344400': 'WEAVE_W_OPERATION_TIME',
        '344500': 'WEAVE_W_BEATING_COUNT',
        '344600': 'WEAVE_WARP_SETTING_LENGTH',
        '344700': 'WEAVE_WARP_PRODUCE_LENGTH',
        '344800': 'WEAVE_WARP_PRODUCE_TIME',
        '344900': 'WEAVE_WARP_OPERATE_TIME',
        '345000': 'WEAVING_AXLE',
        '345100': 'WEAVE_STOP_CATCHING_COUNT'
    }
    
    def fliter_divice_by_weave_feature(self, df):
        df['ATTRID'] = df['ATTRID'].astype('str')
        attr_list = list(self._attr_mapping_dict.keys())
        is_weave_attr = list(df['ATTRID'].isin(attr_list))
        return df.iloc[is_weave_attr,]
    
    def merge_device_data(self, number_df, string_df):
        col_name = ['DEVICEID', 'REPORTTIME'] + list(self._attr_mapping_dict.values())
        device_data_list = number_df
        return device_data_list
