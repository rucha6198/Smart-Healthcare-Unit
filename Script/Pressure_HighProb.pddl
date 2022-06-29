(define (problem PressureProblem) (:domain pres)

(:objects 
 pres_high pres_low pres_ambient -pressure
 p_high p_low p_none -pressure_sensor
)

(:init
    (isPresHigh pres_high)
    (isPresSensHigh p_high)
    (isPresLow pres_low)
    (isPresSensLow p_low)
)

(:goal (off_LED p_high)
)
)