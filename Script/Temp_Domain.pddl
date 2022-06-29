(define (domain temp)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types temperature -object
    temp_sensor -object
    )
    
    (:predicates
    (isTempHigh ?th -temperature)
    (isTempLow ?tl -temperature)
    (isTempSensHigh ?h -temp_sensor)
    (isTempSensLow ?l -temp_sensor)
    (off_heater ?oc -temp_sensor)
    (on_heater ?xc -temp_sensor)
    )
    
    (:action SwitchOFFHeater
        :parameters (?th -temperature ?h ?oc -temp_sensor)
        :precondition (and (isTempHigh ?th) (isTempSensHigh ?h))
        :effect (off_heater ?oc)
    )
    
    (:action SwitchONHeater
        :parameters (?tl -temperature ?xc ?l -temp_sensor)
        :precondition (and (isTempLow ?tl) (isTempSensLow ?l))
        :effect (on_heater ?xc)
    )
)