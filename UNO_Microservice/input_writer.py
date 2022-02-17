import json

input_dict = {}
input_dict["calorie_max"] = 500
input_dict["calorie_min"] = 200
input_dict["cuisine"] = 'indian'
input_dict["diet_type"] = 'low-sodium'

output = json.dumps(input_dict)
jsonWrite = open("recipe_input.json","w")
jsonWrite.write(output)
jsonWrite.close()