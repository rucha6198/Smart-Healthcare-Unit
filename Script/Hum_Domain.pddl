(define (domain humidity)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types hum -object
    hum_sensor -object
    )
    
    (:predicates

    (isHumHigh ?hum_h -hum)
    (isHumLow ?hum_l -hum)
    (isHumSensHigh ?high -hum_sensor)
    (isHumSensLow ?low -hum_sensor)
    (off_humidifier ?oc -hum_sensor)
    (on_humidifier ?xc -hum_sensor)
    )
    

    (:action SwitchOFFHumidifier
        :parameters (?hum_h -hum ?high ?oc -hum_sensor)
        :precondition (and (isHumHigh ?hum_h) (isHumSensHigh ?high))
        :effect (off_humidifier ?oc)
    )
    
    (:action SwitchONHumidifier
        :parameters (?hum_l -hum ?xc ?low -hum_sensor)
        :precondition (and (isHumLow ?hum_l) (isHumSensLow ?low))
        :effect (on_humidifier ?xc)
    )
)