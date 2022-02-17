import yaml
with open(r'C:\codeSpace\PythonCodeTests\test_yaml\yaml_sample.yml', 'r') as f:
    yaml_data = f.read()
    json_data = yaml.safe_load(yaml_data)
    print(json_data)


with open(r'C:\codeSpace\PythonCodeTests\test_yaml\logs\yaml_sample.yml', 'w') as f:
    yaml.safe_dump(json_data, f)