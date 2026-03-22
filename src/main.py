from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import cv2
import mediapipe as mp
import numpy as np
import colorsys
from src.utils import api_limiter, search_result, fingers_up
from src.db import state
import threading


app = FastAPI()

templates = Jinja2Templates(directory="src/web/templates")



def generate_frames():

    hue = 0
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 850)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils

    canvas = None
    prev_x, prev_y = None, None

    colors = [(0,255,0), (255,0,0), (0,0,255), (255,255,0)]
    color_index = 0
    draw_color = colors[color_index]


    k = 0
    temp = False
    willCrop = 0

    state.change_glow(0)
    state.change_search(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        #frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        if canvas is None:
            canvas = np.zeros_like(frame)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                
                e_point = []
                lm = hand.landmark
                finger_state = fingers_up.fingers_up(lm)

                x = int(lm[8].x * w)
                y = int(lm[8].y * h)

                #  Pinkey → clear
                if finger_state == [False, False, False, False, True]:
                    canvas = np.zeros_like(frame)
                    prev_x, prev_y = None, None
                    state.change_search(1)
                
                elif finger_state == [True, True, True, True, True]:
                    state.change_search(0)


                #  Index only → draw
                elif finger_state[1] and not finger_state[2]:
                    if prev_x is None:
                        prev_x, prev_y = x, y
                        s_point = [x,y]
                        cords = []
                    
                    hue += 0.01
                    if hue > 1:
                        hue = 0

                    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
                    draw_color = (int(b*255), int(g*255), int(r*255))
                    

                    cv2.line(canvas, (prev_x, prev_y), (x, y), draw_color, 8)

                    
                    
                    prev_x, prev_y = x, y
                    cords.append([x,y])
                    e_point = [x,y]
                    

                # Index + Middle → pause
                elif finger_state[1] and finger_state[2]:
                    prev_x, prev_y = None, None
                

                #mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)
                
                
                
        else:
            prev_x, prev_y = None, None
            canvas = np.zeros_like(frame)
            k = 0
        try:    

            if k == 0 and (e_point[0] - s_point[0] < -50 or e_point[0] - s_point[0] > 50) and (e_point[1] - s_point[1] > 50 or e_point[1] - s_point[1] < -50) :
                k = 1
                print ("start")
            if (e_point[0] - s_point[0] > -50) and (e_point[0] - s_point[0] < 50) and (e_point[1] - s_point[1] < 50) and (e_point[1] - s_point[1] > -50) and k == 1:
                k = 0
                if api_limiter.api_limit():
                    temp = True
                    print ("ready to crop")
                else:
                    print(" Limit reached ")
                max_x = 0
                min_x = cords[0][0]
                max_y = 0
                min_y = cords[0][1]
                for x,y in cords:
                    max_x = x if x > max_x else max_x
                    min_x = x if x < min_x else min_x
                    max_y = y if y > max_y else max_y
                    min_y = y if y < min_y else min_y
                
                print (max_x, min_x, max_y, min_y)
        except:
            pass
            

        if temp :
            willCrop = (willCrop + 1) % 26
            if willCrop == 25:
                crop = frame[min_y:max_y,min_x:max_x]
                
                
                
                
                try:
                    
                    state.change_glow(1)
                    t1 = threading.Thread(target=search_result.result, args=(crop,))
                    t1.start()
                    
                    
                except Exception as e:
                    print(e)
                    print ("Failed to cropped frame")
                    canvas = np.zeros_like(frame)
                    prev_x, prev_y = None, None
                    state.change_glow(0)
                
                temp = False
        
        
        output = cv2.add(frame, canvas)
        

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        ret, buffer = cv2.imencode('.jpg', output)
        outputframe = buffer.tobytes()
        
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + outputframe + b'\r\n')
        

        
    cap.release()
    
    cv2.destroyAllWindows()




@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video", response_class=HTMLResponse)
def video_page(request: Request):
    return templates.TemplateResponse("video.html", {"request": request})


@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(),
            media_type="multipart/x-mixed-replace; boundary=frame")


@app.get("/result", response_class=HTMLResponse)
def result(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})


@app.get("/check")
def check():
    return JSONResponse({"value": int(state.check_search())})


@app.get("/glow")
def glow():
    return JSONResponse({"value": int(state.check_glow())})