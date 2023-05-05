

import pyqrcode
import png
from pyqrcode import QRCode

str="ParvezHossen"
url=pyqrcode.create(str) #Generate QR Code
url.svg("myqr.svg",scale=8) # create svg file
url.png('myqr.png',scale=6) # create png file



