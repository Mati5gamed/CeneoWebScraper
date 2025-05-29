def extract(ancestor,selector= None, atribute = None, many = False):
    if selector:
        if many:
            if atribute:
                return [item[atribute].strip() for item in ancestor.select(selector)]
            return [item.text.strip() for item in ancestor.select(selector)]
        if atribute:
            try:
                return ancestor.select_one(selector)[atribute].strip()
            except TypeError: 
                return None
        try:

            return ancestor.select_one(selector).text.strip()
        except AttributeError:
            return None
    if atribute:
#        try:
        return ancestor[atribute]
        # except TypeError:
        #     return None
    return ancestor.text.strip()