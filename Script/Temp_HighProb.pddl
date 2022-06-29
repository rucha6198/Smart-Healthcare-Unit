(define (problem TempProblem) (:domain temp)

(:objects 
 temp_high temp_low temp_ambient -temperature
 t_high t_low t_none -temp_sensor
)

(:init
    (isTempHigh temp_high)
    (isTempSensHigh t_high)
    (isTempLow temp_low)
    (isTempSensLow t_low)
)

(:goal (off_heater t_high)
)
)