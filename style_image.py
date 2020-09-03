import cv2
import imutils
from imutils import paths

def style_transfer(knot_path, style_path, file_path):
	# load the neural style transfer model from disk
	print("[INFO] loading style transfer model...")
	net = cv2.dnn.readNetFromTorch(style_path)

	# load the input image, resize it to have a width of 600 pixels, and
	# then grab the image dimensions
	image = cv2.imread(knot_path)
	image = imutils.resize(image, width=600)
	(h, w) = image.shape[:2]

	# construct a blob from the image, set the input, and then perform a
	# forward pass of the network
	blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
		(103.939, 116.779, 123.680), swapRB=False, crop=False)
	net.setInput(blob)

	output = net.forward()


	#cv2.imwrite("out_alpha.png", output)

	# reshape the output tensor, add back in the mean subtraction, and
	# then swap the channel ordering
	output = output.reshape((3, output.shape[2], output.shape[3]))
	output[0] += 103.939
	output[1] += 116.779
	output[2] += 123.680

	output = output.transpose(1, 2, 0)
	cv2.imwrite(file_path, output)





if __name__ == '__main__':
    im = "sh.jpg"


    # Style Transfer
    modelPaths = paths.list_files('models', validExts=(".t7",))
    modelPaths = sorted(list(modelPaths))

    """
    # Which Style
    s = rd.randint(0,len(modelPaths)-1)
    style_path = modelPaths[s]
    print("No of styles:",len(modelPaths))
    print("Style selected:",s)
    """


    for i in range(0,len(modelPaths)-1):
        print("Style selected:",i)
        style_path = modelPaths[i]
        out_path = "sh/"+str(i)+"_b_k.png"

        style_transfer(im, style_path, out_path)
