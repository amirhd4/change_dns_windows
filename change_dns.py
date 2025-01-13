import os
os.system('netsh interface ip set dns name="Ethernet" static 78.157.42.100')
os.system('netsh interface ip add dns name="Ethernet"  78.157.42.101 index=2')
