from PIL import Image, ImageDraw, ImageFont

def add_number(img, number):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fill_color = "#ff0000"
    width, _ = img.size
    draw.text((width-40, 0), number, font=myfont, fill=fill_color)
    img.save('result.jpg', 'jpeg')


if __name__ =='__main__':
    img_name = Image.open('test.jpg')
    add_number(img_name, '5')