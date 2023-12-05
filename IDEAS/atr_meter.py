import pandas_ta as ta


class IDEASS():
    def __init__(self) -> None:
        pass
    # ///////////////////////////////////////////////////////////////////////////
    def atr_ranging(self, data_list):
            
        for i, data in enumerate(data_list):
            try:
                atr_data_UnrangedList = self.calculate_steck_atrS(data[f"Average_data"])
                last_atr = atr_data_UnrangedList[-1]
                atr_data_RangedList = sorted(atr_data_UnrangedList) 
                strongest_atr = atr_data_RangedList[-1]
                atr_level_100 = round((last_atr *100 / strongest_atr), 2)  
                data_list[i]["Atr_percentage_level"] = atr_level_100   
                data_list[i]["Last_atr"] = last_atr
            except Exception as ex:
                    print(ex)
                # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

    def calculate_steck_atrS(self, data):        
        data.sort_index(ascending=True, inplace=True) 
        atr_data_UnrangeList = []
        for i in range(20, len(data)):
            atr_data = ta.atr(data['High'].iloc[:i], data['Low'].iloc[:i], data['Close'].iloc[:i], timeperiod=i)                          
            atr_data = atr_data.dropna()
            last_atr = float(atr_data.iloc[-1])
            # print(last_atr)
            atr_data_UnrangeList.append(last_atr)
        # print(sorted(atr_data_rangeList), last_atr)
        return atr_data_UnrangeList
    # ///////////////////////////////////////////////////////////////////////////