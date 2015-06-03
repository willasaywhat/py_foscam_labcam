import shutil, os, errno, time, base64, json, requests, datetime
from PIL import Image
from base64 import b64encode

def empty_directory_silently(directory):
    try:
        os.makedirs(directory)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    
    time.sleep(0.5)
    
    shutil.rmtree(directory)
    time.sleep(0.5)
    os.makedirs(directory)
  
def stitch_all_images():
    im1 = Image.open("snapshots\\1.jpg")
    im2 = Image.open("snapshots\\2.jpg")
    im3 = Image.open("snapshots\\3.jpg")
    im4 = Image.open("snapshots\\4.jpg")
    im5 = Image.open("snapshots\\5.jpg")
    im6 = Image.open("snapshots\\6.jpg")
    im7 = Image.open("snapshots\\7.jpg")

    # Creates a new empty image, RGB mode, and size 640 by 480 * 7. (Since we have 7 snapshots)
    new_im = Image.new('RGB', (4480,480))

    # Iterate through a 1 by 7 grid with 480 spacing, to make pano
    new_im.paste(im1, (640 * 0, 0))
    new_im.paste(im2, (640 * 1, 0))
    new_im.paste(im3, (640 * 2, 0))
    new_im.paste(im4, (640 * 3, 0))
    new_im.paste(im5, (640 * 4, 0))
    new_im.paste(im6, (640 * 5, 0))
    new_im.paste(im7, (640 * 6, 0))

    new_im.save("snapshots\pano.jpg")
    
def upload_to_imgur(file, title, client_id, api_key):
        headers = {"Authorization": "Client-ID {0}".format(client_id)}
        
        url = "https://api.imgur.com/3/upload.json"
        
        j1 = requests.post(
            url, 
            headers = headers,
            data = {
                "key": api_key, 
                "image": b64encode(open(file, "rb").read()),
                "type": "base64",
                "name": title,
                "title": title
            }
        )
    
        data_back = json.loads(j1.content)
        
        return data_back["data"]["link"]