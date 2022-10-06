import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"ok.mp4")
my_clip.audio.write_audiofile(r"my_result2.wav")
