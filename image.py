def imagecreate():
    image = open("theimage.ppm", "w")
    image.write("P3\n")
    image.write("500 500\n")
    image.write("255\n\n")
    for i in range(500):
        curline = ""
        for j in range(500):
            if i > 250:
                i = 250 - (i % 250)
            if j > 250:
                j = 250 - (j % 250)
            if i == 0 or j == 0:
                r = 0
                g = 0
            else:
                r = 255 % (i + j)
                g = 255 % (i + j)
            b = (i + j) % 255
            curline += "%d %d %d "%(r,g,b)
        image.write(curline+"\n")
    image.close()

imagecreate()
