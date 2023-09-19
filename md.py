import os
import cv2
import random
import time

# 获取视频文件夹路径
video_folder = input("请输入视频文件夹路径：")

# 检查路径是否存在
if not os.path.exists(video_folder):
    print("指定的文件夹路径不存在")
else:
    # 获取视频文件列表
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

    # 循环处理每个视频文件
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        cap = cv2.VideoCapture(video_path)

        # 获取视频帧率
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 创建一个目录用于存储删除帧后的视频
        output_folder = os.path.join(video_folder, 'frames_removed')
        os.makedirs(output_folder, exist_ok=True)

        output_file = os.path.join(output_folder, video_file)

        # 定义间隔时间范围
        min_interval = 3  # 最小间隔3秒
        max_interval = 5  # 最大间隔5秒

        # 初始化计数器和计时器
        frame_count = 0
        start_time = time.time()

        # 打开一个新的视频写入器
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            out.write(frame)

            # 生成随机间隔
            interval = random.randint(min_interval, max_interval)

            # 如果达到间隔时间或处理到视频末尾，则删除当前帧
            if frame_count % (fps * interval) == 0 or frame_count == total_frames:
                frame_count = 0
                end_time = time.time()
                elapsed_time = end_time - start_time
                if elapsed_time < interval:
                    time.sleep(interval - elapsed_time)

        cap.release()
        out.release()

    print("视频帧已删除完成")
