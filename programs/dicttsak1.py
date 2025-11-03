
colors = [
      {
      "colors": "red",
      "values": "#f00"
      },
      {
      "colors": "green",
      "values": "#0f0"
      },
      {
      "colors": "blue",
      "values": "#00f"
      },
      {
      "colors": "cyan",
      "values": "#0ff"
      },
      {
      "colors": "magenta",
      "values": "#f0f"
      },
      {
      "colors": "yellow",
      "values": "#ff0"
      },
      {
      "colors": "black",
      "values": "#000"
      }
      ]

print(type(colors))
print(isinstance(colors,list))
print(isinstance(colors,dict))


for color in colors:
    print(color['colors'], color['values'])