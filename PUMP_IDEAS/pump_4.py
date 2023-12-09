# This script displays the percentage of movement of all candles on the chart, as well as identifying abnormal movements to which you can attach alerts. An abnormal movement is considered a rise or fall that exceeds the parameter set in the settings (by default, 1% per 1 bar).
# Added a function to display the volume on abnormal candlesticks.
# Авг 18
# Информация о релизе:
# This script displays the percentage of movement of all candles on the chart, as well as identifying abnormal movements to which you can attach alerts. An abnormal movement is considered a rise or fall that exceeds the parameter set in the settings (by default, 1% per 1 bar).
# Added a function to display the volume on abnormal candlesticks.




# //@version=5
# indicator("Scalp Pump-Dump Detector with Alerts", "", true, max_labels_count=500)

# var int precision = input.int(2, "Rounding", minval = 0, maxval = 5)
# float fromSource = input.source(low, "From")
# float toSource = input.source(high, "To")

# var format = "#"
# if barstate.isfirst
#     if precision != 0
#         format += "."
#         for i = 0 to precision - 1
#             format += "#"

# diff = (toSource / fromSource - 1) * 100

# diff_color = close < open ? color.red : color.green

# anomalyThreshold = input.float(1, "Anomaly Threshold (%)", step = 0.1, minval = 0)

# isAnomaly = math.abs(diff) > anomalyThreshold

# bgcolor(isAnomaly ? color.new(close < open ? color.red : color.green, 70) : na)

# label.new(bar_index, high, str.tostring(diff, format), style = label.style_none, size = size.tiny, textcolor = diff_color)


# alertcondition(isAnomaly and close < open, "Anomaly Down", "Anomaly Down Detected!")
# alertcondition(isAnomaly and close > open, "Anomaly Up", "Anomaly Up Detected!")
# alertcondition(isAnomaly, "Anomaly", "Anomaly Detected!")

# var bool showVolume = input.bool(true, "Show Volume", inline = "Volume")

# var float anomalyVolume = na
# if isAnomaly
#     anomalyVolume := volume

# if showVolume and isAnomaly
#     volumeLabel =  anomalyVolume >= 1000000000 ? str.tostring(anomalyVolume / 1000000000, "#.#") + "B" : anomalyVolume >= 1000000 ? str.tostring(anomalyVolume / 1000000, "#.#") + "M" : anomalyVolume >= 1000 ? str.tostring(anomalyVolume / 1000, "#.#") + "K" : str.tostring(anomalyVolume)
#     label.new(bar_index, high, "Vol - " + volumeLabel, color = color.rgb(95, 59, 255, 100), textcolor = color.rgb(255, 255, 255), style = label.style_circle, size = size.small)


# import PineCoders/getSeries/1 as gs
# price = close    
# sumVolTF = switch
#     timeframe.isminutes or timeframe.isseconds => "1"
#     timeframe.isdaily => "5"
#     => "60"

# sum24hVol(src) =>
#     msIn24h = 24 * 60 * 60 * 1000
#     sourceValues = gs.rollOnTimeWhen(src, msIn24h)
#     sourceValues.sum()
        

# var float vol24h = na
# expr = syminfo.volumetype == "quote" ? volume : close * volume
# vol24h := request.security(syminfo.tickerid, sumVolTF, sum24hVol(expr))


# vol24h := na(vol24h) ? 0 : vol24h

# formattedVolToShow = vol24h >= 1000000000 ? str.tostring(vol24h / 1000000000, "#,###.###") + "B" : vol24h >= 1000000 ? str.tostring(vol24h / 1000000, "#,###.###") + "M" : str.tostring(vol24h / 1000, "#,###.###") + "K"

# t_info = table.new(position.bottom_right, 1, 1, bgcolor=color.new(#706f6f, 0))
# isTableVisible = input(true, title="Show Table")

# if isTableVisible
#     table.cell(t_info, 0, 0, formattedVolToShow + " USD")





