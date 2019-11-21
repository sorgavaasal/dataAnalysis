import os
import sys
sys.path.insert(0, os.getcwd())
from all_generic import config

bulletin_settings = "bulletin-settings.yml"

settings = {}


def load_settings_yml(workspace):
    yaml_settings_file = workspace + '/' + bulletin_settings
    return config.load_settings_yaml(yaml_settings_file)


if __name__ == '__main__':
    workspace = os.getcwd()
    settings = load_settings_yml(workspace + '/resources')
    print(settings)
