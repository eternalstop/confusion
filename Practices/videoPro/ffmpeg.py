import os
import asyncio
import ffmpy3


async def test(name):
    infile = r"D:\图片\音乐典藏馆" + "\\" + name
    outfile = infile.split(".")[0] + "." + "m4a"
    # print(outfile)
    ff = ffmpy3.FFmpeg(inputs={infile: None}, outputs={outfile: "-vn -codec copy"})
    return ff.run()


loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test(i)) for i in os.listdir(r'D:\图片\音乐典藏馆')]
# print(task)
loop.run_until_complete(asyncio.wait(task))
loop.close()


# for i in os.listdir(r"D:\图片\音乐典藏馆"):
#     infile = r"D:\图片\音乐典藏馆" + "\\" + i
#     outfile = infile.split(".")[0] + "." + "m4a"
#     print(outfile)
#     ff = ffmpy3.FFmpeg(inputs={infile: None}, outputs={outfile: "-vn -codec copy"})
#     ff.run()
