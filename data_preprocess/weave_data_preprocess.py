import pandas as pd

class DeviceData:
    def __init__(self, device_id, report_time, 
                 device_type, machine_number):
        self.device_id = device_id
        self.report_time = report_time
        self.device_type = device_type
        self.machine_number = machine_number

class WeaveDataPreprocessService:
    # attrID 的對應
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
    
    def fliter_device_by_weave_feature(self, df):
        df['ATTRID'] = df['ATTRID'].astype('str')
        attr_list = list(self._attr_mapping_dict.keys())
        is_weave_attr = list(df['ATTRID'].isin(attr_list))
        return df.iloc[is_weave_attr,]
    
    def get_attr_name(self, attr_id):
        return self._attr_mapping_dict[attr_id]
    
    def perform_attr_mapping(self, df):
        """
        用來做 attrId 的欄位轉換
        """
        device_id_list = list((df.groupby('DEVICEID').size()).index)
        attr_id_list = list((df.groupby('ATTRID').size()).index)
        preprocess_df = pd.DataFrame()
        
        for device_id in device_id_list:
            device_df = df[df['DEVICEID']==device_id]
            for i in range(len(attr_id_list)):
                attr_df = device_df[device_df['ATTRID']==attr_id_list[i]]
                attr_name = self.get_attr_name(attr_id_list[i])
                attr_df = attr_df.rename(columns={"VALUE": attr_name})
                attr_df = attr_df.drop(columns=['LISTID', 'ATTRID'])
                attr_df = attr_df.sort_values('REPORTTIME')
                if i == 0:
                    temp_df = attr_df
                else:
                    temp_df = pd.merge(temp_df, attr_df, how='outer')
            preprocess_df = preprocess_df.append(temp_df, ignore_index=True)
        return preprocess_df
