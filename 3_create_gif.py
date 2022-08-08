from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all import crop

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)
output_path1 = os.path.join(GIF_DIR, "sample1.gif")
output_path2 = os.path.join(GIF_DIR, "sample2.gif")

clips = VideoFileClip(source_path)
fps = clips.reader.fps
#Time interval to make the GIF at
subclip = clips.subclip(10, 20)
#Using crop
subclip = subclip.resize(width=320, height=320)
# subclip.write_gif(output_path1, fps=20, program=" ffmpeg")

w, h = clips.size
subclip2 = clips.subclip(10, 20)
squared_cropped_clip = crop(subclip2, width=320, height=320, x_center=w/2, y_center=h/2)
squared_cropped_clip.write_gif(output_path2, fps, program="ffmpeg")



