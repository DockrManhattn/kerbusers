# Kerbusers
This repo hosts a wrapper for kerbrute to run basic scans for usernames.

# Installation
```bash
python3 setup.py
```

# Usage
```bash
kerbusers -d $DOMAIN -dc-ip $IP
```
# Example
```bash
┌─[✗]─[kali@parrot]─[~/kerbusers]
└──╼ $kerbusers -d retro2.vl -dc-ip 10.10.89.161

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 01/12/25 - Ronnie Flathers @ropnop

2025/01/12 23:29:04 >  Using KDC(s):
2025/01/12 23:29:04 >  	10.10.89.161:88

2025/01/12 23:29:04 >  [+] VALID USERNAME:	 ADMIN@retro2.vl
2025/01/12 23:29:04 >  [+] VALID USERNAME:	 ADMINISTRATOR@retro2.vl
2025/01/12 23:29:04 >  [+] VALID USERNAME:	 Administrator@retro2.vl
2025/01/12 23:29:04 >  [+] VALID USERNAME:	 Admin@retro2.vl
2025/01/12 23:29:05 >  [+] VALID USERNAME:	 GUEST@retro2.vl
2025/01/12 23:29:05 >  [+] VALID USERNAME:	 Guest@retro2.vl
2025/01/12 23:29:05 >  [+] VALID USERNAME:	 admin@retro2.vl
2025/01/12 23:29:05 >  [+] VALID USERNAME:	 administrator@retro2.vl
2025/01/12 23:29:05 >  [+] VALID USERNAME:	 guest@retro2.vl
2025/01/12 23:30:00 >  [+] VALID USERNAME:	 julie.martin@retro2.vl
2025/01/12 23:30:53 >  [+] VALID USERNAME:	 alex.scott@retro2.vl
2025/01/12 23:32:00 >  [+] VALID USERNAME:	 laura.davies@retro2.vl
2025/01/12 23:32:43 >  [+] VALID USERNAME:	 clare.smith@retro2.vl
2025/01/12 23:34:52 >  [+] VALID USERNAME:	 emily.price@retro2.vl
2025/01/12 23:40:55 >  [+] VALID USERNAME:	 leah.robinson@retro2.vl
2025/01/12 23:41:04 >  [+] VALID USERNAME:	 caroline.james@retro2.vl
2025/01/12 23:43:35 >  [+] VALID USERNAME:	 mandy.davies@retro2.vl
2025/01/12 23:44:06 >  [+] VALID USERNAME:	 michelle.bird@retro2.vl
2025/01/12 23:45:25 >  [+] VALID USERNAME:	 lindsey.harrison@retro2.vl
2025/01/12 23:51:03 >  Done! Tested 962936 usernames (19 valid) in 1318.585 seconds
```
