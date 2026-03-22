
def fingers_up(lm):
    fingers = []
    fingers.append(lm[4].x < lm[3].x)        # Thumb
    fingers.append(lm[8].y < lm[6].y)        # Index
    fingers.append(lm[12].y < lm[10].y)      # Middle
    fingers.append(lm[16].y < lm[14].y)      # Ring
    fingers.append(lm[20].y < lm[18].y)      # Pinky
    return fingers

#END WITH TUSHAR