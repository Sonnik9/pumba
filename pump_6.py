# Фев 5
# 🔥 Cryptos Pump Hunter captured high volatility symbols in real-time, Up to 40 symbols can be monitored at same time.
# Help you find the most profitable symbol with excellent visualization.


# 🔥 Indicator Design logic

# 🎯 The core pump/dump logic is quite simple

# 1. calc past bars highest and lowest High price, get movement by this formula
# " movement = (highest - lowest) / lowest * 100 "
# 2. order by 'movement' value descending, you will get a volatility List
# 3. use Table tool display List, The higher the 'movement', the higher the ranking.


# 🔥 Settings

# 🎯 2 input properties impact on the results, 2 input impact on display effects, others look picture below.

# pump_bars_cnt: lookback bar to calc pump/dump
# resolution for pump: 1min to 1D
# show_top1: when ranking list top1 change, will draw a label
# show pump: when symbol over threhold, draw a pump lable


# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © liwei666
# //@version=5
# // # ========================================================================= #
# // #                   |Cryptos Pump Hunter   Indicator  |
# // # ========================================================================= #
# indicator(
#  title                = "Cryptos Pump Hunter[liwei666]",
#  shorttitle           = "Cryptos Pump Hunter",
#  overlay              =  true,
#  max_lines_count                 =  500, 
#  max_labels_count                =  500, 
#  max_boxes_count                 =  500,
#  max_bars_back = 5000
#  )
# // # ========================================================================= #
# // #                   |Cryptos Pump Hunter   Indicator  |
# // # ========================================================================= #

# // BINANCE:BTCUSDTPERP,BINANCE:ETHUSDTPERP,BINANCE:LTCUSDTPERP,BINANCE:LUNCBUSD,BINANCE:SOLUSDT,BINANCE:ANCBUSDPERP,BINANCE:KEYBUSD,BINANCE:1000LUNCBUSDPERP,BINANCE:LUNA2BUSDPERP,BINANCE:ATOMUSDTPERP,BINANCE:FLOWUSDTPERP,BINANCE:FIDABUSD,BINANCE:APEBUSD,BINANCE:RVNUSDTPERP,BINANCE:FTTUSDTPERP
# // --------------- Inputs ---------------
# pump_timeframe = input.timeframe(defval = "", title = "Resolution for Pump")
# pump_bars_cnt = input.int(defval =  16)
# top_k = input.int(defval = 10)
# res = pump_timeframe == '0' ? timeframe.period : pump_timeframe 

# // Table color
# t_loc = input.string(defval="top_right", 
#      options=["top_right",  "middle_right",  "bottom_right", 
#               "top_center", "middle_center", "bottom_center", 
#               "top_left",   "middle_left",   "bottom_left"], title = "table position", tooltip = "table_position", inline = "11", group = 'Table')
# t_size = input.string(defval="Auto", 
#      options=["Auto",  "Huge",  "Large", "Normal", "Small", "Tiny"], 
#      title = "table size", tooltip = "table size", inline = "11", group = 'Table')
# t_header_color = input.color(defval = color.new(#787b86, 10), title = "t_header_color", tooltip = "t_header_color", inline = "12", group = 'Table') 
# t_cell_bg_color1 = input.color(defval = color.new(color.green, 40) , title = "t_cell_bg_color1", tooltip = "t_cell_bg_color1", inline = "13", group = 'Table') 
# t_cell_bg_color2 = input.color(defval = color.new(color.red, 40) , title = "t_cell_bg_color2", tooltip = "t_cell_bg_color2", inline = "13", group = 'Table') 
# t_cell_txt_color = input.color(defval = color.new(color.white, 30) , title = "t_cell_txt_color", tooltip = "t_cell_txt_color", inline = "13", group = 'Table') 

# // Alert Condition
# pump_threhold = input.float(defval = 5.0, title = "pump threhold", tooltip = 'pump threhold', inline = "11", group = 'Alert') 
# pump_position_threhold = input.float(defval = 0.8, title = "pump position threhold", tooltip = 'pump position threhold', inline = "11", group = 'Alert') 
# cell_color = input.color(defval = color.new(color.orange, 40) , title = "alert_cell_color", tooltip = "cell_color", inline = "12", group = 'Alert') 
# // up_up_bars = input.int(defval = 5, title = "up_up_bars", minval =  3, maxval =  10, step =  1, tooltip = "up_up_up bar apart", inline = "13", group = 'Alert') 
# max_arr_size = 100

# show_top1 =  input.bool(defval =  true, inline = "14", group = "Alert") 
# show_pump =  input.bool(defval =  false, inline = "14", group = "Alert") 
# show_history_label =  input.bool(defval =  true, inline = "15", group = "Alert") 

# // symbol_arr = array.from('1000LUNCUSDTPERP','1000SHIBUSDTPERP','AAVEUSDTPERP','ADAUSDTPERP','ALGOUSDTPERP','APEUSDTPERP','APTUSDTPERP','ATOMUSDTPERP','AVAXUSDTPERP','AXSUSDTPERP','BANDUSDTPERP','BCHUSDTPERP','BNBUSDTPERP','BTCUSDTPERP','CELOUSDTPERP','CHZUSDTPERP','COMPUSDTPERP','CRVUSDTPERP','CVXUSDTPERP','DOGEUSDTPERP','DOTUSDTPERP','DYDXUSDTPERP','ENJUSDTPERP','EOSUSDTPERP','ETCUSDTPERP','ETHUSDTPERP','FILUSDTPERP','FLOWUSDTPERP','FTMUSDTPERP','GALAUSDTPERP','GALUSDTPERP','GMTUSDTPERP','GRTUSDTPERP','HNTUSDTPERP','KAVAUSDTPERP','KNCUSDTPERP','LDOUSDTPERP','LINKUSDTPERP','LITUSDTPERP','LRCUSDTPERP','LTCUSDTPERP','LUNA2USDTPERP','MANAUSDTPERP','MASKUSDTPERP','MATICUSDTPERP','NEARUSDTPERP','OCEANUSDTPERP','ONEUSDTPERP','OPUSDTPERP','PEOPLEUSDTPERP','RLCUSDTPERP','SANDUSDTPERP','SOLUSDTPERP','SUSHIUSDTPERP','THETAUSDTPERP','TRXUSDTPERP','UNFIUSDTPERP','UNIUSDTPERP','WAVESUSDTPERP','WOOUSDTPERP','XMRUSDTPERP','XRPUSDTPERP','ZECUSDTPERP','ZILUSDTPERP')

# // --------------- Inputs ---------------

# // --------------- Functions ---------------
# type Symbol
#     string ticker = na
#     float  price_change  = na 
#     float  current_pos = na


# add_to_zigzag(arr, value) =>
#     array.unshift(arr, value)
#     if array.size(arr) > max_arr_size
#         array.pop(arr)

# create_symbol_obj(symbol) => 
#     res_high = request.security(symbol, pump_timeframe, high)
#     highest = ta.highest(res_high, length = pump_bars_cnt) 
#     lowest = ta.lowest(res_high, length = pump_bars_cnt)
#     temp_move = math.round(number = (highest - lowest) / lowest , precision = 3) * 100
#     temp_per = math.round(number = (res_high - lowest) / (highest - lowest) , precision = 1)
#     Symbol.new(ticker= symbol, price_change= temp_move, current_pos= temp_per)

    
# // top1 名次变化   top1_change
# top1_change(current_name_arr, prev_name_arr_str) =>
#     curr_top1 = array.get(current_name_arr,0) 
#     prev_name_arr = str.split(prev_name_arr_str, ',')
#     if array.size(prev_name_arr) > 1
#         prev_top1 = array.get(prev_name_arr,0)
#         top1_change = curr_top1 == prev_top1 ? false: true
#         top1_change
#     else
#         false

# // change 超过threhold  over_threhold
# var overthrehold_arr = array.new_int(0)
# over_threhold(val_arr, val_threhold, pos_arr, pos_threhold) =>
#     array.clear(overthrehold_arr) 
#     for i = 0 to array.size(val_arr) - 1
#         val = array.get(val_arr, i) 
#         pos = array.get(pos_arr, i) 
#         if val > val_threhold and pos > pos_threhold
#             array.push(overthrehold_arr, i) 
#     overthrehold_arr

# // --------------- Functions ---------------


# // --------------- vars ---------------
# symbol_a = array.new  <Symbol> ()

# // 1000LUNCUSDTPERP = create_symbol_obj('BINANCE:1000LUNCUSDTPERP'), array.unshift(symbol_a, 1000LUNCUSDTPERP )
# // 1000SHIBUSDTPERP = create_symbol_obj('BINANCE:1000SHIBUSDTPERP'), array.unshift(symbol_a, 1000SHIBUSDTPERP )
# AAVEUSDTPERP = create_symbol_obj('BINANCE:AAVEUSDTPERP'), array.unshift(symbol_a, AAVEUSDTPERP )
# ADAUSDTPERP = create_symbol_obj('BINANCE:ADAUSDTPERP'), array.unshift(symbol_a, ADAUSDTPERP )
# ALGOUSDTPERP = create_symbol_obj('BINANCE:ALGOUSDTPERP'), array.unshift(symbol_a, ALGOUSDTPERP )
# APEUSDTPERP = create_symbol_obj('BINANCE:APEUSDTPERP'), array.unshift(symbol_a, APEUSDTPERP )
# APTUSDTPERP = create_symbol_obj('BINANCE:APTUSDTPERP'), array.unshift(symbol_a, APTUSDTPERP )
# ATOMUSDTPERP = create_symbol_obj('BINANCE:ATOMUSDTPERP'), array.unshift(symbol_a, ATOMUSDTPERP )
# AVAXUSDTPERP = create_symbol_obj('BINANCE:AVAXUSDTPERP'), array.unshift(symbol_a, AVAXUSDTPERP )
# AXSUSDTPERP = create_symbol_obj('BINANCE:AXSUSDTPERP'), array.unshift(symbol_a, AXSUSDTPERP )
# BANDUSDTPERP = create_symbol_obj('BINANCE:BANDUSDTPERP'), array.unshift(symbol_a, BANDUSDTPERP )
# BCHUSDTPERP = create_symbol_obj('BINANCE:BCHUSDTPERP'), array.unshift(symbol_a, BCHUSDTPERP )
# BNBUSDTPERP = create_symbol_obj('BINANCE:BNBUSDTPERP'), array.unshift(symbol_a, BNBUSDTPERP )
# BTCUSDTPERP = create_symbol_obj('BINANCE:BTCUSDTPERP'), array.unshift(symbol_a, BTCUSDTPERP )
# CELOUSDTPERP = create_symbol_obj('BINANCE:CELOUSDTPERP'), array.unshift(symbol_a, CELOUSDTPERP )
# CHZUSDTPERP = create_symbol_obj('BINANCE:CHZUSDTPERP'), array.unshift(symbol_a, CHZUSDTPERP )
# COMPUSDTPERP = create_symbol_obj('BINANCE:COMPUSDTPERP'), array.unshift(symbol_a, COMPUSDTPERP )
# CRVUSDTPERP = create_symbol_obj('BINANCE:CRVUSDTPERP'), array.unshift(symbol_a, CRVUSDTPERP )
# CVXUSDTPERP = create_symbol_obj('BINANCE:CVXUSDTPERP'), array.unshift(symbol_a, CVXUSDTPERP )
# DOGEUSDTPERP = create_symbol_obj('BINANCE:DOGEUSDTPERP'), array.unshift(symbol_a, DOGEUSDTPERP )
# DOTUSDTPERP = create_symbol_obj('BINANCE:DOTUSDTPERP'), array.unshift(symbol_a, DOTUSDTPERP )
# DYDXUSDTPERP = create_symbol_obj('BINANCE:DYDXUSDTPERP'), array.unshift(symbol_a, DYDXUSDTPERP )
# ENJUSDTPERP = create_symbol_obj('BINANCE:ENJUSDTPERP'), array.unshift(symbol_a, ENJUSDTPERP )
# EOSUSDTPERP = create_symbol_obj('BINANCE:EOSUSDTPERP'), array.unshift(symbol_a, EOSUSDTPERP )
# ETCUSDTPERP = create_symbol_obj('BINANCE:ETCUSDTPERP'), array.unshift(symbol_a, ETCUSDTPERP )
# ETHUSDTPERP = create_symbol_obj('BINANCE:ETHUSDTPERP'), array.unshift(symbol_a, ETHUSDTPERP )
# FILUSDTPERP = create_symbol_obj('BINANCE:FILUSDTPERP'), array.unshift(symbol_a, FILUSDTPERP )
# FLOWUSDTPERP = create_symbol_obj('BINANCE:FLOWUSDTPERP'), array.unshift(symbol_a, FLOWUSDTPERP )
# FTMUSDTPERP = create_symbol_obj('BINANCE:FTMUSDTPERP'), array.unshift(symbol_a, FTMUSDTPERP )
# GALAUSDTPERP = create_symbol_obj('BINANCE:GALAUSDTPERP'), array.unshift(symbol_a, GALAUSDTPERP )
# // GALUSDTPERP = create_symbol_obj('BINANCE:GALUSDTPERP'), array.unshift(symbol_a, GALUSDTPERP )
# // GMTUSDTPERP = create_symbol_obj('BINANCE:GMTUSDTPERP'), array.unshift(symbol_a, GMTUSDTPERP )
# // GRTUSDTPERP = create_symbol_obj('BINANCE:GRTUSDTPERP'), array.unshift(symbol_a, GRTUSDTPERP )
# // HNTUSDTPERP = create_symbol_obj('BINANCE:HNTUSDTPERP'), array.unshift(symbol_a, HNTUSDTPERP )
# // KAVAUSDTPERP = create_symbol_obj('BINANCE:KAVAUSDTPERP'), array.unshift(symbol_a, KAVAUSDTPERP )
# // KNCUSDTPERP = create_symbol_obj('BINANCE:KNCUSDTPERP'), array.unshift(symbol_a, KNCUSDTPERP )
# // LDOUSDTPERP = create_symbol_obj('BINANCE:LDOUSDTPERP'), array.unshift(symbol_a, LDOUSDTPERP )
# // LINKUSDTPERP = create_symbol_obj('BINANCE:LINKUSDTPERP'), array.unshift(symbol_a, LINKUSDTPERP )
# // LITUSDTPERP = create_symbol_obj('BINANCE:LITUSDTPERP'), array.unshift(symbol_a, LITUSDTPERP )
# // LRCUSDTPERP = create_symbol_obj('BINANCE:LRCUSDTPERP'), array.unshift(symbol_a, LRCUSDTPERP )
# // LTCUSDTPERP = create_symbol_obj('BINANCE:LTCUSDTPERP'), array.unshift(symbol_a, LTCUSDTPERP )
# // LUNA2USDTPERP = create_symbol_obj('BINANCE:LUNA2USDTPERP'), array.unshift(symbol_a, LUNA2USDTPERP )
# // MANAUSDTPERP = create_symbol_obj('BINANCE:MANAUSDTPERP'), array.unshift(symbol_a, MANAUSDTPERP )
# // MASKUSDTPERP = create_symbol_obj('BINANCE:MASKUSDTPERP'), array.unshift(symbol_a, MASKUSDTPERP )
# // MATICUSDTPERP = create_symbol_obj('BINANCE:MATICUSDTPERP'), array.unshift(symbol_a, MATICUSDTPERP )
# // NEARUSDTPERP = create_symbol_obj('BINANCE:NEARUSDTPERP'), array.unshift(symbol_a, NEARUSDTPERP )
# // OCEANUSDTPERP = create_symbol_obj('BINANCE:OCEANUSDTPERP'), array.unshift(symbol_a, OCEANUSDTPERP )
# // ONEUSDTPERP = create_symbol_obj('BINANCE:ONEUSDTPERP'), array.unshift(symbol_a, ONEUSDTPERP )
# // OPUSDTPERP = create_symbol_obj('BINANCE:OPUSDTPERP'), array.unshift(symbol_a, OPUSDTPERP )
# // PEOPLEUSDTPERP = create_symbol_obj('BINANCE:PEOPLEUSDTPERP'), array.unshift(symbol_a, PEOPLEUSDTPERP )
# // RLCUSDTPERP = create_symbol_obj('BINANCE:RLCUSDTPERP'), array.unshift(symbol_a, RLCUSDTPERP )
# // SANDUSDTPERP = create_symbol_obj('BINANCE:SANDUSDTPERP'), array.unshift(symbol_a, SANDUSDTPERP )
# // SOLUSDTPERP = create_symbol_obj('BINANCE:SOLUSDTPERP'), array.unshift(symbol_a, SOLUSDTPERP )
# // SUSHIUSDTPERP = create_symbol_obj('BINANCE:SUSHIUSDTPERP'), array.unshift(symbol_a, SUSHIUSDTPERP )
# // THETAUSDTPERP = create_symbol_obj('BINANCE:THETAUSDTPERP'), array.unshift(symbol_a, THETAUSDTPERP )
# // TRXUSDTPERP = create_symbol_obj('BINANCE:TRXUSDTPERP'), array.unshift(symbol_a, TRXUSDTPERP )
# // UNFIUSDTPERP = create_symbol_obj('BINANCE:UNFIUSDTPERP'), array.unshift(symbol_a, UNFIUSDTPERP )
# // UNIUSDTPERP = create_symbol_obj('BINANCE:UNIUSDTPERP'), array.unshift(symbol_a, UNIUSDTPERP )
# // WAVESUSDTPERP = create_symbol_obj('BINANCE:WAVESUSDTPERP'), array.unshift(symbol_a, WAVESUSDTPERP )
# // WOOUSDTPERP = create_symbol_obj('BINANCE:WOOUSDTPERP'), array.unshift(symbol_a, WOOUSDTPERP )
# // XMRUSDTPERP = create_symbol_obj('BINANCE:XMRUSDTPERP'), array.unshift(symbol_a, XMRUSDTPERP )
# // XRPUSDTPERP = create_symbol_obj('BINANCE:XRPUSDTPERP'), array.unshift(symbol_a, XRPUSDTPERP )
# // ZECUSDTPERP = create_symbol_obj('BINANCE:ZECUSDTPERP'), array.unshift(symbol_a, ZECUSDTPERP )
# // ZILUSDTPERP = create_symbol_obj('BINANCE:ZILUSDTPERP'), array.unshift(symbol_a, ZILUSDTPERP )

# float[] pos_arr = array.new_float(size = array.size(symbol_a), initial_value = 0.0) 
# float[] move_arr = array.new_float(size = array.size(symbol_a), initial_value = 0.0) 
# string[] symbol_arr = array.new_string(size = array.size(symbol_a), initial_value = "") 
# string[] topk_pair_name_arr = array.new_string(size = top_k, initial_value = "") 

# string[] prev_topk_pair_name_arr = array.new_string(top_k, "") 
# var string prev_topk_pair_name_str = na
# var string prev_topk_val_arr_str = na
# var string prev_topk_pos_arr_str = na

# // --------------- vars ---------------

# // --------------- Calculate  TopK Symbols---------------
# for i = 0 to array.size(symbol_a) -1
#     pair = array.get(symbol_a, i)
#     pair_ticker = pair.ticker
#     pair_change = pair.price_change
#     pair_pos = pair.current_pos
#     array.set(id = symbol_arr, index = i, value = pair_ticker)
#     array.set(id = move_arr, index = i, value = pair_change)
#     array.set(id = pos_arr, index = i, value = pair_pos)
    
# sorted_indices_arr = array.sort_indices(move_arr, order = order.descending) // [1, 2, 4, 0, 3]
# array.sort(id = move_arr, order =  order.descending) 

# sorted_move_arr = array.copy(move_arr)

# // 将symbol 名称重新排序 与sorted_move_arr的值对应上
# sorted_symbol_arr = array.new_string(size = array.size(symbol_arr), initial_value = "") 
# sorted_pos_arr = array.new_float(size = array.size(symbol_arr), initial_value = 0.0) 
# for i = 0 to array.size(sorted_indices_arr) - 1
#     j = array.get(sorted_indices_arr, i)
#     pair2 = array.get(id = symbol_arr, index = j) 
#     array.set(id = sorted_symbol_arr, index=i, value = pair2)
#     pair3 = array.get(id = pos_arr, index = j) 
#     array.set(id = sorted_pos_arr, index=i, value = pair3)

# topk_name_arr = array.slice(id = sorted_symbol_arr, index_from = 0, index_to = top_k) 
# topk_val_arr = array.slice(id = sorted_move_arr, index_from = 0, index_to = top_k) 
# topk_pos_arr = array.slice(id = sorted_pos_arr, index_from = 0, index_to = top_k)  


# // 干掉 BINANCE: 字符串
# for i = 0 to array.size(id = topk_name_arr) - 1
#     symbol_name = array.get(topk_name_arr, i)
#     s_arr = str.split(symbol_name, ':')
#     pair_name = array.get(s_arr, 1)
#     array.set(id = topk_pair_name_arr, index = i, value = pair_name) 

# // --------------- Calculate  TopK Symbols---------------


# // --------------- Calculate  Alert Condition   ---------------
# // top_change
# top_change_ = top1_change(topk_pair_name_arr, prev_topk_pair_name_str[1])
# // over threhold
# overthrehold_arr_ = over_threhold(topk_val_arr, pump_threhold, topk_pos_arr, pump_position_threhold)
# overthrehold_size = array.size(id = overthrehold_arr_) 
# // add label in chart

# top_change_cond = top_change_ and show_top1
# pump_cond = overthrehold_size >= 1 and show_pump

# var lbl = label.new(bar_index, na, "", color = color.orange, style = label.style_label_up)

# label_text = ''
# tooltip_text = ''
# if  top_change_cond or pump_cond
#     if top_change_cond
#         label_text := label_text + 'T: ' + str.tostring(array.get(topk_pair_name_arr, 0))
#         tooltip_text := tooltip_text + 'top1: '
#         tooltip_text := tooltip_text + str.tostring(array.get(topk_pair_name_arr, 0)) 
#         // tooltip_text := '\n'

#     if pump_cond
#         label_text := label_text + 'P: '
#         tooltip_text := tooltip_text + '\npump: '
#         for i = 0 to overthrehold_size - 1
#             pairname = array.get(topk_pair_name_arr, array.get(overthrehold_arr_, i))  
#             tooltip_text := tooltip_text + str.tostring(pairname) 

#     if show_history_label
#         label.new(bar_index, low, label_text, tooltip = tooltip_text, color = color.orange, style = label.style_label_up)
#     else
#         label.set_xy(lbl, bar_index, low)
#         label.set_text(lbl, label_text)
#         label.set_tooltip(lbl, tooltip_text) 

# // add alert when top_change_cond or pump_cond
# alertcondition(top_change_cond, title='top1_change', message='{{tooltip_text}} || {{timenow}}')
# alertcondition(pump_cond, title='cryptos pump', message='{{tooltip_text}} || {{timenow}}')

# // if overthrehold_size >= 1
# //     labelText = ''
# //     for i = 0 to overthrehold_size - 1
# //         labelText := labelText +  str.tostring(array.get(overthrehold_arr_, i))
# //     // labelText = prev_topk_pair_name_str[1]
# //     // labelText = "High: " + str.tostring(new_up_size, format.mintick)
# //     tooltipText = "Offest in bars: " + str.tostring(111) + "\nLow: " + str.tostring(low[10], format.mintick)
# //     // Update the label's position, text and tooltip.
# //     label.new(bar_index, high, labelText, tooltip = tooltipText, color = color.orange, style = label.style_label_down)
# //     // label.set_text(lbl, labelText)
# //     // label.set_tooltip(lbl, tooltipText)   

# // --------------- Calculate  Alert Condition    ---------------

# // --------------- Save history array value      ---------------
# prev_topk_pair_name_str := array.join(topk_pair_name_arr, separator = ",")
# prev_topk_val_arr_str := array.join(topk_val_arr, separator = ",")
# prev_topk_pos_arr_str := array.join(topk_pos_arr, separator = ",")


# // --------------- Calculate  Alert Condition    ---------------


# // --------------- plot table cells---------------
# // 画table.cell()

# table_position = t_loc== "top_right"    ? position.top_right: 
#            t_loc== "middle_right" ? position.middle_right:  
#            t_loc== "bottom_right" ? position.bottom_right: 
#            t_loc== "top_center"   ? position.top_center: 
#            t_loc== "middle_center"? position.middle_center:
#            t_loc== "bottom_center"? position.bottom_center:
#            t_loc== "top_left"     ? position.top_left: 
#            t_loc== "middle_left"  ? position.middle_left:position.bottom_left

# table_size = t_size == "Auto" ? size.auto:  t_size == "Huge"  ? size.huge: t_size == "Large"? size.large: t_size == "Normal"? size.normal: t_size == "Small"? size.small: size.tiny



# table_rows = array.size(id= topk_pair_name_arr)
# var tabl = table.new (table_position, columns= 4, rows= table_rows)

# table.cell(tabl, 0, 0, "Rank", bgcolor = t_header_color, text_size = table_size)
# table.cell(tabl, 1, 0, "Symbol", bgcolor = t_header_color, text_size = table_size)
# table.cell(tabl, 2, 0, "Value", bgcolor = t_header_color, text_size = table_size)
# table.cell(tabl, 3, 0, "Position", bgcolor = t_header_color, text_size = table_size)

# if barstate.isconfirmed    
#     table.clear(tabl, 0,0,3,table_rows - 1)

#     for i = 0 to table_rows - 2
#         mod = i % 2  ==  0 
#         bg_color  = mod ?  t_cell_bg_color1 : t_cell_bg_color2
#         txt_color  = mod ?  t_cell_txt_color : t_cell_txt_color
#         row_1_txt = array.get(id = topk_pair_name_arr, index =i) 
#         row_2_txt = array.get(id = topk_val_arr, index =i) 
#         row_3_txt = array.get(id = topk_pos_arr, index =i) 
#         table.cell(table_id= tabl, column= 0, row= i+1, text= str.tostring(i+1), text_font_family=font.family_monospace, text_color= txt_color, bgcolor= bg_color, text_size = table_size)
#         table.cell(table_id= tabl, column= 1, row= i+1, text= row_1_txt, text_font_family=font.family_monospace, text_color= txt_color, bgcolor= bg_color, text_size = table_size)
#         table.cell(table_id= tabl, column= 2, row= i+1, text= str.tostring(row_2_txt), text_font_family=font.family_monospace, text_color= txt_color, bgcolor= bg_color, text_size = table_size)
#         table.cell(table_id= tabl, column= 3, row= i+1, text= str.tostring(row_3_txt), text_font_family=font.family_monospace, text_color= txt_color, bgcolor= bg_color, text_size = table_size)