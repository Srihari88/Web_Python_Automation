import re
import linkGrabber

links = linkGrabber.Links("https://www.pitchvision.com/#/")
gb = links.find(pretty=True)

print(gb)

