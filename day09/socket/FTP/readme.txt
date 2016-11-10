 各种LTE终端缺省的用户名和密码

LTE终端缺省的用户名和密码

1. 大亚CPE

webUI usr/pwd: admin/111111,或者root/root

telnet usr/pwd: root/root

输入sky123,就能进入到linux命令行

2. IDU

webUI usr/pwd: admin/admin

or superadmin/admin

串口登录：root/zmtel-sw2014  

MTx22e新发布的版本，通过串口登录时，需要用户名和密码

name：root

password: Si8a&2vV9
669080
ssh shell登录：admin/amdin

3.厦门优泰CPE

webUI:

telnet: admin/admin

4.巴林menatelecom版本

webUI:

administrator/m3nat3l3com

5.中兴版本CPE

webUI:

admin/pldt_zteWD600

ODU/Smart
engineer/1_m!%r0d87(x9rT:I0Qb
greenpacket、bwro!5ZwWCq_KyJ%4JIpXf
GP
admin/admin
operator、D1reC7V@Dm1n

ZTE-WD600 
admin/pldt_zteWD600 
ulterainstaller/uLTEra1n$t@ll3r 
homeultera/homeultera

IDU：
admin：NzYvOTg0,TEv/29uZmln
ODU：
admin：NzYvOTg0,TEv/29uZmln


京信
超级账号：
telecomadmin,nE7jA%5m
普通账号：
useradmin
admin

iperf –s –u –i1（开启服务器监听，UDP类型，1秒打印一次）
iperf –c （DAU地址）-u -i1 –b50M –t9999（客户端上行灌UDP包，带宽50M，一秒打印一次，持续9999秒）

中国移动TD-LTE：支持频段38、39、40

中国联通TD-LTE：支持频段40、41

中国电信TD-LTE：支持频段40、41

中国联通FDD-LTE：支持频段3

中国电信FDD-LTE：支持频段3

设置信号强度：
 touch /etc/noreboot;pkill ucid
 ps|grep -i ucid
uci show|grep -i rsrp
uci set sqns.radio.RSRP0=-105;uci set sqns.radio.RSRP1=-105;
 uci show|grep -i rsrp
uci show|grep -i band

929 root      1524 S    udhcpc -p /var/run/udhcpc-eth0.pid -s /lib/netifd/dhcp.script -f -t 0 -i eth0 -C
root@ZMWR2500:~# kill -17 929
root@ZMWR2500:~# kill -16 929
tcpdump -i pptp-vpn -w /tmp/voip_dns.pcap

chunjiesun
2wsx#edc

cbe "showmeas" 
cbe "showactive" 
cbe "showversion"

devlist-output debug

dmesg:查看系统消息

查看规则表：iptables -L -nv
iptables -nvL

ipconfig /flushdns//清空DNS缓存

at at!=showrequire

at at!=showsi

at at+cgact?//查APN起来没有的命令

at at+cgpaddr//sqn使用的命令

at at+cgcontrdp
at at+cgdcont?//标准的命令

ls| grep -i ***//查找东西

http://192.168.15.1/dev-info.asp

：http://docs.seleniumhq.org/download/
root@OpenWrt:~# /etc/init.d/zmfw0 restart

Loading zmtel MAC flt rules

cbe "activateTta enable=1"

-- Measurement ----------------------------------------------------------------------------------- date=3922978 --
| C | arfcn | pci | filtr, sample |     rsrp last/filt.     |      rsrq last/filt.    |      cinr last/filt.    |
-----------------------------------------------------------------------------------------------------------------
| P | 41140 | 220 | true , 34     | -96.00 /-96.09 /-96.00  | -8.50  /-8.41  /-8.50   | 11.10  /11.03  /11.10   |
| A | 41140 | 122 | true , 31     | -99.40 /-99.61 /-99.40  | -9.50  /-9.65  /-9.50   | 5.10   /4.82   /5.10    |
--(P:primSrv)(S:2ndSrv)(A:Intra)(R:Inter)------------------------------(rsrp:dBm)(cinr,rsrq:dB)(tMeas,dates:ms)--

getper

cbe "fsm"

编号	ICCID	卡号	PUK	PIN
1	8986031500021113720	18916806604	75855271	1234
2	8986031500021113721	18916835144	54138385	1234
3	8986031500021113722	18916396614	22722870	1234


8986031500021113722B S
中国电信
沈媛
开通日期：2015-12-1
上海48G包年卡，上海地区44G，全国漫游4G
ISDN：18916396614
PUK：22722870
服务密码：113722
正常
//查看ODU版本
apph
!showver

root@CPE:/proc# cat interrupts 

1、	进入/etc/dinc/目录，并编辑din.cfg文件内容，设置GP服务器IP地址: 123.51.170.31设置进去，然后重启下ODU；
2、	打开浏览器输入URL:
http://123.51.170.31:9000/index.html?page=device&device=0000001FFBA0ED7A  

vi /etc/init.d/done 

find / -name '*dinc*'


ps ww| grep dinc查看，
din --daemon --cfg_path=/etc/dinc/din.cfg
找服务器是三个
找到了是两个
找不到是一个

showsearchContext//查看dlarfcn,pci


一边通一边不通，可能是因为有一方的编码方式优先级不通。puma,pumu

写入SN的方法：
登陆到CPE后:
echo "SN=1234567890" > /tmp/sn
flash_raw  -H -w /tmp/sn
reboot

ifconfig eth0 up              #可以用于启动网卡
ifconfig eth0 down            #可以用于禁用网卡
ifconfig eth0 192.168.1.101   #可以给主机制定静态地址 


IP地址是网络间通信，物理地址是网络内部通信

dins需要配置端口镜像才可以使用！

写硬件的版本：
echo "SN=ZMTELA8935203D0E0" > /tmp/sn

echo "HW_VER=1.0" > /tmp/sn
mtd erase /dev/mtd4
flash_raw  -H -w /tmp/sn
reboot


touch /etc/tr069_lan
touch tr069_lan
 tr069 -d /etc/trconf/&
 killall tr069

串口设置：
E:\LOG\ACPU\%S-%M-%D-%h-%m.log
%D-%M
%D-%M
%M-%D_%h-%m-%s

\\172.16.34.4\Volume_1\Public\Test\测试部\8-技术文档\CN2917中兴微


route add 169.254.0.1 mask 255.255.255.0 192.168.1.1

atcmd /dev/ttyACM0 115200 AT+CPIN? 