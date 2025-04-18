# zowsup

zowsup is a python whatsapp-protocol project base on [yowsup](https://github.com/tgalal/yowsup/).

Since the original yowsup project has not been maintained for a long time, we forked yowsup and some associated projects(axolotl, consonance) and intergrated into an All-In-One Project and keep updating with latest version of Whatsapp.

```
- ZOWSUP VERSION : 0.5.0

- UPDATE TIME : 2025-04-10

- WHATSAPP VERSION : 
    2.25.10.71(Android) 
    2.25.11.4(SMB Android) 
    2.25.5.74(iOS) 
    2.25.5.74(SMB iOS) 

```

## What's New 
 * Latest version(6.3) of noise-protocol and token-dictionary
 * Multi-Environment support (android,smb_android,ios,smb_ios)
 * Multi-Device protocol support
 * Display a QR to Login as a companion device 
 * 6-parts account support (import / export )
 * Proxy support
 * Threading command architecture 
 * Bubbling up all the config variables to the top layer ( app and conf folder)
 * Mass of WA-protocol updates
 
## Subsequent update promise
 * Critical protocol update
 * Version update with latest WhatsApp 
 

## Quick start for the project

 * Installation 

```
 pip install -r requirements.txt

```
 * Basic configuration

```
copy ./conf/config.conf.example to ./conf/config.conf and modify variables in config.conf according to your system

ACCOUNT_PATH=/data/account/               #location you store the account data
DOWNLOAD_PATH=/data/tmp/                  #download path
UPLOAD_PATH=/data/tmp/                    #upload path
LOG_PATH=/data/log/                       #log path
DEFAULT_ENV=android                       #default environment

```
 * Import account from 5-parts-account-data

```
 python script/import5.py [5-parts-account-data] --env android             # env : android/smb_android/ios/smb_ios is available without rc2key

```
 * Import account from 6-parts-account-data

```
 python script/import6.py [6-parts-account-data] --env android             # env : android/smb_android/ios/smb_ios is available

```

 * Export accounts to 6-parts-account-data
 
```
 python script/export6.py [account-number]

```


 * Run

```
 python script/main.py [account-number] --env android                        # env : android/smb_android/ios/smb_ios is available

```

* Register as companion 

```
 python script/regwithscan.py 

```

 * Basic commands

```
main.py [account-number] [command] [commandParams]

[command]           |   [description]
-----------------------------------------------------------------------
getavatar           |   get account avatar
getgroupinvite      |   get the invite code of a group
groupadd            |   add member to group
groupapprove        |   approve participants to join the group
groupdemote         |   demote group member (from admin)
groupinfo           |   show the group info
grouppromote        |   promote group member (to admin)
groupremove         |   remove member from group
init                |   initialize (first login)
joingroup           |   join group with a invite code
leavegroup          |   leave group
makegroup           |   make group with members
sendmedia           |   send media message to  peer
send                |   send message to peer
set2fa              |   set account 2fa
setavatar           |   set account avatar
setgroupicon        |   set icon for group
setselfname         |   set account name
sync                |   sync contacts
-----------------------------------------------------------------------
```


 * Proxy 

```
 python script/main.py [account-number] --proxy "host:port:username:password"  

 dynamic [location] and [session_id] replacin the proxy string is supported 

```



