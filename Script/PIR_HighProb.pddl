(define (problem MotionProblem) (:domain motion)

(:objects 
 PIR_high PIR_low PIR_ambient -PIR
 p_high p_low p_none -PIR_sensor
)

(:init
    (isPIRHigh PIR_high)
    (isPIRSensHigh p_high)
    (isPIRLow PIR_low)
    (isPIRSensLow p_low)
)

(:goal (on_light p_high)
)
)