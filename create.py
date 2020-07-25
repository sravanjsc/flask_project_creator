#!/usr/bin/python3

# Script to generate directory Structure for Flask Project

import argparse
import os


# Create ArgumentParser class object
parser = argparse.ArgumentParser(description="This script generates flask project files ")

# Add argument with the name file_name and type as string
parser.add_argument("name", type = str, help = "Please enter the project name")

# Retrieve the argument passed to the program
args = parser.parse_args()


# Take the argument value here and allocate to result
project_name = args.name # result will be the project name



def create_templates(template_path):
    template_index_file = open(os.path.join(template_path,'index.html'), 'w')
    template_index_file.close()


def create_static(static_path):
    static_style_file = open(os.path.join(static_path,'style.css'), 'w')
    static_style_file.close()


# Create project
def create_project(project_path, project_name):
    os.mkdir(project_path)
    root_file = "app.py"
    root_file_create = open(os.path.join(project_path, root_file), 'w')
    root_file_create.close()
    project_components = os.path.join(project_path, project_name)
    os.mkdir(project_components)
    template_path = os.path.join(project_components, 'templates')
    os.mkdir(template_path)
    static_path = os.path.join(project_components, 'static')
    os.mkdir(static_path)
    init_file = open(os.path.join(project_components, '__init__.py'), 'w')
    init_file.close()
    model_file = open(os.path.join(project_components, 'models.py'), 'w')
    model_file.close()
    form_file = open(os.path.join(project_components, 'forms.py'), 'w')
    form_file.close()
    routes_file = open(os.path.join(project_components, 'routes.py'), 'w')
    routes_file.close()
    create_templates(template_path)
    create_static(static_path)
    print("Project created Successfully!")
    
if len(project_name) < 2:
    print("Please enter a proper project name")
    
else:
    DIR_PATH = os.getcwd()
    set_path = os.path.join(DIR_PATH, project_name)
    if os.path.isdir(set_path):
        print("A directoty same as your project name already exist. Please enter another name")
    else:
        create_project(set_path, project_name)


