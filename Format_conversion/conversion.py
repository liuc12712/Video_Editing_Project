import subprocess
def con():
    print('*' * 10, '已进入程序，请按指示操作', '*' * 10)

    # 输入和输出文件路径
    print('请选择要转换成什么格式的视频文件:\n1.MP4  2.AVI  3.MKV\n4.MOV  5.WMV  6.FLV\n7.WEBM  8.OGV')
    print('-'*40)

    while True:
        try:
            choose_num1 = int(input('请输入要转成的格式(只允许填写格式前面的阿拉伯数字编号):'))
        except ValueError:
            print('请填写有效数字')
            continue
        break


    # 用户选择判断
    if choose_num1 == 1:
        format='.mp4'
    elif choose_num1 == 2:
        format='.avi'
    elif choose_num1 == 3:
        format='.mkv'
    elif choose_num1 == 4:
        format='.mov'
    elif choose_num1 == 5:
        format='.wmv'
    elif choose_num1 == 6:
        format='.flv'
    elif choose_num1 == 7:
        format='.webm'
    elif choose_num1 == 8:
        format='.ogv'
    else:
        print('请输入有效数字')

    input_file = input('请输入原视频文件路径(需要指定到视频文件)')
    folder = input('请输入视频文件要存放的位置路径(指定到文件夹即可)')

    output_file = f'{folder}\\output_video{format}'

    # 构造 ffmpeg 命令
    command = [
        'ffmpeg',
        '-i', input_file,  # 指定输入文件
        output_file        # 指定输出文件及格式
    ]

    # 执行命令
    subprocess.run(command)
    print(f'文件目录:{folder}\\output_video{format}')
