# This indicator reads the charts as frequency because the charts are just waves after all. This is an excellent tool for finding "Booms" and detecting dumps. Booms are found when all the frequencies pull under the red 20 line. Dumps are detected when all the lines drag themselves along the 20 line as seen is screenshots below.
# snapshot
# Below is another 2 examples of a "boom". Everything sucks in before exploding out.
# snapshot
# Below is an example of a dump:
# snapshot
# Июл 9, 2021
# Информация о релизе:
# Added signals for pos and neg crossover. Added bg coloring. Added alerts for pos/neg crossover and "boom" for when all lines are under 20. Added mirror option.
# Ноя 6, 2021
# Информация о релизе:
# A big shout out to @KryptoBeau for the latest update and improvements. Here are the changes:
# 144 plot(len1 * 3 ,"3xlen1", color=#bbd9fb)//original line
# 155 cond1 = rcm < 20 and len < 20 and average < 20 and len1 < 20//original line - had problems because of the len1*3 issue
# 160 cond3 = crossunder(average,20)//KB edit from "crossover"
# 166 bgcolor(cond2 and bgcolor ? color.new(color.white, transp=inputBackgroundTransparency) : na, title="cond2 Background")//KB changed from cond1.
# 169 plotshape(signals ? cond3 : na, title="Neg Crossover", location=location.top, style=shape.circle, size=size.tiny, color=color.new(color.red, transp=20))//KB Edit to Neg Cross over not Pos Crossover
# Янв 3, 2022
# Информация о релизе:
# Tesla coil is now easier to read. Use this indicator to pin point the best trades and exact moment of explosion. Enter trade on a crossover and you skip the sideways wait before a breakout. Look for crosses on each set of lines. Lines light up as it pulls in for an explosion. Big things also happen when the purple and light blue lines cross. Use with a fast oscillator like boom hunter pro and it is hard to make a bad trade. Enjoy
# snapshot
# snapshot
# snapshot
# Янв 4, 2022
# Информация о релизе:
# Minor fix to alerts. Alerts trigger when the white lines cross, when the purple lines cross and when the blue lines cross.

# There are 3 lines displayed. All are based on formulas by John Ehlers. These lines measure the cycles of charts, using them together we can enter trades at the beginning/end of cycles. These are moments of extreme volatility.
# snapshot

# Cosine IFM - An instantaneous frequency measurement of dominant cycle periods.

# In-phase and quadrature IFM - An instantaneous frequency measurement of dominant cycle periods using in-phase and quadrature analysis.

# Average - Average of the 2 above lines as well as RCM. These are strong cycle measurements as it uses 3 sets of data to find the mean.

# The white and purple lines will help find explosive volatility.


# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © veryfid
# // contribution by @KryptoBeau 

# //@version=5

# indicator(title='Tesla Coil', overlay=false, timeframe='')
# src = input(title='Source', defval=close)
# mirror = true

# //////////
# //The Cosine IFM
# //Copyright DasanC 2019
# range_1 = input(title='Scanning Range', defval=100)
# len2 = input(40)
# PI = 3.14159265359
# s2 = 0.0
# s3 = 0.0
# delta1 = 0.0
# inst1 = 0.0
# len1 = 0.0
# v1 = 0.0
# v2 = 0.0
# v4 = 0.0

# v1 := src - src[7]
# s2 := 0.2 * (v1[1] + v1) * (v1[1] + v1) + 0.8 * nz(s2[1])
# s3 := 0.2 * (v1[1] - v1) * (v1[1] - v1) + 0.8 * nz(s3[1])
# if s2 != 0
#     v2 := math.sqrt(s3 / s2)
#     v2
# if s3 != 0
#     delta1 := 2 * math.atan(v2)
#     delta1
# for i = 0 to range_1 by 1
#     v4 += delta1[i]
#     if v4 > 2 * PI and inst1 == 0.0
#         inst1 := i - 1
#         inst1
# if inst1 == 0.0
#     inst1 := inst1[1]
#     inst1
# len1 := 0.25 * inst1 + 0.75 * nz(len1[1])



# //Robust Cycle Measurement Function (I-Q Principles)
# //Args: src is the series you want to find the period of
# // I cant remember where I got this code from...
# //##############################################################################
# getRCM(src) =>
#     Price = src
#     alpha = 0.1
#     //Optional Parameters if the user wishes to change
#     //alpha := input(title="Alpha", type=float, defval=0.07)
#     Cycle = 0.0
#     Q1 = 0.0
#     I1 = 0.0
#     I2 = 0.0
#     Q2 = 0.0
#     DeltaPhase = 0.0
#     MedianDelta = 0.0
#     DC = 0.0
#     InstPeriod = 0.0
#     Period = 0.0


#     Smooth = (Price + 2 * Price[1] + 2 * Price[2] + Price[3]) / 6
#     Cycle := (1 - 0.5 * alpha) * (1 - 0.5 * alpha) * (Smooth - 2 * Smooth[1] + Smooth[2]) + 2 * (1 - alpha) * nz(Cycle[1]) - (1 - alpha) * (1 - alpha) * nz(Cycle[2])
#     if bar_index < 7
#         Cycle := (Price - 2 * Price[1] + Price[2]) / 4
#         Cycle
#     Q1 := (0.0962 * Cycle + 0.5769 * Cycle[2] - 0.5769 * Cycle[4] - 0.0962 * Cycle[6]) * (0.5 + 0.08 * InstPeriod[1])
#     I1 := Cycle[3]
#     if Q1 != 0 and Q1[1] != 0
#         DeltaPhase := (I1 / Q1 - I1[1] / Q1[1]) / (1 + I1 * I1[1] / (Q1 * Q1[1]))
#         DeltaPhase
#     if DeltaPhase < 0.1
#         DeltaPhase := 0.1
#         DeltaPhase
#     if DeltaPhase > 1.1
#         DeltaPhase := 1.1
#         DeltaPhase
#     MedianDelta := ta.percentile_nearest_rank(DeltaPhase, 5, 50)
#     if MedianDelta == 0
#         DC := 15
#         DC
#     else
#         DC := 6.28318 / MedianDelta + 0.5
#         DC
#     InstPeriod := 0.33 * DC + 0.67 * nz(InstPeriod[1])
#     Period := 0.15 * InstPeriod + 0.85 * nz(Period[1])
#     Period := math.round(Period)
#     Period
# //##############################################################################

# rcm = getRCM(src)


# //#############################################################################
# //The In-phase & quadrature IFM
# //Copyright DasanC 2019
# //#############################################################################

# imult = 0.635
# qmult = 0.338
# inphase = 0.0
# quadrature = 0.0
# re = 0.0
# im = 0.0
# delta = 0.0
# inst = 0.0
# len = 0.0
# V = 0.0

# P = src - src[7]

# inphase := 1.25 * (P[4] - imult * P[2]) + imult * nz(inphase[3])
# quadrature := P[2] - qmult * P + qmult * nz(quadrature[2])
# re := 0.2 * (inphase * inphase[1] + quadrature * quadrature[1]) + 0.8 * nz(re[1])
# im := 0.2 * (inphase * quadrature[1] - inphase[1] * quadrature) + 0.8 * nz(im[1])
# if re != 0.0
#     delta := math.atan(im / re)
#     delta

# for i = 0 to 100 by 1
#     V += delta[i]
#     if V > 2 * PI and inst == 0.0
#         inst := i
#         inst

# if inst == 0.0
#     inst := nz(inst[1])
#     inst

# len := 0.25 * inst + 0.75 * nz(len[1])

# average = math.avg(len1 * 3, rcm, len)
# tfig = input(50)
# tfig2 = len1 * 3 > len1 * 3 * -1 + len2 ? 50 : 0
# tfig3 = average > average * -1 + len2 ? 50 : 0
# tfig4 = len <= len * -1 + len2 ? 90 : 50
# cola= input.color(color.blue)
# colb= input.color(#bbd9fb)
# colc= input.color(#9575cd)
# plot(len, 'len', color=color.new(cola, tfig4))
# //plot(len1 * 3 ,"3xlen1", color=#bbd9fb)//original line
# len1x3 = len1 * 3  //KB edit
# plot(len1x3, '3xlen1', color=color.new(colb, tfig2))  //KB edit

# //Mirror
# plot(mirror ? len * -1 + len2 : na, 'len mirror', color=color.new(cola, tfig4))
# plot(mirror ? len1 * 3 * -1 + len2 : na, 'len1 mirror', color=color.new(colb, tfig2))
# plot(mirror ? average * -1 + len2 : na, 'average mirror', color=color.new(colc, tfig3))
# plot(average, 'average', color=color.new(colc, tfig3))

# alertcond = ta.cross(len1 * 3, 20) or ta.cross(average, average * -1 + len2) or ta.cross(len, len * -1 + len2 )
# alertcondition(alertcond, title='Tesla Coil', message='Tesla Coil Crossover')
