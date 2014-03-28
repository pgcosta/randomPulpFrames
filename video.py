from moviepy.editor import *
import random
max_len=8988


random_t = random.randint(0,max_len)
video = VideoFileClip("video.mp4")
video.save_frame('frame.jpg', random_t)
