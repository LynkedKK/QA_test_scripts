import base64
from lib.config import *

def saveRecordingScreen(driver, video_name):
  video_rawdata = driver.stop_recording_screen()

  filepath = os.path.join("{}/{}.mp4".format(VIDEO_PATH, video_name))
  with open(filepath, "wb") as vd:
      vd.write(base64.b64decode(video_rawdata))
