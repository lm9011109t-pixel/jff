from config import *

def get_auto_passlist(level):
    if level == "1":
        return ["firstlast", "first last","first", "first112233", "first1234567", "first123456789", "first123456", "first12345678", "first1234", "first123"]
    elif level == "2":
        return ["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"]
    elif level == "3":
        return ["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"]
    elif level == "4":
        return ["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"]
    else:
        return ["firstlast","first@","first last@@","firstlast12345","firstlast1234","firstlast@@","firstlast@","first@@"]

def generate_password(pw, fn, ln, names):
    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
    return pas