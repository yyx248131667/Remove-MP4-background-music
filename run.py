from moviepy.editor import VideoFileClip
import os

# 输入文件夹路径，包含要处理的多个视频文件
input_folder = r'D:\tiktok\douyin-downloader-main\Downloaded\d\post'

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(input_folder, f"no_audio_{filename}")

        # 加载视频
        video_clip = VideoFileClip(input_path)

        # 去掉音频
        video_clip = video_clip.set_audio(None)

        # 保存去掉音乐后的视频
        video_clip.write_videofile(output_path, codec='libx264')

        print(f"已去掉 {filename} 的音乐，保存为 {output_path}")

print("批量去掉音乐完成")
