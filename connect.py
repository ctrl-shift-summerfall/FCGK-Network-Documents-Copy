# External libraries:
import os


def connect_network():

    # Address and user settings:
    NETWORK_ADDRESS: str = r'\\KindergartenNAS\HC-Kindergarden'
    NETWORK_DRIVE_ASSIGNED: str = 'N:'
    USER_REQUIRED: bool = False
    USER_NAME: str = 'teacher'
    USER_PASSWORD: str = 'hc@laoshi123'
    
    # Establishing new connection:
    command_prompt: str = f'net use {NETWORK_DRIVE_ASSIGNED} {NETWORK_ADDRESS} /p:yes '
    if USER_REQUIRED: command_prompt += '/user:{USER_NAME} {USER_PASSWORD}'
    os.system(command_prompt)
