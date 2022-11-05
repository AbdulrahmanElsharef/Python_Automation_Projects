from pytube import YouTube
import os
from pathlib import Path


def video_download():
    '''function  has one parameter which is the location where to download the file.'''
    link = input("Enter link here: ")
    # input link of video
    link_url = YouTube(link)
    # link of the video to be downloaded
    print("downloading....")
    # print("downloading")
    video = link_url.streams.get_highest_resolution()
    # resolution passed in the get() function
    path_to_download_folder = (
        r"J:\Abdo_BackEnd\Django_FullStack_Project\Python_Dev\01_Python_Basics\intermediat_python")
    # where to save
    video.download(path_to_download_folder)
    # downloading the video


download = video_download()
