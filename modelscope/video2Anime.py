# coding=utf-8
import ffmpy3
import os


def video2img(infile, outdir="./"):
    output_dir = outdir  + "\\input\\" + '%4d.jpeg'
    ff = ffmpy3.FFmpeg(
        inputs={infile: None},
        outputs={output_dir: [
            # '-t', '30',
            '-s', '1920x1080',
            '-r', '30'
        ]}
    )

    ff_audio = ffmpy3.FFmpeg(
        inputs={infile: None},
        outputs={'{}\\input.mp3'.format(outdir): [
            # '-t', '30',
            '-r', '30',
            '-vn'
        ]}
    )
    # print(ff_audio.cmd)
    # print(ff.cmd)
    ff.run()
    ff_audio.run()
    return "Finished!!"


def img2anime(input_dir, output_dir):

    imgs_list = os.listdir(input_dir)
    import cv2
    from modelscope.pipelines import pipeline
    from modelscope.utils.constant import Tasks

    # 方法1：:每张图片调用一次pipline
    img_cartoon = pipeline(
        Tasks.image_portrait_stylization,
        # 人像卡通化模型
        # model='damo/cv_unet_person-image-cartoon_compound-models',
        # 人像卡通化模型-3D
        # model='damo/cv_unet_person-image-cartoon-3d_compound-models',
        # 人像卡通化模型-素描
        # model='damo/cv_unet_person-image-cartoon-sketch_compound-models',
        # 人像卡通化模型-手绘风
        # model='damo/cv_unet_person-image-cartoon-handdrawn_compound-models',
        # 人像卡通化模型-艺术风
        model='damo/cv_unet_person-image-cartoon-artstyle_compound-models',
    )
    for img in imgs_list:
        frame = cv2.imread(input_dir + "\\" + img)
        result = img_cartoon(frame)
        file_name_pre = img.split(".")[0]
        out_file_name = '{}\\{}.jpeg'.format(output_dir, file_name_pre)
        cv2.imwrite(out_file_name, result["output_img"])
        # break 
    return "Finished!!"


def img2video(imagedir, audio_file, outdir="./"):
    output = outdir + '\\output.mp4'
    # ffmpeg -r 15 -f images -i %d.jpeg -s 1920x1080 output.mp4
    ff = ffmpy3.FFmpeg(
        inputs={
            imagedir + "\\" + '%4d.jpeg': [
                '-r', '30',
                '-f', 'image2'
            ],
            audio_file: None
        },
        outputs={output: [
            '-s', '1920x1080',
            '-b:v', '5000k'
        ]}
    )

    print(ff.cmd)
    ff.run()

    return ff.cmd


if __name__ == "__main__":
    # video2img(infile="D:\headD\headD.flv", outdir="D:\headD")
    # print(img2anime(input_dir="D:\headD\input", output_dir="D:\headD\output"))
    img2video(imagedir="D:\headD\output", audio_file="D:\headD\input.mp3", outdir="D:\headD")
