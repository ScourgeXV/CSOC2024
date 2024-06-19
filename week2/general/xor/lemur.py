#!/usr/bin/env python3

from PIL import Image, ImageChops

lemur = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
flag = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')

result = ImageChops.add(ImageChops.subtract(flag,lemur), ImageChops.subtract(lemur,flag))
result.show()
result.save("flag.png")
