#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pylab as lab
from PIL import Image

def run(args):
	i = args.input
	o = args.output
	p = args.pixel
	r = args.ratio
	m = args.map

	img = mpimg.imread(i)

	#choose RGB
	lum_img = img[:, :, 0]			

	#set color map
	plt.imshow(lum_img, cmap=m) 	

	#remove axis
	plt.axis("off")	

	#plot colorbar
	cb = plt.colorbar()				
	cb.outline.set_visible(False)
	cb.set_ticks([])

	#from matplotlib > PIL
	img = lab.savefig(o)			
	img = Image.open(o)				

	# stretching the image
	img = img.resize((img.size[0],img.size[1]*r), Image.NEAREST)

	# pixelating the image
	img = img.resize((img.size[0]/p, img.size[1]/p), Image.NEAREST)
	img = img.resize((img.size[0]*p, img.size[1]*p), Image.NEAREST)

	# skewing the image
	img = img.resize((img.size[0], img.size[1]/r), Image.NEAREST)

 	img.save(o)

def main():
	parser=argparse.ArgumentParser(description="Transform any PNG file into a heatmap! N.B. works best with grayscaled & low contrast images" )
	parser.add_argument("-i",help="input file", dest="input", type=str, required="True")
	parser.add_argument("-o", help="output file", dest="output", type=str, required="True")
	parser.add_argument("-p", help="pixelation, default = 10", dest="pixel", type=int, default=10)
	parser.add_argument("-m", help="color map, default='bwr' see matplotlib manual for other color maps", dest="map", type=str, default="bwr")
	parser.add_argument("-r", help="pixel ratio, default = 3", dest="ratio", type=int, default=3)
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()