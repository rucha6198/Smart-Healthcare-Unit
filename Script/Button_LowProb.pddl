(define (problem Fire_alarmProblem) (:domain Fire_alarm)

(:objects 
 button_high button_low button_ambient -button
 b_high b_low b_none -button_sensor
)

(:init
    (isButtonHigh button_high)
    (isButtonSensHigh b_high)
    (isButtonLow button_low)
    (isButtonSensLow b_low)
)

(:goal (off_buzzer b_low)
)
)