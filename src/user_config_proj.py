def add_setting(dictionary, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()
    result = ""
    if dictionary.get(key):
        result += f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary.update({key:value})
        result += f"Setting '{key}' added with value '{value}' successfully!"
    return result

def update_setting(dictionary, key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()
    result = ""
    if dictionary.get(key):
        dictionary.update({key:value})
        result += f"Setting '{key}' updated to '{value}' successfully!"
    else:
        result += f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    return result

def delete_setting(dictionary, key):
    key = key.lower()
    result = ""
    if dictionary.get(key):
        dictionary.pop(key)
        result += f"Setting '{key}' deleted successfully!"
    else:
        result += "Setting not found!"
    return result

def view_settings(dictionary):
    result = ""
    if not dictionary:
        result += "No settings available."
    else:
        result += "Current User Settings:\n"
        for key,value in dictionary.items():
            result += f"{key.capitalize()}: {value}\n"
    return result

if __name__ == "__main__":
    # test run
    test_settings = dict()
    add_setting(test_settings, ('THEME', 'dark')])
    add_setting(test_settings, ('volume', 'high'))
    print(view_settings(test_settings))