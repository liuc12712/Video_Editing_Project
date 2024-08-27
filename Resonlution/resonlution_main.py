import subprocess
def resonlution():
    print('*' * 10, '已进入程序，请按指示操作', '*' * 10)

    # 用户输入视频和输出视频的路径
    information_input = input('请输入原视频的路径:')
    information_output = input('请输入视频编辑后未来的路径:')

    # 目标分辨率（例如：1280x720）
    print('请选择输出视频的分辨率\n1.360p (640x360)  2.480p (854x480)  3.720p (1280x720)\n4.1080p (1920x1080)  5.1440p (2560x1440)  6.2160p (3840x2160)\n7.4320p (7680x4320)')
    print('-'*40)

    while True:
        try:
            num_resolution = int(input('请输入要更改分辨率的编号(只允许填写所示分辨率前面的阿拉伯数字编号):'))
        except ValueError:
            print('请填写有效数字')
            continue
        break

    if num_resolution==1:
        resolution_video='640x360'
    elif num_resolution==2:
        resolution_video='854x480'
    elif num_resolution==3:
        resolution_video='1280x720'
    elif num_resolution==4:
        resolution_video='1920x1080'
    elif num_resolution==5:
        resolution_video='2560x1440'
    elif num_resolution==6:
        resolution_video='3840x2160'
    elif num_resolution==7:
        resolution_video='7680x4320'
    else:
        print('输入的数字有误')


    # 定义 FFmpeg 命令
    command = [
        'ffmpeg', '-i', information_input,
        '-vf', f'scale={resolution_video}',
        '-c:a', 'copy',  # 保持音频不变
        information_output
    ]

    # 使用 subprocess 运行命令
    subprocess.run(command)
