import re

txt = "192.168.110.1/24"

pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\/(\d{1,2})$"

match = re.match(pattern,txt)

print(match.group(1))
print(match.group(2))

if match:
    ip = match.group(1)
    cidr = int(match.group(2))
    octats = ip.split('.')

    if all(0 <= int(oct) <= 255 for oct in octats) and 0 <= cidr <= 32:
        print(f"{txt} is a valid IP address with CIDR")
    else:
        print(f"{txt} is Not a valid IP address or CIDR")
else:
    print(f"{txt} is Not a valid IP address or CIDR")