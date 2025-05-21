
```python
$ ipconfig

Windows IP Configuration


Ethernet adapter ▒̴▒▒▒:

   Media State . . . . . . . . . . . : Media disconnected 
	'''현재는 유선 네트워크 어댑터가 사용되지 않음을 뜻함'''

   Connection-specific DNS Suffix  . : 
	'''특정 네트워크 도메인이 설정되지 않음'''

Wireless LAN adapter ▒▒▒▒ ▒▒▒▒ ▒▒▒▒* 1:
'''현재 사용되지 않는 무선 네트워크 인터페이스'''

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter ▒▒▒▒ ▒▒▒▒ ▒▒▒▒* 10: 
'''현재 사용되지 않는 무선 네트워크 인터페이스'''

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter VMware Network Adapter VMnet1: 
'''VMware 가상 네트워크 어댑터(가상 머신 관련)'''

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::c9fa:37e7:a06f:2d5f%10
   IPv4 Address. . . . . . . . . . . : 192.168.183.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::37d4:156c:7462:4f85%21
   IPv4 Address. . . . . . . . . . . : 192.168.33.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

'''
VMware Network Adapter VMnet1 & VMnet8**: VMware에서 가상 머신을 실행할 때 생성하는 가상 네트워크 어댑터.
    
    1.VMnet1 (Host-only)**: 가상 머신과 호스트(내 PC)만 연결되는 네트워크.
        
    2. VMnet8 (NAT)**: 가상 머신이 내 PC를 통해 인터넷을 사용할 수 있도록 하는 네트워크.
        
IPv4 주소 (`192.168.183.1`, `192.168.33.1`)**: 이 주소들은 가상 머신과의 통신을 위한 내부 IP 주소임.
    
기본 게이트웨이 없음: 이 네트워크 어댑터는 외부 인터넷과 직접 연결되지 않음.
'''

Wireless LAN adapter Wi-Fi:
'''실제 wifi 네트워크 (현재 사용 중인 네트워크)'''
   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::390f:b0e9:d631:c8a3%8
   IPv4 Address. . . . . . . . . . . : 192.168.68.107
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::1e3b:f3ff:feb4:a514%8
                                       192.168.68.1
'''
- 현재 사용 중인 **Wi-Fi 네트워크** 정보를 나타냄.
    
- **IPv4 주소: `192.168.68.107`** → 내 PC가 공유기로부터 할당받은 내부 IP 주소.
- **Subnet Mask: `255.255.255.0`** → 같은 네트워크 대역은 `192.168.68.x`까지 가능.
지금 이 경우의 네트워크 범위는 192.168.68.0 ~ 192.168.68.255입니다.

- **기본 게이트웨이: `192.168.68.1`** → 공유기의 내부 IP 주소.
    
    - 공유기 설정 페이지 접속하려면 브라우저에서 `http://192.168.68.1` 입력하면 됨.
'''

Ethernet adapter ▒̴▒▒▒ 2:
'''기타 유선 LAN 어댑터 (사용 안하는 중)'''
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Bluetooth ▒▒Ʈ▒▒ũ ▒▒▒▒:
'''Bluetooth 네트워크 어댑터'''
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter vEthernet (WSL (Hyper-V firewall)):
'''WSL (Windows Subsystem for Linux) 관련 가상 네트워크'''
   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::83ba:9332:d52f:4ca9%48
   IPv4 Address. . . . . . . . . . . : 192.168.240.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
'''
- **WSL2 (Windows Subsystem for Linux)**에서 사용하는 가상 네트워크 어댑터.
    
- **IPv4 주소: `192.168.240.1`** → WSL 환경 내에서 네트워크 통신을 위한 내부 IP.
    
- **기본 게이트웨이 없음** → WSL이 호스트 네트워크를 통해 인터넷에 연결됨.
'''
```

