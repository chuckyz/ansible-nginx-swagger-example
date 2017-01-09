import re
def regex_replace(s, find, replace):
    return re.sub(find, replace, s)

class FilterModule(object):

    def filters(self):
        return {
            'regex_replace': regex_replace
        }
