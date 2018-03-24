import pyqrcode,png,io

#create basic QR with message
url = pyqrcode.create('Helloooo'+'hi')
url.svg('uca-url.svg', scale=8)

#print in terminal
print(url.terminal(quiet_zone=1))
print(url.terminal())
print(url.terminal(module_color='red', background='yellow'))
print(url.terminal(module_color=5, background=123, quiet_zone=1))

#create svg
url.svg('uca.svg', scale=4, background="white", module_color="black")

#create png
url.png('uca-colors.png',scale=6,module_color=[0, 0, 0, 128],background=[0xff, 0xff, 0xcc])

