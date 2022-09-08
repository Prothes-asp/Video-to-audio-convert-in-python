# Firstly import install...............[pip install moviepy]
# python version 3.9.0
# Pycharm version 2020.2.3

import moviepy.editor
from tkinter.filedialog import*

vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)
Convert_Audio = video.audio
Convert_Audio.write_audiofile("demo.mp3")
print("-----End-----")