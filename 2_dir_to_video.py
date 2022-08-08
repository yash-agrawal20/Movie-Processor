from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnail-pre-frame')
output_video = os.path.join(SAMPLE_OUTPUTS, "thumbs.mp4")

this_dir = os.listdir(thumbnail_dir)
# filepath = []
# for fname in this_dir:
#     if fname.endswith("jpg"):
#         path = os.path.join(thumbnail_dir, fname)
#         filepath.append(path)

#Ordering the images present in the thumbnail_per_frame_dir based on name:
directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)

#From images creating video
clip = ImageSequenceClip(new_paths, fps=10)
clip.write_videofile(output_video)

 