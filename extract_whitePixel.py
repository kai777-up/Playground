from PIL import Image

def jpg_to_png(input_jpg_path, output_png_path):
    img = Image.open(input_jpg_path)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []
    for item in datas:
        # change all white (also shades of whites) pixels to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_png_path, "PNG")

# 使用函数
jpg_to_png("/Users/likai/Desktop/IMG_5931.jpg", "output.png")
