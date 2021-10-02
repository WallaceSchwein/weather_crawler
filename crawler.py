import wetter

class Color():
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    PRESENTER =  '\u001b[38;5;155m'

    GREY = '\u001b[38;5;250m'
    COLOR1 = '\u001b[38;5;120m'
    COLOR2 = '\u001b[38;5;121m'
    COLOR3 = '\u001b[38;5;122m'
    COLOR4 = '\u001b[38;5;123m'

    END = '\033[0m'

crawl = wetter.DataCrawler()
color = Color()

print(color.UNDERLINE + "\nDas Wetter der nächsten 14 Tage, wird Ihnen präsentiert von:" + color.END 
      + color.PRESENTER + "\tWallace Schwein Inc. ®\n\n" + color.END)

for elem in crawl.crawl():
    print(color.GREY + "◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦" + color.END)
    print("Am " 
          + color.COLOR1 + str(elem.tag) + color.END 
          + " wird es zwischen:\t" + color.COLOR2 + str(elem.max) + color.END 
          + " tags und " + color.COLOR3 + str(elem.min) + color.END 
          + " \tnachts. Himmel: \t" + color.COLOR4 + elem.regen + color.END)

print("\n")
