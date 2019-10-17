import yaml
import os

#read yaml file with urls coming from the config.yml

class Utilities:
    def __init__(self):
        with open('config.yml','r') as fileVals:
            ymldoc = yaml.load(fileVals, Loader=yaml.FullLoader)
            os.environ['URL'] = ymldoc['temperature_reading']['url']
#             if we are running it locally, we will pick the browser value from config.yml
#              using docker we are setting it in the environment variable in docker compose
            if os.getenv('env') == "local" :
                os.environ['BROWSER'] = ymldoc['temperature_reading']['browser']



