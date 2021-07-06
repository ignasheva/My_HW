class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []

    def decorator(key, value):
        def keyword_filter_func(item):
            return key in item and item[key] == value

        return keyword_filter_func

    for key, value in keywords.items():
        filter_funcs.append(decorator(key, value))

    return Filter(filter_funcs)
