import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from arch64 import main
    main()
elif bit == '32bit':
    from arch32 import main
    main()
