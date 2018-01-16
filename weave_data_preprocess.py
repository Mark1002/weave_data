class DeviceData:
    def __init__(self, device_id, report_time, 
                 device_type, machine_number):
        self.device_id = device_id
        self.report_time = report_time
        self.device_type = device_type
        self.machine_number = machine_number

class WeaveDataPreprocessService:
    def merge_device_data(self, number_df, string_df):
        device_data_list = number_df
        return device_data_list
