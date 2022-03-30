from service import automatic_service as asv


'''
Pre-exquisite:
- 22:00 -> 06:00 :
    - Bedroom ac & music turned off

- 08:00 -> 11:00 :
    - All music is played

- if people exists:
    - music on
    
- if too dark and people exists:
    - lights on
    
- if too hot and people exists:
    - AC on
    
------------------------------------------------------------
Sensor simulation details:
- 22:00 -> 08:00 : No one exists
    - Nothing is operated

- 08:00 -> 22:00 : someone exists
    - All music is played
    - 08:00 -> 17:00: AC turned on due to hot
    - 08:00 -> 17:00: Light turned off due to brightness
------------------------------------------------------------
'''

def simulator(hour):
    asv.update_sensor('BEDROOM', 'temperature', 7, 20, '50', '25', hour)
    asv.update_sensor('BEDROOM', 'brightness', 7, 20, '100', '50', hour)
    asv.update_sensor('BEDROOM', 'people', 7, 20, '1', '0', hour)

    asv.update_sensor('BATHROOM', 'brightness', 7, 17, '100', '50', hour)
    asv.update_sensor('BATHROOM', 'people', 7, 20, '1', '0', hour)

    asv.update_sensor('LIVING_ROOM', 'temperature', 7, 17, '50', '25', hour)
    asv.update_sensor('LIVING_ROOM', 'brightness', 7, 17, '100', '50', hour)
    asv.update_sensor('LIVING_ROOM', 'people', 7, 20, '1', '0', hour)

    asv.update_sensor('KITCHEN', 'temperature', 7, 17, '50', '25', hour)
    asv.update_sensor('KITCHEN', 'brightness', 7, 17, '100', '50', hour)
    asv.update_sensor('KITCHEN', 'people', 7, 20, '1', '0', hour)

