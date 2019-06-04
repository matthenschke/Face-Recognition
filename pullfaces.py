from PIL import Image # process imaging library
import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image) # get locations for each face

for face_location in face_locations:
    top, right, bottom, left = face_location # get each coordinate for each face location
    face_image = image[top:bottom, left:right] # create face image

    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    pil_image.save('{}.jpg'.format(top)) # save image


