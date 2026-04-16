import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parser_data = json.loads(json_data)

print(type(parser_data))