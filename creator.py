from PIL import Image, ImageDraw, ImageFont

# 需求：生成不同size的图片


# 此方法生成的图片由于是单色，size不会很大，并且利用两次for循环来设置每个像素的颜色，很耗时，不可取
def create_img():
    img = Image.new("RGB", (3000, 3000))
    pix = (255, 0, 255, 50)
    for i in range(3000):
        for j in range(3000):
            img.putpixel((i, j), pix)
    img.save("baa.png")

def draw_image(new_img, text, show_image=False):
    text = str(text)
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
    draw.line((0, 0) + img_size, fill=128)
    draw.line((0, img_size[1], img_size[0], 0), fill=128)

    font_size = 40
    fnt = ImageFont.truetype('arial.ttf', font_size)
    fnt_size = fnt.getsize(text)
    while fnt_size[0] > img_size[0] or fnt_size[0] > img_size[0]:
        font_size -= 5
        fnt = ImageFont.truetype('arial.ttf', font_size)
        fnt_size = fnt.getsize(text)

    x = (img_size[0] - fnt_size[0]) / 2
    y = (img_size[1] - fnt_size[1]) / 2
    draw.text((x, y), text, font=fnt, fill=(255, 0, 0))

    if show_image:
        new_img.show()
    del draw


# 生成图片
def new_image(width, height, text='default', color=(100, 100, 100, 255), show_image=False):
    new_img = Image.new('RGBA', (int(width), int(height)), color)
    draw_image(new_img, text, show_image)
    new_img.save('%s_%s.png' % (width, height))
    del new_img


def new_image_with_file(fn):
    with open(fn, encoding='utf-8') as f:
        for l in f:
            l = l.strip()
            if l:
                ls = l.split(',')
                if '#' == l[0] or len(ls) < 2:
                    continue

                new_image(*ls)


if __name__ == '__main__':
    create_img()
