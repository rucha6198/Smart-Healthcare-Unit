(define (domain light_intensity)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types light -object
    light_sensor -object
    )
    
    (:predicates
    (isBrightnessHigh ?light_h -light)
    (isBrightnessLow ?light_l -light)
    (isBrightnessSensHigh ?h -light_sensor)
    (isBrightnessSensLow ?l -light_sensor)
    (off_led ?oc -light_sensor)
    (on_led ?xc -light_sensor)
    )
    
    (:action SwitchOFFled
        :parameters (?light_h -light ?h ?oc -light_sensor)
        :precondition (and (isBrightnessHigh ?light_h) (isBrightnessSensHigh ?h))
        :effect (off_led ?oc)
    )
    
    (:action SwitchONled
        :parameters (?light_l -light ?xc ?l -light_sensor)
        :precondition (and (isBrightnessLow ?light_l) (isBrightnessSensLow ?l))
        :effect (on_led ?xc)
    )
)