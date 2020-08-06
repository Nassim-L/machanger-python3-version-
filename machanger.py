import data
print("""
machanger : v0.0.1
created by : Nassim L
github :
python version : 3.8 

""")

x = data.data()
mac0 = data.get_mac0(x.interface)
print('Current mac:', mac0)
data.mc(x.interface,x.mac)
mac1 = data.get_mac0(x.interface)
print('current new mac:', mac1)









