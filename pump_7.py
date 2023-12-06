# This indicator displays volume as a pump wave. Can be useful for chart analysis and easy detection of anomalies/trends.





# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © veryfid

# //@version=4
# study("Volume Pump Wave",overlay = false, resolution = "")

# //INPUTS
# devH = input(3, title="Upper Line", maxval=5, minval=0.1,inline = "line")
# devL = input(3, title="Lower Line", maxval=5, minval=0.1,inline = "line")
# stdevper = input(100, title="Stdev Period", maxval=200, minval=1,inline = "line2")
# showalerts = input(false,title = "Show Alerts?")

# l1 =stdev(volume, stdevper)
# a = avg(volume,l1)
# k = a / l1
# k2 = k * -1
# col = close < open ? color.red : color.blue
# a1 = plot(k, color = col)
# a2 = plot(k2, color = col)


# //UPPER AND LOWER LINES
# l =plot(devH * stdev(k, stdevper), color=color.gray, title = "Upper Line")
# l2 =plot(-devL * stdev(k, stdevper), color=color.gray, title = "Lower Line")

# //CONDITIONS
# xo = crossover(k,devH * stdev(k, stdevper))
# pump = xo and close > open
# dump = xo and close < open

# //PLOTS
# plotshape(showalerts ? dump : na, title="Dump", location=location.top, style=shape.circle, size=size.tiny, color=color.red, transp=20)
# plotshape(showalerts ? pump : na, title="Pump", location=location.top, style=shape.circle, size=size.tiny, color=color.blue, transp=20)
# fill(a1,a2, color = col, transp = 50)

# //ALERTS
# alertcondition(dump, title='Dump', message='Volume Dump')
# alertcondition(pump, title='Pump', message='Volume Pump')