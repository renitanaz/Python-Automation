import json
dicttest='{"k1":"first","k2":"second"}'

json_result=json.loads(dicttest)
print(json_result.values())