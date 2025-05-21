
고정 ip 할당 이유: 모든 기기에서 동일한 "raspberrypi"라는 이름으로 인해 ip로 본인의 기기에 접속하고자 함

요구조건
-  개인 USB에 아래 3개의 파일 다운로드
__1.hanback.cfg
2.wlan_static
3.wpa_supplicant__

<파일 위치>
```
1.공유드라이브\RaspberryPi\tools\IP_Allocation_Program\file/hanback.cfg
2.공유드라이브\RaspberryPi\tools\IP_Allocation_Program\file/wlan_static
3.공유드라이브\RaspberryPi\tools\IP_Allocation_Program\file/wpa_supplicant
```

__1.hanback.cfg__
![[Pasted image 20250325180559.png]]

```python
dhcp = no #동적 할당을 할것인지 물어보는 부분 yes -> no로 변경
interface = wlan0 #eth0 -> wlan0으로 변경 #wifi 사용한다는 뜻 
```

__2.wlan_static__
![[Pasted image 20250325180625.png]]
```python
auto lo
iface lo inet loopback

auto wlan0
allow-hotplug wlan0
iface wlan0 inet static
address 192.168.68.110 //사용할 ip 주소는 모두 달라야 함
netmask 255.255.255.0
gateway 192.168.68.1 //게이트 웨이는 iptime의 경우 기본적으로 192.168.0.1이나 공유기 마다 다름
                     //우리집의 경우 공유기 주소가 192.168.68.1임
wpa-ssid "shim_home" //사용할 wifi이름
#wpa-psk "shim7070" //사용할 wifi 비밀번호

wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

__3.wpa_supplicant__
![[Pasted image 20250325180700.png]]

```python
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="shim_home" //이전에 작성했던 wlan_static과 동일한 wifi 이름
    psk="shim7070" //이전에 작성했던 wlan_static과 동일한 비밀번호
    proto=RSN
    key_mgmt=WPA-PSK
    pairwise=CCMP
    auth_alg=OPEN
}
```

![[Pasted image 20250325180727.png]]

![[Pasted image 20250325180752.png]]

->USB를 라즈베리파이에 꼽고 고정 ip가 제대로 설정 되었으면 
__ipaddr.txt__ 이 생성됨

![[Pasted image 20250325204853.png]]

#192.168.68.250은 내가 고정 ip로 설정한 기록이 남은거임
