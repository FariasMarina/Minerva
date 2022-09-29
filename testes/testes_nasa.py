from NASApi import APOD
from PIL import Image

apod = APOD("2020-08-18") # Instantiates the class
pic = Image.open(apod.bytes_image) # Opens the bytes image using PIL
pic.show() # Opens the current image for viewing pleasures

apod = APOD("2020-08-19") # Instantiates the class
pic = Image.open(apod.bytes_thumbnail) # Opens the bytes image using PIL
pic.show() # Opens the current image for viewing pleasures