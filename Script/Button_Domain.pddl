(define (domain Fire_alarm)

    (:requirements
        :strips
        :typing
        :negative-preconditions
    )
    (:types  button -object
    button_sensor -object
    )
    
    (:predicates
    (isButtonHigh ?bh -button)
    (isButtonLow ?bl -button)
    (isButtonSensHigh ?h -button_sensor)
    (isButtonSensLow ?l -button_sensor)
    (off_buzzer ?oc -button_sensor)
    (on_buzzer ?xc -button_sensor)
    )
    
    (:action SwitchOFF_buzzer
        :parameters (?bh -button ?h ?oc -button_sensor)
        :precondition (and (isButtonHigh ?bh) (isButtonSensHigh ?h))
        :effect (off_buzzer ?oc)
    )
    
    (:action SwitchON_buzzer
        :parameters (?bl -button ?xc ?l -button_sensor)
        :precondition (and (isButtonLow ?bl) (isButtonSensLow ?l))
        :effect (on_buzzer ?xc)
    )
) 