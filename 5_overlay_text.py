from pyparsing import withAttribute
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, "audio.mp3")
mix_audio_dir = os.path.join(SAMPLE_OUTPUTS, 'mixed-audio')
os.makedirs(mix_audio_dir, exist_ok=True)
#Original audio
og_audio_path = os.path.join(mix_audio_dir, 'og.mp3')
final_audio_path = os.path.join(mix_audio_dir, "overlay-audio.mp3")
final_video_path = os.path.join(mix_audio_dir, "overlay-video.mp4")

clip = VideoFileClip(source_path)

original_audio = clip.audio
original_audio.write_audiofile(og_audio_path)

audio_clip = AudioFileClip(source_audio_path)

#Time in sec
w, h = clip.size();
intro_duration = 5
intro_text = TextClip("Hello World", fontsize=70, color='white', size=clip.size)
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_fps(clip.fps)
intro_text = intro_text.set_pos("center")
intro_music = audio_clip.subclip(0, intro_duration)

intro_text = intro_text.set_audio(intro_music)

# intro_text.write_videofile(final_video_path)
watermark_size = 60
watermark_text = TextClip("Yash", fontsize=30, color='white', align='East', size=(w,watermark_size))
watermark_text = watermark_text.fps(clip.fps)
watermark_text = watermark_text.duration(clip.reader.duration)
watermark_text = watermark_text.set_position(("bottom"))

# cvc = CompositeVideoClip([watermark_text], size=clip.size)
# cvc = cvc.set_duration(clip.reader.duration)
# cvc = cvc.set_fps(clip.fps)
# cvc = cvc.set_audio(None)

overlay_clip = CompositeVideoClip([clip, watermark_text], size=clip.size)
overlay_clip = overlay_clip.set_duration(clip.reader.duration)
overlay_clip = overlay_clip.set_fps(clip.fps)
overlay_clip = overlay_clip.set_audio(None)
overlay_clip = overlay_clip.set_audio(AudioFileClip(og_audio_path))


final_clip = concatenate_videoclips([intro_text, clip])
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")
