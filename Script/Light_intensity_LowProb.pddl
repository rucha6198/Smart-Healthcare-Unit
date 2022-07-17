(define (problem BrightnessProblem) (:domain light_intensity)

(:objects 
 light_high light_low light_ambient -light
 l_high l_low l_none -light_sensor
)

(:init
    (isBrightnessHigh light_high)
    (isBrightnessSensHigh l_high)
    (isBrightnessLow light_low)
    (isBrightnessSensLow l_low)
)

(:goal (off_led l_low)
)
)