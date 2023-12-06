# Here is a script to know when big dumps, and pumps, are happening.
# Meant for crypto (I know that's what most people are interested in - it's a mistake) and small caps.
# Might work for other things have not checked.



# //@version=1
# study(title="Mr Renev Dump alert", shorttitle="Mr Renev Dump alert", overlay=false)
# // To be used with small cap stocks and crypto if it is still around.

# drop = input(15, "Percentage drop", type = float)

# drop_pct = drop / 100

# dump = low < high * (1-drop_pct)

# plot(dump, color=blue, linewidth=2, title="Signal")