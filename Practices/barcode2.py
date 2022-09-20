from pystrich.code128 import Code128Encoder
import matplotlib.pyplot as plt
import barcode
from barcode.writer import ImageWriter


def barcode_with_stch(num):
    if num.isdigit():  # 判断是否为数字
        encoder = Code128Encoder(num)
        encoder.save("./files/code39.png", bar_width=1)
        return "文件已保存{}".format("./files/code39.png")
    else:
        return "请提供数字！！！"


def barcode_with_pybarcode(num):
    bar = barcode.get(u'code128', num, writer=ImageWriter())
    output = bar.render(writer_options={"format": "PNG"})
    # 渲染生成图像对象
    print(type(output))
    plt.imshow(output)
    plt.axis('off')
    plt.show()
    bar.save("./files/11.jpg", options={"format": "JPEG"})
    # 保存图形里有渲染然后保存到文件


if __name__ == '__main__':
    code = '05520220914000016'
    barcode_with_pybarcode(code)
