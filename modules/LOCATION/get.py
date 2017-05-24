import os
import sys

xloc = 40.741895
yloc = 10.5
zloc = -73.989308

if len(sys.argv) > 1:
    location_parsed = sys.argv[1].lower().replace("x", str(xloc))
    location_parsed = location_parsed.replace("y", str(yloc))
    location_parsed = location_parsed.replace("z", str(zloc))

else:
    location_parsed = str(xloc) + ";" + str(yloc) + ";" + str(zloc)

sys.stdout.write(location_parsed)