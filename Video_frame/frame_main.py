import subprocess

# 使用 FFmpeg 将视频提升到指定帧数
def frame():
    print('*'*10,'已进入程序，请按指示操作','*'*10)
    # 用户输入视频和输出视频的路径
    information_input = input('请输入原视频的路径:')
    information_output = input('请输入视频编辑后未来的路径:')
    # 用户输入视频的帧率
    frame = input('请输入目标视频的帧率:')
    command_frame = [
        'ffmpeg', '-i', information_input,
        '-vf', f"minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps={frame}'",
        information_output
    ]

    # 调用 FFmpeg
    subprocess.run(command_frame)
