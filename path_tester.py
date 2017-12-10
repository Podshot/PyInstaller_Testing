import sys
import json
import os

def find_bundle_dir():
    if getattr(sys, 'frozen', False):
        return "{} ({})".format(sys._MEIPASS, 'frozen')
    else:
        return "{} ({})".format(os.path.dirname(os.path.abspath(__file__)), 'not frozen')

def run():
    print "Frozen: {}".format(getattr(sys, 'frozen', False))
    print "Bundle Directory: {}".format(find_bundle_dir())
    print "System Arguments: {}".format(sys.argv)
    print "Executable: {}".format(sys.executable)
    print "Working Directory: {}".format(os.getcwdu())

    bundle_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    fp = open(os.path.join(bundle_dir, 'test.json'), 'rb')
    data1 = json.load(fp)
    fp.close()

    fp = open(os.path.join(bundle_dir, 'directory', 'test.json'))
    data2 = json.load(fp)
    fp.close()

    print "Value (base file): {}".format(data1['test'])
    print "Value (directory file): {}".format(data2['test'])



if __name__ == '__main__':
    run()
