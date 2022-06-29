(define (domain motion)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types PIR -object
    PIR_sensor -object
    )
    
    (:predicates
    (isPIRHigh ?pir_h -PIR)
    (isPIRLow ?pir_l -PIR)
    (isPIRSensHigh ?h -PIR_sensor)
    (isPIRSensLow ?l -PIR_sensor)
    (off_light ?oc -PIR_sensor)
    (on_light ?xc -PIR_sensor)
    )
    
 (:action SwitchOFFLight
        :parameters (?pir_l -PIR ?oc ?l -PIR_sensor)
        :precondition (and (isPIRLow ?pir_l) (isPIRSensLow ?l))
        :effect (off_light ?oc)
    )

  (:action SwitchONLight
        :parameters (?pir_h -PIR ?h ?xc -PIR_sensor)
        :precondition (and (isPIRHigh ?pir_h) (isPIRSensHigh ?h))
        :effect (on_light ?xc)
    )
    
   
)