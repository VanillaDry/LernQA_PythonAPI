import json
string_as_json_format = '{"answer": "Hellow, User"}'
obj = json.loads(string_as_json_format)
print(obj['answer2'])