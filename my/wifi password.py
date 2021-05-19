import subprocess
import re

command_output=subprocess.run(["netsh","wlan","show","profiles"],capture_output=True).stdout.decode()
profile_names=(re.findall("All user prrofiles.....:(.*)\r",command_output))
wifi_list=[]
if len(profile_names)!=0:
    for name in profile_names:
        wifi_pofile=dict()
        profile_info=subprocess.run(["netsh","wlan","show","profile",name],capture_output=True).stdout.decode()
        if re.search("security key      :absent",profile_info):
            continue
        else:
            wifi_pofile=[]=name
            profile_info_pass=subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()
            password=re.search("key content     (.*)\r",profile_info_pass)
            if password==None:
                wifi_pofile["password"]=None
            else:
                wifi_pofile["password"]=password[1]
            wifi_list.append(wifi_pofile)
for x in range(len(wifi_list)):
    print(wifi_list[x])