import os
from all-generic import config

bulletin_settings = "bulletin-settings.yml"

def load_settings_yml (workspace) :
    print ('debug message for loading ')
    yaml_settings_file = workspace + '/' + bulletin_settings
    print (yaml_settings_file)
    config = config.load_settings_yml(yaml_settings_file)
    print (config)

if __name__ == '__main__':
    workspace = os.getcwd()
    print ('current-working-directory', workspace)
    load_settings_yml(workspace)