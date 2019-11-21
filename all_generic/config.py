import yaml


def load_settings_yaml(filename):
    with open(filename) as setting_yaml:
        config = yaml.load(setting_yaml, Loader=yaml.FullLoader)
    return config