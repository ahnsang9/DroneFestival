import cv2
import logging as log
import time





O = (0,0)
sheep_frame  = [xmax, ymax, xmin, ymin] #objectdetector에서 보낸 양의 프레임값
door_frame = [amax, bmax, xmin, ymin] #objectdetector에서 보낸 양의 프레임값
sheep_position = [int((xmax+xmin)/2),0] #양 frame x축 값의 평균
door_position = [int((amax+xmin)/2),0] #문 frame x축 값의 평균
Difference_sheep = int(O[0] - sheep_position) #양 frame 가운데 점과 원점데 대한 x축 차이값
Difference_door = int(O[0] - door_) #문 frame 가운데 점과 원점데 대한 x축 차이값
'''
Label_sheep = 1 : 화면 안에 양 인식 O
Label_sheep = 0 : 화면 안에 양 인식 X
Label_Door = 1 : 화면 안에 문 인식 O
Label_Door = 0 : 화면 안에 문 인식 X
'''
Label_sheep = 0
Label_door = 0
sheperd_Mode = 0


while sheperd_Mode == 1:
    i = 0
    if Label_sheep == 0:
        while Label_sheep == 1:
            cv2.socket("CW, %d" %5)
            i = i + 5
            if i == 1080:
                cv2.socket("land")
                time.sleepy(3)
                i = 0
                sheperd_Mode = 0
                log.info("더 이상 탐지되는 양이 없습니다.")


    else :
        while Label_sheep == 0:
            if -2>=Difference_sheep or 2<=Difference_sheep:
                if Difference_sheep < 0:
                    while -2 < Difference_sheep < 2 :
                        cv2.socket("CW, %d" %5)

                else :
                    while -2 < Difference_sheep < 2 :
                        cv2.socket("CCW, %d" %5)

            else :
                if xmax-xmin < 30:
                    while xmax-xmin > 30:
                        cv2.socket("foward, %d" %20)

            if Label_door is False:
                while Label_door and -2 < Difference_door < 2:
                    cv2.socket("circle")

            else :
                cv2.socket("flip r")
                cv2.socket("flip l")
                if amax-amin < 60:
                    while amax-amin > 60:
                        cv2.socket("forward %d" %30)




