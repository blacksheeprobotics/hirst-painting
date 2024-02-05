###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb_colors.append((red, green, blue))

print(rgb_colors)
