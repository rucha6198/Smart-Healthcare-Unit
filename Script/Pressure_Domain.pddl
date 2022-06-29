(define (domain pres)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types pressure -object
    pressure_sensor -object
    )
    
    (:predicates
    (isPresHigh ?ph -pressure)
    (isPresLow ?pl -pressure)
    (isPresSensHigh ?h -pressure_sensor)
    (isPresSensLow ?l -pressure_sensor)
    (off_LED ?oc -pressure_sensor)
    (on_LED ?xc -pressure_sensor)
    )
    
    (:action SwitchOFF_LED
        :parameters (?ph -pressure ?h ?oc -pressure_sensor)
        :precondition (and (isPresHigh ?ph) (isPresSensHigh ?h))
        :effect (off_LED ?oc)
    )
    
    (:action SwitchON_LED
        :parameters (?pl -pressure ?xc ?l -pressure_sensor)
        :precondition (and (isPresLow ?pl) (isPresSensLow ?l))
        :effect (on_LED ?xc)
    )
) 