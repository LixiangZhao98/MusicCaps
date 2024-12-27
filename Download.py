from datasets import load_dataset

# 加载 MusicCaps 数据集
dataset = load_dataset("google/MusicCaps", split="train")

# 查看数据集的前几个样本
print(dataset[0])

import subprocess
import os
from pathlib import Path
import re

def sanitize_filename(filename):
    """清理非法文件名字符"""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_clip(video_id, output_path, start_time, end_time, tmp_dir="./tmp", num_attempts=3):
    """
    下载指定的 YouTube 音频片段。
    """
    tmp_dir = Path(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)  # 确保临时目录存在

    output_path = Path(output_path)
    output_path = output_path.parent / sanitize_filename(output_path.name)  # 清理文件名
    output_path.parent.mkdir(parents=True, exist_ok=True)  # 确保输出目录存在

    if start_time >= end_time:
        raise ValueError(f"开始时间 ({start_time}) 必须小于结束时间 ({end_time})")

    command = [
        "yt-dlp",
        "--cookies", "cookies.txt",
        "--quiet",
        "--no-warnings",
        "--force-keyframes-at-cuts",
        "-x",
        "--audio-format", "wav",
        "-f", "bestaudio",
        "-o", str(output_path),
        "--download-sections", f"*{start_time}-{end_time}",
        f"https://www.youtube.com/watch?v={video_id}"
    ]

    attempts = 0
    while attempts < num_attempts:
        try:
            subprocess.run(command, check=True)
            if output_path.exists():
                return True
        except subprocess.CalledProcessError as e:
            print(f"下载失败，重试中 ({attempts + 1}/{num_attempts})...")
        attempts += 1

    return False

from pathlib import Path

def download_musiccaps(data_dir, limit=None):
    """
    下载 MusicCaps 数据集中的音频片段。

    参数:
        data_dir (str): 保存音频的目录。
        limit (int): 限制下载的样本数量（可选）。
    """
    # 加载数据集
    dataset = load_dataset("google/MusicCaps", split="train")
    if limit:
        dataset = dataset.select(range(limit))

    # 创建保存目录
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)

    for i, example in enumerate(dataset):
        video_id = example["ytid"]
        start_time = example["start_s"]
        end_time = example["end_s"]
        output_path = data_dir / f"{video_id}.wav"

        if output_path.exists():
            print(f"[{i+1}] 已存在，跳过: {output_path}")
            continue

        print(f"[{i+1}] 下载: {video_id} -> {output_path}")
        success = download_clip(
            video_id=video_id,
            output_path=str(output_path),
            start_time=start_time,
            end_time=end_time
        )
        if not success:
            print(f"下载失败: {video_id}")
            
# 下载前 10 个样本
# download_musiccaps(data_dir="./musiccaps_data", limit=10)
download_musiccaps(data_dir="./musiccaps_data")
import os

# 列出下载的文件
files = os.listdir("./musiccaps_data")
print("下载的文件:", files)

# Resampling
# from pydub import AudioSegment

# def resample_audio(file_path, target_sample_rate=16000):  
#     audio = AudioSegment.from_file(file_path)
#     audio = audio.set_frame_rate(target_sample_rate)
#     audio.export(file_path, format="wav")