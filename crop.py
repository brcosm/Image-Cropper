#! /usr/bin/python
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Create a cropped version of the input image file')
parser.add_argument('image', metavar='img', type=str, help='the path to the original image file')
parser.add_argument('x',metavar='x-coord', type=int, help='the x coordinate of the top left corner') 
parser.add_argument('y',metavar='y-coord', type=int, help='the y coordinate of the top left corner') 
parser.add_argument('width',metavar='width', type=int, help='the width of the cropped image') 
parser.add_argument('height',metavar='height', type=int, help='the width of the cropped image') 
args = parser.parse_args()

# Create an image using the input file argument
image = Image.open(args.image)

# Setup cropping region
origin = (args.x, args.y)
size = (min(args.width, image.size[0]), min(args.height, image.size[1]))
region = origin + (origin[0]+size[0], origin[1]+size[1])

# Crop region from original image and paste into new iamge
cropped_region = image.crop(region)
cropped_image = Image.new("RGBA", size)
cropped_image.paste(cropped_region, (0, 0))
image_name = args.image.split(".")[0]+"_cropped.png"
cropped_image.save(image_name, "PNG")
