"""A script for building all of the files to be put together."""
import subprocess
import shutil
import os

video_directory = "video"

# from scratch!
if os.path.exists(video_directory):
    shutil.rmtree(video_directory)

# call Manim
subprocess.Popen(["manim", "scenes.py", "-a"]).communicate()

# rename to [1..n].mp4
for scene in os.listdir(video_directory):
    if os.path.isdir(os.path.join(video_directory, scene)):
        with open(os.path.join(video_directory, scene, "partial_movie_file_list.txt")) as f:
            for i, video in enumerate(f.read().splitlines()[1:]):
                path, name = os.path.split(video[11:-1])
                
                original_path = os.path.join(path, name)
                changed_path = os.path.join(path, f"{i+1}.mp4")
                image_path = os.path.join(path, f"{i+1}.png")

                os.rename(original_path, changed_path)

                # save the last frames
                subprocess.Popen(["ffmpeg", "-sseof", "-3", "-i",  changed_path, "-update", "1", "-q:v", "1", image_path]).communicate()
