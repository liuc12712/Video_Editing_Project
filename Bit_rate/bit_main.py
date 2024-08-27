import subprocess
def bit():
    print('*' * 10, '已进入程序，请按指示操作', '*' * 10)

    # 输入和输出文件路径
    input_file = input('请输入原视频的路径:')
    output_file = input('请输入视频编辑后未来的路径:')

    # 设置比特率、锐化强度和色彩锐化强度
    bitrate = input('请输入您要更改的视频比特率:')                # 比特率
    sharpen_amount = input('请输入锐化程度:')          # 锐化强度
    chroma_amount = input('请输入色彩锐化强度:')           # 色彩锐化强度

    # 构造 ffmpeg 命令
    command = [
        'ffmpeg',
        '-i', input_file,  # 输入文件
        '-b:v', bitrate,   # 设置视频比特率
        '-vf', (
            f'unsharp=luma_msize_x=3:luma_msize_y=3:luma_amount={sharpen_amount}:'
            f'chroma_msize_x=3:chroma_msize_y=3:chroma_amount={chroma_amount},'
            f'yadif,'
            f'eq=brightness=0.08:contrast=1.4:saturation=1.5:gamma=1.2'
        ),  # 应用锐化和色彩增强
        output_file        # 输出文件
    ]

    # 执行命令
    subprocess.run(command)
