from PIL import Image  # 导入PIL库
import numpy as np     # 导入numpy

a = (np.array(Image.open(r"D:\\图片\\Snipaste\Snipaste_20231201-151953.png").convert('L')).astype('float'))

depth = 10.            # 范围时0~100 可以用来控制图片颜色深度
grad = np.gradient(a)
grad_x, grad_y = grad
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2
vec_az = np.pi/4.
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))
im.save("D:\\图片\\123_1.jpg")
