import PIL.ImageOps 
from PIL import Image

def color_invert(image_path):

    image = Image.open(image_path)
    print("inverting.... image.mode =",image.mode)
    if image.mode == 'RGBA':
        r,g,b,a = image.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        #r2,g2,b2 = inverted_image.split()

        #final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

        #final_transparent_image.save('new_file.png')

    else:
        inverted_image = PIL.ImageOps.invert(image)
        #inverted_image.save('new_name3.png')
    
    return(inverted_image)

if __name__ == '__main__':

    for i in range(0,13):
        im_path = "sh/"+str(i)+ "_b_k.png"
        out_path = "sh/"+str(i)+ "_b_k_ex.png"
        inverted = color_invert(im_path)
        inverted.save(out_path,quality=95)

