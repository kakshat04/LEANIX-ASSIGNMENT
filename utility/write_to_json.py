"""
“” for 0 .. 30 days
“low” for 31 .. 60 days
“medium” for more than 60 days
"""
import json


class WriteJson:
    def write_security_warn_level(self):
        with open(r'F:\LeanIX_Assessment\Assessment\assessment.json', 'r') as f:
            playlist = json.load(f)

            for i in range(len(playlist["content"])):
                if "AmazonIamUser" in playlist["content"][i]['type']:
                    age = playlist["content"][i]["data"]["Properties"]["AccessKeyAge"].split(" ")[0]
                    if 0 <= int(age) <= 30:
                        playlist["content"][i]["data"]["Properties"]["violationLevelSecurity"] = ""
                        print(f"Age {age}, within range 0-30 found, updating 'violationLevelSecurity' with ''")
                    elif 31 <= int(age) <= 60:
                        playlist["content"][i]["data"]["Properties"]["violationLevelSecurity"] = "low"
                        print(f"Age {age}, within range 31-60 found, updating 'violationLevelSecurity' with 'low'")
                    elif int(age) > 60:
                        playlist["content"][i]["data"]["Properties"]["violationLevelSecurity"] = "medium"
                        print(f"Age {age}, >60 found, updating 'violationLevelSecurity' with 'medium'")

        with open(r'F:\LeanIX_Assessment\Assessment\assessment.json', 'w') as f1:
            json.dump(playlist, f1)
        return playlist


if __name__ == '__main__':
    wj_obj = WriteJson()
    wj_obj.write_security_warn_level()
