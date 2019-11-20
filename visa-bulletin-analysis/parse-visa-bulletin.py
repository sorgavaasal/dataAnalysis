import os

bulletin_settings = "bulletin-settings.yml"

def load_settings_yml (workspace) :
    print ('debug message for loading ')
    yaml_settings_file = workspace + '/' + bulletin_settings
    print (yaml_settings_file)

if __name__ == '__main__':
    workspace = os.getcwd()
    print ('current-working-directory', workspace)
    load_settings_yml(workspace)