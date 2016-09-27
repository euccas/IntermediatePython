# Reference: https://docs.python.org/3/library/json.html

import json

def jsonify(func):
    jsoninfo = {}

    def new_func():
        jsoninfo = json.dumps(func())
        return jsoninfo

    return new_func

@jsonify
def get_thing():
    return {'trey': "red", 'dinae': "purple"}

if __name__ == "__main__":
    print(get_thing())


