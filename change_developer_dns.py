import os
os.system('netsh interface ip set dns name="Ethernet" static 10.202.10.202')
os.system('netsh interface ip add dns name="Ethernet"  10.202.10.102 index=2')
