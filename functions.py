import cv2

def function_one():
    cap = cv2.VideoCapture(2)
    while True:
        ret, image_np = cap.read()

        cv2.imshow('object Detection', image_np)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows
            break
        abc = { 'a': "WOW", 'b': "WIW", 'c':"WEW"}
    return(abc)


def get_string():
    xyz = { 'x': "WOW", 'y': "WIW", 'z':"WEW"}
    return(xyz)

def get_string2():
    def get_string3():
        xyz = { 'x': "WOW", 'y': "WIW", 'z':"WEW"}
        return(xyz)


