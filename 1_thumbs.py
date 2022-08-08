from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnail-pre-frame')
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)


clip = VideoFileClip(source_path)
#Reading the Frames Per second
print(clip.reader.fps)
#Reading the total number of frames
print(clip.reader.nframes)
#Duration of the video in second
#(fps)*(duration) = (nframes)
print(clip.duration)

#Capturing the frames at every second (30)
duration = int(clip.duration)
for i in range(0, duration + 1):
    # print(f"Frame at {i} second")
    #Gives the color value at each pixel in that frame
    #in the form of an array
    frame = clip.get_frame(i)
    # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    # print(f"Frame at {i} seconds is saved at {new_img_filepath}.")
    #Using Pillow (PIL) library to convert array to function
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

#Capturing all the frames (900)
#iterate frame
for i, frame in enumerate(clip.iter_frames()):
    new_img_filepath = os.path.join(thumbnail_per_frame_dir, f"{i}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)


