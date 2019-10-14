from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
   symbols = string.ascii_letters + string.digits + " "*10 # string.punctuation +
   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", home="", work="", mobile="", phone2="", address="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), home=random_string("home", 20), work=random_string("work", 20), mobile=random_string("mobile", 20), phone2=random_string("phone2", 20), address=random_string("address", 20), email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))