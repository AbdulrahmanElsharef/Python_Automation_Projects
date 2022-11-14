
# - Google Image Downloader : create a python function that takes a url of an
# image from google and save location , then download the image in the save
# location

from bing_image_downloader import downloader


def google_images():
    strings_searsh = "dress,laptop,kids"
    downloader.download(strings_searsh, limit=30,  output_dir='F:\\Download\\photos',
                        adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


downlad = google_images()
