#in this sector you will fiend all fonction that we will use it in our code
#mac changer
import subprocess
import optparse
import re
import time
def mc(x,y):
    subprocess.call(["ifconfig", x, 'down'])
    time.sleep(1)
    subprocess.call(["ifconfig", x, 'hw ether', y])
    time.sleep(1)
    subprocess.call(["ifconfig", x, 'down'])



def data():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='chose your interface ')
    parser.add_option('-m','--mac',dest ='mac',help='put you new mac adress')
    (x,y)  = parser.parse_args()
    if not x.interface:
        print('there is no interface for more info use --help or -h')
    elif not x.mac:
        print('there is no mac adress for more info use --help or -h')


    return x

def get_mac0(x):
    a = str(subprocess.check_output(["ifconfig", x]))  #x = interface
    b = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",a)

    if b:
        return b.group(0)
    else:
        prunt("[-] there is no mac for this interface for more info use --help,-h")


