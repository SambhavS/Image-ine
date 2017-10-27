#Run with python 2, not 3
from PIL import Image, ImageDraw
pic = raw_input("Please enter file name: ")
im = Image.open(pic)
square_ratio = 30
filter_colors = []
square_width = im.width/square_ratio
square_pixels = square_width ** 2
def filtered_image(im, fil_col):
	rectangle = Image.new('RGB', (im.width, im.height), fil_col)
	return Image.blend(im,rectangle, 0.7)
for i in range(square_ratio):
	row1 = []
	for j in range(square_ratio):
		col_sum = [0,0,0]
		for x in range(int(square_width)):
			for y in range(int(square_width)):
				pix = im.getpixel((int(square_width*i)+x,int(square_width*j)+y))
				col_sum[0], col_sum[1], col_sum[2] = col_sum[0]+pix[0], col_sum[1]+pix[1], col_sum[2]+pix[2]
		row1.append((col_sum[0]/square_pixels,col_sum[1]/square_pixels,col_sum[2]/square_pixels))
	filter_colors.append(tuple(row1))
new_image = Image.new('RGB',(im.height,im.width))
mini_pic = im.copy().resize((int(square_width),int(square_width)))
x_offset = 0
for a in range(square_ratio):
	y_offset = 0
	for b in range(square_ratio):
		new_image.paste(filtered_image(mini_pic,filter_colors[a][b]), (x_offset,y_offset))
		y_offset+=int(square_width)
	x_offset+=int(square_width)
new_image.save("new_"+pic+".png")
