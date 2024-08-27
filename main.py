import hello
import Video_frame.frame_main
import Resonlution.resonlution_main
import Bit_rate.bit_main
import Format_conversion.conversion

hello.info() # 介绍一下程序作为开始
print(hello.segmentation) # 分隔符而已
print('请选择您要执行的模式')
print('1.视频帧数调节     2.视频比特率,锐化程度,色彩强度调节     3.视频分辨率调节\n4.视频转码')
print('-'*40)
# 判断输入是否为阿拉伯整数数字

while True:
    try:
        choose_num=int(input('请输入要执行模式的编号(只允许填写模式前面的阿拉伯数字编号):'))
    except ValueError:
        print('请填写1-5以内的有效数字')
        continue
    break


if choose_num==1:
    Video_frame.frame_main.frame()
elif choose_num==2:
    Bit_rate.bit_main.bit()
elif choose_num==3:
    Resonlution.resonlution_main.resonlution()
elif choose_num==4:
    Format_conversion.conversion.con()
else:
    print('请填写有效数字')
print('请在目标文件夹查看，退出终端代表程序结束')
input()








