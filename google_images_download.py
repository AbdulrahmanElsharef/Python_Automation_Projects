
# - Google Image Downloader : create a python function that takes a url of an
# image from google and save location , then download the image in the save
# location

from bing_image_downloader import downloader
from google_images_download import google_images_download  # importing the library


def google_images():
    response = google_images_download.googleimagesdownload()  # class instantiation
    arguments = {"keywords": "Polar bears,baloons,Beaches",
                 "limit": 20, "print_urls": True}  # creating list of arguments
    # passing the arguments to the function
    paths = response.download(arguments)
    return (paths)  # printing absolute paths of the downloaded images


downlad = google_images()


'''query_string : String to be searched.
limit : (optional, default is 100) Number of images to download.
output_dir : (optional, default is 'dataset') Name of output dir.
adult_filter_off : (optional, default is True) Enable of disable adult filteration.
force_replace : (optional, default is False) Delete folder if present and start a fresh download.
timeout : (optional, default is 60) timeout for connection in seconds.
filter : (optional, default is "") filter, choose from [line, photo, clipart, gif, transparent]
verbose : (optional, default is True) Enable downloaded message.

You can also test the programm by runnning test.py keyword'''


def google_images():
    query_searsh = "dogs,cars,baby"
    downloader.download(query_searsh, limit=100,  output_dir='dataset',
                        adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


downlad = google_images()
