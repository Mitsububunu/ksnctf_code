from PIL import Image
import os
import os.path


def main():
    moji_set = "0123456789ABCDEF"

    through_moji = []

    for i in moji_set:
        path = "./data/"+str(i)
        if len(os.listdir(path)) >= 100:
            through_moji.append(str(i))

    name = str(input("file name:"))
    image = Image.open("./image/image/"+name)
    rgb_image = image.convert("RGB")
    size = rgb_image.size
    space = int(size[0]/32)
    size0 = (int(size[0]/32), size[1])
    image2 = Image.new("RGBA", size0)
    init_color = rgb_image.getpixel((0, 0))
    count = 1
    moji = str(input("moji:"))
    counter = input("number:")

    for x in range(size[0]):
        if x >= count*space:
            if (moji[count-1] in through_moji) is False:
                image2.save("./data/"+moji[count-1] +
                            "/"+str(count+(32*int(counter)))+".jpg")
            else:
                pass
            image2 = Image.new("RGBA", size0)
            count = count+1
        for y in range(size[1]):
            if rgb_image.getpixel((x, y)) != init_color:
                image2.putpixel((x-((count-1)*space), y), (0, 0, 0, 0))
            else:
                image2.putpixel((x-((count-1)*space), y), (255, 255, 255, 0))

    for i in moji_set:
        path = "./data/"+str(i)
        print(i+":"+str(len(os.listdir(path))))


if __name__ == "__main__":
    main()
