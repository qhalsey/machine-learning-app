import face_recognition
import cv2
import subprocess
from gtts import gTTS
import createPeopleObjects

peopleSeen = []

def sayName(name):
    if checkIfSeen(name) == False:
        peopleSeen.append(name)
        audio_file = "hello.mp3"
        tts = gTTS(text="Hello " + name + ". Hope you have a great day!", lang="en")
        tts.save(audio_file)
        return_code = subprocess.call(["afplay", audio_file])

def checkIfSeen(name):
    if name in peopleSeen:
        return True
    else:
        return False

# Create arrays of known face encodings and their names
arr_of_people = createPeopleObjects.instantiateObjectes()

known_face_encodings = []
known_face_names = []


for x in range(len(arr_of_people)):
    a = face_recognition.load_image_file(arr_of_people[x].imagename)
    known_face_encodings.append(face_recognition.face_encodings(a)[0])
    full_name = arr_of_people[x].firstname + " " + arr_of_people[x].lastname
    known_face_names.append(full_name)

print(len(arr_of_people))

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        print(matches)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            sayName(known_face_names[first_match_index])
            print(name)

        #Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    #Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()