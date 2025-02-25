import re

txt = "30.168.10.1000"

regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

result = re.search(regex,txt)

print(result)

if result:
    print(f"Valid IPv4 Address: {result.group()}")
else:
    print("Invalid IPv4 Address")