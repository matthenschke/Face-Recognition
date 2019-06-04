import face_recognition

image = face_recognition.load_image_file('./img/groups/team2.jpg') # load image

face_locations = face_recognition.face_locations(image) # get coordinates for each face

# Array of coordinates for each face
print(face_locations)

print('There are {} people in this image'.format(len(face_locations)))
