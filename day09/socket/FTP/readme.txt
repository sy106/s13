 ����LTE�ն�ȱʡ���û���������

LTE�ն�ȱʡ���û���������

1. ����CPE

webUI usr/pwd: admin/111111,����root/root

telnet usr/pwd: root/root

����sky123,���ܽ��뵽linux������

2. IDU

webUI usr/pwd: admin/admin

or superadmin/admin

���ڵ�¼��root/zmtel-sw2014  

MTx22e�·����İ汾��ͨ�����ڵ�¼ʱ����Ҫ�û���������

name��root

password: Si8a&2vV9
669080
ssh shell��¼��admin/amdin

3.������̩CPE

webUI:

telnet: admin/admin

4.����menatelecom�汾

webUI:

administrator/m3nat3l3com

5.���˰汾CPE

webUI:

admin/pldt_zteWD600

ODU/Smart
engineer/1_m!%r0d87(x9rT:I0Qb
greenpacket��bwro!5ZwWCq_KyJ%4JIpXf
GP
admin/admin
operator��D1reC7V@Dm1n

ZTE-WD600 
admin/pldt_zteWD600 
ulterainstaller/uLTEra1n$t@ll3r 
homeultera/homeultera

IDU��
admin��NzYvOTg0,TEv/29uZmln
ODU��
admin��NzYvOTg0,TEv/29uZmln


����
�����˺ţ�
telecomadmin,nE7jA%5m
��ͨ�˺ţ�
useradmin
admin

iperf �Cs �Cu �Ci1������������������UDP���ͣ�1���ӡһ�Σ�
iperf �Cc ��DAU��ַ��-u -i1 �Cb50M �Ct9999���ͻ������й�UDP��������50M��һ���ӡһ�Σ�����9999�룩

�й��ƶ�TD-LTE��֧��Ƶ��38��39��40

�й���ͨTD-LTE��֧��Ƶ��40��41

�й�����TD-LTE��֧��Ƶ��40��41

�й���ͨFDD-LTE��֧��Ƶ��3

�й�����FDD-LTE��֧��Ƶ��3

�����ź�ǿ�ȣ�
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

dmesg:�鿴ϵͳ��Ϣ

�鿴�����iptables -L -nv
iptables -nvL

ipconfig /flushdns//���DNS����

at at!=showrequire

at at!=showsi

at at+cgact?//��APN����û�е�����

at at+cgpaddr//sqnʹ�õ�����

at at+cgcontrdp
at at+cgdcont?//��׼������

ls| grep -i ***//���Ҷ���

http://192.168.15.1/dev-info.asp

��http://docs.seleniumhq.org/download/
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

���	ICCID	����	PUK	PIN
1	8986031500021113720	18916806604	75855271	1234
2	8986031500021113721	18916835144	54138385	1234
3	8986031500021113722	18916396614	22722870	1234


8986031500021113722B S
�й�����
����
��ͨ���ڣ�2015-12-1
�Ϻ�48G���꿨���Ϻ�����44G��ȫ������4G
ISDN��18916396614
PUK��22722870
�������룺113722
����
//�鿴ODU�汾
apph
!showver

root@CPE:/proc# cat interrupts 

1��	����/etc/dinc/Ŀ¼�����༭din.cfg�ļ����ݣ�����GP������IP��ַ: 123.51.170.31���ý�ȥ��Ȼ��������ODU��
2��	�����������URL:
http://123.51.170.31:9000/index.html?page=device&device=0000001FFBA0ED7A  

vi /etc/init.d/done 

find / -name '*dinc*'


ps ww| grep dinc�鿴��
din --daemon --cfg_path=/etc/dinc/din.cfg
�ҷ�����������
�ҵ���������
�Ҳ�����һ��

showsearchContext//�鿴dlarfcn,pci


һ��ͨһ�߲�ͨ����������Ϊ��һ���ı��뷽ʽ���ȼ���ͨ��puma,pumu

д��SN�ķ�����
��½��CPE��:
echo "SN=1234567890" > /tmp/sn
flash_raw  -H -w /tmp/sn
reboot

ifconfig eth0 up              #����������������
ifconfig eth0 down            #�������ڽ�������
ifconfig eth0 192.168.1.101   #���Ը������ƶ���̬��ַ 


IP��ַ�������ͨ�ţ������ַ�������ڲ�ͨ��

dins��Ҫ���ö˿ھ���ſ���ʹ�ã�

дӲ���İ汾��
echo "SN=ZMTELA8935203D0E0" > /tmp/sn

echo "HW_VER=1.0" > /tmp/sn
mtd erase /dev/mtd4
flash_raw  -H -w /tmp/sn
reboot


touch /etc/tr069_lan
touch tr069_lan
 tr069 -d /etc/trconf/&
 killall tr069

�������ã�
E:\LOG\ACPU\%S-%M-%D-%h-%m.log
%D-%M
%D-%M
%M-%D_%h-%m-%s

\\172.16.34.4\Volume_1\Public\Test\���Բ�\8-�����ĵ�\CN2917����΢


route add 169.254.0.1 mask 255.255.255.0 192.168.1.1

atcmd /dev/ttyACM0 115200 AT+CPIN? 