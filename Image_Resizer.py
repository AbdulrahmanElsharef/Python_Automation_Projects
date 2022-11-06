from PIL import Image


def image_resize():
    '''create a python function that takes an image path , the the
needed image size then resize the image to this size and save it in the same folder'''
    image = Image.open('F:\\Download\\Image_1.jpg')
    print(f"Original size : {image.size}") # 5464x3640
    sunset_resized = image.resize((400, 400))
    sunset_resized.save('sunset_400.jpeg')
    print(f"Original size : {sunset_resized.size} & image_resize is finshed ....")
image_resize()
