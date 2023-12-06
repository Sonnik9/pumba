# The anomalous volume indicator, could help in detecting pumps and dumps. Open Source.

# //@version=4
# study(title="Pump-Dump Volume")
# volChange = close[0] - close[1]
# color1 =  color.new(#ffeb3b, 50)
# green = color.new(#388e3c, 0)
# red = color.new(#ef5350, 0)
# i = input(title="MA Length", type=input.integer, defval=21, minval=1)
# p1= plot(sma(volume, i), color = color1, title = "Volume Moving Avarage")
# p2= plot(series=volume, style=plot.style_columns,
#      color=volChange > 0 ? green : red, title = "Volume")
# fill(p1, plot(0), color=color1, title = "Background")
