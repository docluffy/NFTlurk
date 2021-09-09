#Evan Russenberger-Rosica
#Create a Grid/Matrix of Images
import PIL, os, glob
from PIL import Image
from math import ceil, floor
dirname = os.path.dirname(os.path.abspath(__file__))
PATH = dirname + '/midpunks_images/'



frame_width = 12000
images_per_row = 1000
padding = 0

os.chdir(PATH)

images = sorted(glob.glob("*.png"), key=lambda x: float(x[:-4]))
print(images)
images = images[0:10000]                #get the first 30 images

print(images)

img_width, img_height = Image.open(images[0]).size
sf = (frame_width-(images_per_row-1)*padding)/(images_per_row*img_width)       #scaling factor
scaled_img_width = ceil(img_width*sf)                   #s
scaled_img_height = ceil(img_height*sf)

number_of_rows = ceil(len(images)/images_per_row)
frame_height = ceil(sf*img_height*number_of_rows) 

new_im = Image.new('RGB', (frame_width, frame_height))

i,j=0,0
for num, im in enumerate(images):
    if num%images_per_row==0:
        i=0
    im = Image.open(im)
    #Here I resize my opened image, so it is no bigger than 100,100
    im.thumbnail((scaled_img_width,scaled_img_height))
    #Iterate through a 4 by 4 grid with 100 spacing, to place my image
    y_cord = (j//images_per_row)*scaled_img_height
    new_im.paste(im, (i,y_cord))
    print(i, y_cord)
    i=(i+scaled_img_width)+padding
    j+=1

new_im.show()
new_im.save("out.jpg", "JPEG", quality=100, optimize=True, progressive=True)


# from PIL import Image, ImageOps

# # Open image
# im = Image.open('start.png')

# # Add border and save
# bordered = ImageOps.expand(im, border=(10,40,80,120), fill=(0,0,0))

# bordered.save('result.png')
