from goprohero import GoProHero
import sys

camera = GoProHero(password='')
sys.stdout.write(camera.status())