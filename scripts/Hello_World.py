import optparse

parser = optparse.OptionParser()
parser.add_option('-u', action="store", default="Enter username")
parser.add_option('-p', action="store", default="Enter password")
parser.add_option('-d', action="store", default="directory")
parser.add_option('-f', action="store", default="function")

options, args = parser.parse_args()

print(options.u)
print(options.p)
print(options.d)
print(options.f)
