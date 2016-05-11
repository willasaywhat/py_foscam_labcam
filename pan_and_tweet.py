from functions import *
from fi8918w import Fi8918w
from twitter import *
import os, time
import json
import requests

sec = {}

if __name__ == "__main__":
    # Pull in all the secret stuff
    execfile("secret.py", sec)

    # Set up our camera object
    labCam = Fi8918w(sec["foscam_ip"], sec["foscam_user"], sec["foscam_password"], sec["foscam_realm"])

    labCam.cam_center()
    time.sleep(20)
    labCam.cam_step_down(30)
    time.sleep(5)
    labCam.cam_step_left(360)
    print("Camera panned to leftmost stop.")

    empty_directory_silently("snapshots") # Empty the snapshots dir of all contents

    for x in range(1, 8): # Take 7 pictures, moving the camera 6 times in between.
        filepath = "snapshots\{0}.jpg".format(x)
        labCam.get_snapshot(filepath)
        print("Snapshot %s done.") % (x)

        if x < 7: # On last iteration of the loop, don't move cam, just take a pic.
            labCam.cam_step_right(56)
            time.sleep(5)

    stitch_all_images()

    # Info for the Imgur API
    file = "snapshots\pano.jpg"
    title = "FamiLAB Lobby Pano - {0}".format(datetime.datetime.utcfromtimestamp(time.time()))

    #url = upload_to_imgur(file, title, sec["imgur_id"], sec["imgur_apikey"])
    url = upload_to_s3(file, sec["ACCESS_KEY"], sec["SECRET_KEY"])

    print("Upload complete: %s") % (url)

    # Tweet it:
    twitter = Twitter(
        auth = OAuth(sec["twitter_access_key"], sec["twitter_access_secret"], sec["twitter_consumer_key"], sec["twitter_consumer_secret"]))
    results = twitter.statuses.update(status = "Front Room: "+url)
    print("Twitter posted: %s") % (results)

    # Slack it
    payload = {'text': 'Front Room: '+url}

    res = requests.post(sec["webhook_url"], data=json.dumps(payload))
    print("Slack posted: %s") % (res.text)
