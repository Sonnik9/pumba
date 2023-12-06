# Just a simple script that tweaks the original Volume one.
# The purpose is creating a threshold which we'll use to put an alert on. This way, we can be notified whether Volume pumps.
# Useful for spotting breakouts, breakdowns and pumps.

# Threshold is simply a coeff * ma(volume,period). Coeff is editable as well.

# Hope this helps!


# //@version=3
# study(title="Volume", shorttitle="Vol", precision=0)
# showMA = input(true)
# barColorsOnPrevClose = input(title="Color bars based on previous close", type=bool, defval=false)

# palette = barColorsOnPrevClose ? close[1] > close ? red : green : open > close ? red : green

# ThreshCoeff = input(type=float,defval=2)

# MAperiod=input(20)

# thresh = ThreshCoeff*sma(volume,MAperiod)

# plot(volume, color = palette, style=columns, title="Volume", transp=65)
# plot(showMA ? sma(volume,MAperiod) : na, style=area, color=blue, title="Volume MA", transp=65)
# plot(thresh,title="Threshold")