import os
import datetime

def create_file(file_path, content=""):
    with open(file_path, 'w') as file:
        file.write(content)

def create_directory_structure(package_name):
    # Define the directory structure
    directories = [
        os.path.join(package_name, 'config'),
        os.path.join(package_name, 'launch'),
        os.path.join(package_name, 'src')
    ]

    files_with_content = {
        os.path.join(package_name, 'config', f'{package_name}.param.yaml'): generate_param_yaml_content(),
        os.path.join(package_name, 'launch', f'{package_name}.launch.xml'): generate_launch_xml_content(package_name),
        os.path.join(package_name, 'src', f'{package_name}.cpp'): generate_cpp_content(package_name),
        os.path.join(package_name, 'src', f'{package_name}.hpp'): generate_hpp_content(package_name),
        os.path.join(package_name, 'CMakeLists.txt'): generate_cmakelists_txt_content(package_name),
        os.path.join(package_name, 'package.xml'): generate_package_xml_content(package_name),
        os.path.join(package_name, 'README.md'): generate_readme_md_content(package_name)
    }

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create files
    for file_path, content in files_with_content.items():
        create_file(file_path, content)

def generate_package_xml_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'package.xml')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    return template_content.replace('{{package_name}}', package_name)

def camel_case(s):
    components = s.split('_')
    return ''.join(x.title() for x in components)

def upper_case(s):
    return s.upper()

def generate_cmakelists_txt_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'CMakeLists.txt')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    camel_case_name = camel_case(package_name)
    content = template_content.replace('{{package_name}}', package_name)
    content = content.replace('{{PackageName}}', camel_case_name)
    return content

def generate_param_yaml_content():
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'param.yaml')
    with open(template_path, 'r') as file:
        return file.read()

def generate_launch_xml_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'launch.xml')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    return template_content.replace('{{package_name}}', package_name)

def generate_cpp_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'package_name.cpp')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    year = datetime.datetime.now().year
    camel_case_name = camel_case(package_name)
    content = template_content.replace('{{year}}', str(year))
    content = content.replace('{{package_name}}', package_name)
    content = content.replace('{{PackageName}}', camel_case_name)
    return content

def generate_hpp_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'package_name.hpp')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    year = datetime.datetime.now().year
    camel_case_name = camel_case(package_name)
    upper_case_name = upper_case(package_name)
    content = template_content.replace('{{year}}', str(year))
    content = content.replace('{{package_name}}', package_name)
    content = content.replace('{{PackageName}}', camel_case_name)
    content = content.replace('{{PACKAGE_NAME}}', upper_case_name)
    return content

def generate_readme_md_content(package_name):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'README.md')
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    formatted_name = ' '.join(word.capitalize() for word in package_name.split('_'))
    return template_content.replace('{{Package Name}}', formatted_name)
