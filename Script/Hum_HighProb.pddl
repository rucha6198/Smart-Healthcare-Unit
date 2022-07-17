(define (problem HumProblem) (:domain humidity)

(:objects 
 hum_high hum_low hum_ambient -hum
 h_high h_low h_none -hum_sensor
)

(:init
    (isHumHigh hum_high)
    (isHumSensHigh h_high)
    (isHumLow hum_low)
    (isHumSensLow h_low)
)

(:goal (off_humidifier h_high)
)
)