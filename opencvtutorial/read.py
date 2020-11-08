import cv2 as cv #import the opencv library

img = cv.imread('../how_performance_art_took_over_the_art_world_900x450_c.jpg') #takes in path to an image, returns as matrix of pixels

# pass in two params - name of window, and matrix of pixels to display - we set this as img above
cv.imshow('Art', img)

def rescaleFrame(frame, scale=0.75):
    # works for live video, images, saved videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #resize frame to particular scaled value

def changeRes(width, height):
    # only works for live video
    capture.set(3, width) # 3 references width
    capture.set(4, height) # 4 references height

# waits for a specific delay for a key to be pressed - 0, waits for infinite amount of time for key to be pressed.
#always use this to run it
cv.waitKey(0)
#python read.py



# READING VIDEOS
# capture = cv.VideoCapture('../../../Movies/TheNatureofLight-byCoronetInstructionalFilms_PrelingerArchives1948.m4v') #path to a video file - provide an integer for what camera. enter '0' for your computer camera
# #capture is instance of Video capture class

while True:
    # grab video frame by frame
    isTrue, frame = capture.read() #reads in video frame by frame
    
    frame_resized = rescaleFrame(frame, scale=0.2)
    # display each frame of the video
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) and 0xFF==ord('d'): #if letter d is pressed, then break out of loop
        break

capture.release()
cv.destroyAllWindows()

