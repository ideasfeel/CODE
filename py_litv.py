# -*- coding: utf-8 -*-
# @Author  : Doubebly
# @Time    : 2025/3/23 21:55


import sys
import time
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "Litv"

    def init(self, extend):
        pass

    def getDependence(self):
        return []

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass


    def liveContent(self, url):

        a = [
'#EXTM3U',
'#EXTINF:-1 tvg-id="民视" tvg-name="民视" tvg-logo="https://logo.doube.eu.org/民视.png" group-title="台灣頻道",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', 
'#EXTINF:-1 tvg-id="民视台湾台" tvg-name="民视台湾台" tvg-logo="https://logo.doube.eu.org/民视台湾台.png" group-title="台灣頻道",民視台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv001,1,6', 
'#EXTINF:-1 tvg-id="民视台湾台" tvg-name="民视台湾台" tvg-logo="https://logo.doube.eu.org/民视台湾台.png" group-title="台灣頻道",民視台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', 
'#EXTINF:-1 tvg-id="民视第一台" tvg-name="民视第一台" tvg-logo="https://logo.doube.eu.org/民视第一台.png" group-title="台灣頻道",民視第一台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv003,1,6', 
'#EXTINF:-1 tvg-id="台视" tvg-name="台视" tvg-logo="https://logo.doube.eu.org/台视.png" group-title="台灣頻道",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', 
'#EXTINF:-1 tvg-id="台视" tvg-name="台视" tvg-logo="https://logo.doube.eu.org/台视.png" group-title="台灣頻道",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', 
'#EXTINF:-1 tvg-id="中视" tvg-name="中视" tvg-logo="https://logo.doube.eu.org/中视.png" group-title="台灣頻道",中視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', 
'#EXTINF:-1 tvg-id="中视经典台" tvg-name="中视经典台" tvg-logo="https://logo.doube.eu.org/中视经典台.png" group-title="台灣頻道",中視經典', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv080,1,6',
'#EXTINF:-1 tvg-id="中视菁采台" tvg-name="中视菁采台" tvg-logo="https://logo.doube.eu.org/中视菁采台.png" group-title="台灣頻道",中視菁采', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv064,1,8', 
'#EXTINF:-1 tvg-id="华视" tvg-name="华视" tvg-logo="https://logo.doube.eu.org/华视.png" group-title="台灣頻道",華視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', 
'#EXTINF:-1 tvg-id="客家电视台" tvg-name="客家电视台" tvg-logo="https://logo.doube.eu.org/客家电视台.png" group-title="台灣頻道",客家電視台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv043,1,6',
'#EXTINF:-1 tvg-id="緯來日本" tvg-name="緯來日本" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ.png" group-title="台灣頻道",緯來日本ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv771', 
'#EXTINF:-1 tvg-id="緯來育樂" tvg-name="緯來育樂" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ3.png" group-title="台灣頻道",緯來育樂ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv701', 
'#EXTINF:-1 tvg-id="靖天日本台" tvg-name="靖天日本台" tvg-logo="https://logo.doube.eu.org/靖天日本台.png" group-title="台灣頻道",靖天日本台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv047,1,8', 
'#EXTINF:-1 tvg-id="靖天综合台" tvg-name="靖天综合台" tvg-logo="https://logo.doube.eu.org/靖天综合台.png" group-title="台灣頻道",靖天綜合台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv046,1,8', 
'#EXTINF:-1 tvg-id="靖天欢乐台" tvg-name="靖天欢乐台" tvg-logo="https://logo.doube.eu.org/靖天欢乐台.png" group-title="台灣頻道",靖天歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv054,1,8',  
'#EXTINF:-1 tvg-id="靖天育乐台" tvg-name="靖天育乐台" tvg-logo="https://logo.doube.eu.org/靖天育乐台.png" group-title="台灣頻道",靖天育樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv062,1,8', 
'#EXTINF:-1 tvg-id="靖天国际台" tvg-name="靖天国际台" tvg-logo="https://logo.doube.eu.org/靖天国际台.png" group-title="台灣頻道",靖天國際台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv063,1,6', 
'#EXTINF:-1 tvg-id="靖天资讯台" tvg-name="靖天资讯台" tvg-logo="https://logo.doube.eu.org/靖天资讯台.png" group-title="台灣頻道",靖天資訊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv065,1,8',
'#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="台灣頻道",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', 
'#EXTINF:-1 tvg-id="TVBS精采台" tvg-name="TVBS精采台" tvg-logo="https://logo.doube.eu.org/TVBS精采台.png" group-title="台灣頻道",Tvbs精采台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv067,1,8', 
'#EXTINF:-1 tvg-id="八大综艺" tvg-name="八大综艺" tvg-logo="https://logo.doube.eu.org/八大综艺.png" group-title="台灣頻道",八大綜藝台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv039,1,7', 
'#EXTINF:-1 tvg-id="中天亚洲" tvg-name="中天亚洲" tvg-logo="https://logo.doube.eu.org/中天亚洲.png" group-title="台灣頻道",中天亞洲台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv109,1,7', 
'#EXTINF:-1 tvg-id="ARIRANG" tvg-name="ARIRANG" tvg-logo="https://logo.doube.eu.org/ARIRANG.png" group-title="台灣頻道",阿里郎', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv079,1,2', 
'#EXTINF:-1 tvg-id="国会频道1" tvg-name="国会频道1" tvg-logo="https://logo.doube.eu.org/国会频道1.png" group-title="台灣頻道",國會頻道1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv084,1,6', 
'#EXTINF:-1 tvg-id="国会频道2" tvg-name="国会频道2" tvg-logo="https://logo.doube.eu.org/国会频道2.png" group-title="台灣頻道",國會頻道2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv085,1,5', 
'#EXTINF:-1 tvg-id="好消息1" tvg-name="好消息1" tvg-logo="https://logo.doube.eu.org/好消息1.png" group-title="台灣頻道",好消息1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,2', 
'#EXTINF:-1 tvg-id="好消息1" tvg-name="好消息1" tvg-logo="https://logo.doube.eu.org/好消息1.png" group-title="台灣頻道",好消息1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,6', 
'#EXTINF:-1 tvg-id="好消息2" tvg-name="好消息2" tvg-logo="https://logo.doube.eu.org/好消息2.png" group-title="台灣頻道",好消息2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,2', 
'#EXTINF:-1 tvg-id="好消息2" tvg-name="好消息2" tvg-logo="https://logo.doube.eu.org/好消息2.png" group-title="台灣頻道",好消息2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,6', 
'#EXTINF:-1 tvg-id="民视新闻台" tvg-name="民视新闻台" tvg-logo="https://logo.doube.eu.org/民视新闻台.png" group-title="台灣頻道",民視新聞台', 'http://38.64.72.148:80/hls/modn/list/4012/chunklist0.m3u8', 
'#EXTINF:-1 tvg-id="台视新闻台" tvg-name="台视新闻台" tvg-logo="https://logo.doube.eu.org/台视新闻台.png" group-title="台灣頻道",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,2', 
'#EXTINF:-1 tvg-id="台视新闻台" tvg-name="台视新闻台" tvg-logo="https://logo.doube.eu.org/台视新闻台.png" group-title="台灣頻道",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,6', 
'#EXTINF:-1 tvg-id="台视财经台" tvg-name="台视财经台" tvg-logo="https://logo.doube.eu.org/台视财经台.png" group-title="台灣頻道",台視財經', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv056,1,2',
'#EXTINF:-1 tvg-id="中视新闻台" tvg-name="中视新闻台" tvg-logo="https://logo.doube.eu.org/中视新闻台.png" group-title="台灣頻道",中視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv074,1,2', 
'#EXTINF:-1 tvg-id="华视新闻" tvg-name="华视新闻" tvg-logo="https://logo.doube.eu.org/华视新闻.png" group-title="台灣頻道",華視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv052,1,2', 
'#EXTINF:-1 tvg-id="TVBS新闻" tvg-name="TVBS新闻" tvg-logo="https://logo.doube.eu.org/TVBS新闻.png" group-title="台灣頻道",Tvbs新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2',
'#EXTINF:-1 tvg-id="年代新聞" tvg-name="年代新聞" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/ER2.png" group-title="台灣頻道",年代新聞', 'http://211.23.114.106:8517/http/60.251.39.91:8081/hls/67/809/ch27.m3u8',
'#EXTINF:-1 tvg-id="非凡新闻" tvg-name="非凡新闻" tvg-logo="https://logo.doube.eu.org/非凡新闻.png" group-title="台灣頻道",非凡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv010,1,6', 
'#EXTINF:-1 tvg-id="非凡商业" tvg-name="非凡商业" tvg-logo="https://logo.doube.eu.org/非凡商业.png" group-title="台灣頻道",非凡商業', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv048,1,2', 
'#EXTINF:-1 tvg-id="寰宇新闻台" tvg-name="寰宇新闻台" tvg-logo="https://logo.doube.eu.org/寰宇新闻台.png" group-title="台灣頻道",寰宇新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', 
'#EXTINF:-1 tvg-id="寰宇新闻台湾台" tvg-name="寰宇新闻台湾台" tvg-logo="https://logo.doube.eu.org/寰宇新闻台湾台.png" group-title="台灣頻道",寰宇新聞台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6',  
'#EXTINF:-1 tvg-id="东森新闻台" tvg-name="东森新闻台" tvg-logo="https://logo.doube.eu.org/东森新闻台.png" group-title="台灣頻道",東森新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', 
'#EXTINF:-1 tvg-id="东森财经新闻台" tvg-name="东森财经新闻台" tvg-logo="https://logo.doube.eu.org/东森财经新闻台.png" group-title="台灣頻道",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,2', 
'#EXTINF:-1 tvg-id="东森财经新闻台" tvg-name="东森财经新闻台" tvg-logo="https://logo.doube.eu.org/东森财经新闻台.png" group-title="台灣頻道",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,6', 
'#EXTINF:-1 tvg-id="镜电视新闻台" tvg-name="镜电视新闻台" tvg-logo="https://logo.doube.eu.org/镜电视新闻台.png" group-title="台灣頻道",鏡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', 
'#EXTINF:-1 tvg-id="中天新闻" tvg-name="中天新闻" tvg-logo="https://logo.doube.eu.org/中天新闻.png" group-title="台灣頻道",中天新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', 
'#EXTINF:-1 tvg-id="第1商业台" tvg-name="第1商业台" tvg-logo="https://logo.doube.eu.org/第1商业台.png" group-title="台灣頻道",第1商業台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv104,1,7', 
'#EXTINF:-1 tvg-id="美国之音" tvg-name="美国之音" tvg-logo="https://logo.doube.eu.org/美国之音.png" group-title="台灣頻道",美國之音', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv03,1,7', 
'#EXTINF:-1 tvg-id="半岛国际新闻" tvg-name="半岛国际新闻" tvg-logo="https://logo.doube.eu.org/半岛国际新闻.png" group-title="台灣頻道",半島新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv10,1,7',
'#EXTINF:-1 tvg-id="緯來體育" tvg-name="緯來體育" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ2.png" group-title="台灣頻道",緯來體育ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv721',
'#EXTINF:-1 tvg-id="DAZN1" tvg-name="DAZN1" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/DAZN.png" group-title="台灣頻道",DAZN1', 'rtmp://f13h.mine.nu/sat/tv731',
'#EXTINF:-1 tvg-id="DAZN2" tvg-name="DAZN2" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/DAZN.png" group-title="台灣頻道",DAZN2', 'rtmp://f13h.mine.nu/sat/tv741',
'#EXTINF:-1 tvg-id="博斯魅力" tvg-name="博斯魅力" tvg-logo="https://logo.doube.eu.org/博斯魅力.png" group-title="台灣頻道",博斯魅力', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn04,5,2', 
'#EXTINF:-1 tvg-id="博斯高球1" tvg-name="博斯高球1" tvg-logo="https://logo.doube.eu.org/博斯高球1.png" group-title="台灣頻道",博斯高球1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn05,5,2', 
'#EXTINF:-1 tvg-id="博斯高球2" tvg-name="博斯高球2" tvg-logo="https://logo.doube.eu.org/博斯高球2.png" group-title="台灣頻道",博斯高球2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn06,5,2', 
'#EXTINF:-1 tvg-id="博斯运动1" tvg-name="博斯运动1" tvg-logo="https://logo.doube.eu.org/博斯运动1.png" group-title="台灣頻道",博斯運動1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn07,5,2', 
'#EXTINF:-1 tvg-id="博斯运动2" tvg-name="博斯运动2" tvg-logo="https://logo.doube.eu.org/博斯运动2.png" group-title="台灣頻道",博斯運動2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn08,5,2', 
'#EXTINF:-1 tvg-id="博斯网球1" tvg-name="博斯网球1" tvg-logo="https://logo.doube.eu.org/博斯网球1.png" group-title="台灣頻道",博斯網球', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn09,5,2', 
'#EXTINF:-1 tvg-id="博斯无限1" tvg-name="博斯无限1" tvg-logo="https://logo.doube.eu.org/博斯无限1.png" group-title="台灣頻道",博斯無限', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn10,5,2', 
'#EXTINF:-1 tvg-id="博斯无限2" tvg-name="博斯无限2" tvg-logo="https://logo.doube.eu.org/博斯无限2.png" group-title="台灣頻道",博斯無限2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn13,4,2', 
'#EXTINF:-1 tvg-id="智林体育台" tvg-name="智林体育台" tvg-logo="https://logo.doube.eu.org/智林体育台.png" group-title="台灣頻道",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,5', 
'#EXTINF:-1 tvg-id="智林体育台" tvg-name="智林体育台" tvg-logo="https://logo.doube.eu.org/智林体育台.png" group-title="台灣頻道",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,6', 
'#EXTINF:-1 tvg-id="时尚运动X" tvg-name="时尚运动X" tvg-logo="https://logo.doube.eu.org/时尚运动X.png" group-title="台灣頻道",時尚運動X', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv014,1,5', 
'#EXTINF:-1 tvg-id="TraceSportStars" tvg-name="TraceSportStars" tvg-logo="https://logo.doube.eu.org/TraceSportStars.png" group-title="台灣頻道",TRACE SPORTS STARS', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,2', 
'#EXTINF:-1 tvg-id="GINXEsportsTV" tvg-name="GINXEsportsTV" tvg-logo="https://logo.doube.eu.org/GINXEsportsTV.png" group-title="台灣頻道",GINXEsportsTV', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv053,1,8', 
'#EXTINF:-1 tvg-id="Smart知识台" tvg-name="Smart知识台" tvg-logo="https://logo.doube.eu.org/Smart知识台.png" group-title="台灣頻道",Smart知識台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn19,5,2',
'#EXTINF:-1 tvg-id="Globetrotter" tvg-name="Globetrotter" tvg-logo="https://logo.doube.eu.org/Globetrotter.png" group-title="台灣頻道",GLOBETROTTER', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv016,1,6',
'#EXTINF:-1 tvg-id="民视旅游台" tvg-name="民视旅游台" tvg-logo="https://logo.doube.eu.org/民视旅游台.png" group-title="台灣頻道",民視旅遊', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv07,1,7', 
'#EXTINF:-1 tvg-id="亚洲旅游台" tvg-name="亚洲旅游台" tvg-logo="https://logo.doube.eu.org/亚洲旅游台.png" group-title="台灣頻道",亞洲旅遊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', 
'#EXTINF:-1 tvg-id="Discovery" tvg-name="Discovery" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/ASIA.png" group-title="台灣頻道",Discovery', 'http://125.227.210.55:8154/VideoInput/play.ts', 
'#EXTINF:-1 tvg-id="视纳华仁纪实" tvg-name="视纳华仁纪实" tvg-logo="https://logo.doube.eu.org/视纳华仁纪实.png" group-title="台灣頻道",視納華仁紀實頻道', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv013,1,6', 
'#EXTINF:-1 tvg-id="HBOᴴ" tvg-name="HBOᴴᴰ" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/HBO.png" group-title="台灣頻道",HBOᴴᴰ', 'http://125.227.210.55:8153/VideoInput/play.ts', 
'#EXTINF:-1 tvg-id="amc电影台" tvg-name="amc电影台" tvg-logo="https://logo.doube.eu.org/amc电影台.png" group-title="台灣頻道",amc電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', 
'#EXTINF:-1 tvg-id="影迷數位電影台" tvg-name="影迷數位電影台" tvg-logo="https://logo.doube.eu.org/影迷數位電影台.png" group-title="台灣頻道",影迷數位電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv011,1,6', 
'#EXTINF:-1 tvg-id="龙华洋片台" tvg-name="龙华洋片台" tvg-logo="https://logo.doube.eu.org/龙华洋片台.png" group-title="台灣頻道",龍華洋片', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', 
'#EXTINF:-1 tvg-id="龙华经典台" tvg-name="龙华经典台" tvg-logo="https://logo.doube.eu.org/龙华经典台.png" group-title="台灣頻道",龍華經典', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn21,5,2', 
'#EXTINF:-1 tvg-id="龙华戏剧台" tvg-name="龙华戏剧台" tvg-logo="https://logo.doube.eu.org/龙华戏剧台.png" group-title="台灣頻道",龍華戲劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn18,5,6', 
'#EXTINF:-1 tvg-id="龙华电影台" tvg-name="龙华电影台" tvg-logo="https://logo.doube.eu.org/龙华电影台.png" group-title="台灣頻道",龍華電影', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn03,5,6', 
'#EXTINF:-1 tvg-id="龙华日韩台" tvg-name="龙华日韩台" tvg-logo="https://logo.doube.eu.org/龙华日韩台.png" group-title="台灣頻道",龍華日韓', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn11,5,2', 
'#EXTINF:-1 tvg-id="龙华偶像台" tvg-name="龙华偶像台" tvg-logo="https://logo.doube.eu.org/龙华偶像台.png" group-title="台灣頻道",龍華偶像', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn12,5,2',
'#EXTINF:-1 tvg-id="靖天映画" tvg-name="靖天映画" tvg-logo="https://logo.doube.eu.org/靖天映画.png" group-title="台灣頻道",靖天映畫', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', 
'#EXTINF:-1 tvg-id="靖天电影台" tvg-name="靖天电影台" tvg-logo="https://logo.doube.eu.org/靖天电影台.png" group-title="台灣頻道",靖天電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', 
'#EXTINF:-1 tvg-id="靖天戏剧台" tvg-name="靖天戏剧台" tvg-logo="https://logo.doube.eu.org/靖天戏剧台.png" group-title="台灣頻道",靖天戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv058,1,8',
'#EXTINF:-1 tvg-id="靖洋戏剧台" tvg-name="靖洋戏剧台" tvg-logo="https://logo.doube.eu.org/靖洋戏剧台.png" group-title="台灣頻道",靖洋戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv045,1,6', 
'#EXTINF:-1 tvg-id="民视影剧台" tvg-name="民视影剧台" tvg-logo="https://logo.doube.eu.org/民视影剧台.png" group-title="台灣頻道",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,2', 
'#EXTINF:-1 tvg-id="民视影剧台" tvg-name="民视影剧台" tvg-logo="https://logo.doube.eu.org/民视影剧台.png" group-title="台灣頻道",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,7', 
'#EXTINF:-1 tvg-id="台湾戏剧台" tvg-name="台湾戏剧台" tvg-logo="https://logo.doube.eu.org/台湾戏剧台.png" group-title="台灣頻道",台灣戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn22,5,2', 
'#EXTINF:-1 tvg-id="公视戏剧" tvg-name="公视戏剧" tvg-logo="https://logo.doube.eu.org/公视戏剧.png" group-title="台灣頻道",公視戲劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv042,1,6', 
'#EXTINF:-1 tvg-id="采昌影剧台" tvg-name="采昌影剧台" tvg-logo="https://logo.doube.eu.org/采昌影剧台.png" group-title="台灣頻道",采昌影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv049,1,8', 
'#EXTINF:-1 tvg-id="CLASSICA古典乐" tvg-name="CLASSICA古典乐" tvg-logo="https://logo.doube.eu.org/CLASSICA古典乐.png" group-title="台灣頻道",古典音樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv059,1,6', 
'#EXTINF:-1 tvg-id="TraceUrban" tvg-name="TraceUrban" tvg-logo="https://logo.doube.eu.org/TraceUrban.png" group-title="台灣頻道",TRACE URBAN', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,6',
'#EXTINF:-1 tvg-id="MezzoLiveHD" tvg-name="MezzoLiveHD" tvg-logo="https://logo.doube.eu.org/MezzoLiveHD.png" group-title="台灣頻道",MEZZO LIVE', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv083,1,6', 
'#EXTINF:-1 tvg-id="ELTV娱乐" tvg-name="ELTV娱乐" tvg-logo="https://logo.doube.eu.org/ELTV娱乐.png" group-title="台灣頻道",愛爾達娛樂', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv070,1,7',
'#EXTINF:-1 tvg-id="民视综艺台" tvg-name="民视综艺台" tvg-logo="https://logo.doube.eu.org/民视综艺台.png" group-title="台灣頻道",民視綜藝', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv004,1,8',
'#EXTINF:-1 tvg-id="TVBS欢乐台" tvg-name="TVBS欢乐台" tvg-logo="https://logo.doube.eu.org/TVBS欢乐台.png" group-title="台灣頻道",Tvbs歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv068,1,7', 
'#EXTINF:-1 tvg-id="八大精彩" tvg-name="八大精彩" tvg-logo="https://logo.doube.eu.org/八大精彩.png" group-title="台灣頻道",八大精彩台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv034,1,6',
'#EXTINF:-1 tvg-id="猪哥亮歌厅秀" tvg-name="猪哥亮歌厅秀" tvg-logo="https://logo.doube.eu.org/猪哥亮歌厅秀.png" group-title="台灣頻道",豬哥亮歌廳秀', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv006,1,9',
'#EXTINF:-1 tvg-id="龙华卡通台" tvg-name="龙华卡通台" tvg-logo="https://logo.doube.eu.org/龙华卡通台.png" group-title="台灣頻道",龍華卡通', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,2', 
'#EXTINF:-1 tvg-id="龙华卡通台" tvg-name="龙华卡通台" tvg-logo="https://logo.doube.eu.org/龙华卡通台.png" group-title="台灣頻道",龍華卡通', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,5', 
'#EXTINF:-1 tvg-id="靖天卡通台" tvg-name="靖天卡通台" tvg-logo="https://logo.doube.eu.org/靖天卡通台.png" group-title="台灣頻道",靖天卡通台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv044,1,8', 
'#EXTINF:-1 tvg-id="靖洋卡通台" tvg-name="靖洋卡通台" tvg-logo="https://logo.doube.eu.org/靖洋卡通台.png" group-title="台灣頻道",靖天卡通台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv057,1,8', 
'#EXTINF:-1 tvg-id="达文西频道" tvg-name="达文西频道" tvg-logo="https://logo.doube.eu.org/达文西频道.png" group-title="台灣頻道",達文西頻道', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv018,1,6', 
'#EXTINF:-1 tvg-id="ELTV生活英语台" tvg-name="ELTV生活英语台" tvg-logo="https://logo.doube.eu.org/ELTV生活英语台.png" group-title="台灣頻道",生活英語台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn20,5,6', 


'#EXTINF:-1 tvg-id="緯來日本" tvg-name="緯來日本" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ.png" group-title="綜合其他",緯來日本ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv771', 
'#EXTINF:-1 tvg-id="緯來育樂" tvg-name="緯來育樂" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ3.png" group-title="綜合其他",緯來育樂ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv701', 
'#EXTINF:-1 tvg-id="靖天日本台" tvg-name="靖天日本台" tvg-logo="https://logo.doube.eu.org/靖天日本台.png" group-title="綜合其他",靖天日本台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv047,1,8', 
'#EXTINF:-1 tvg-id="靖天综合台" tvg-name="靖天综合台" tvg-logo="https://logo.doube.eu.org/靖天综合台.png" group-title="綜合其他",靖天綜合台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv046,1,8', 
'#EXTINF:-1 tvg-id="靖天欢乐台" tvg-name="靖天欢乐台" tvg-logo="https://logo.doube.eu.org/靖天欢乐台.png" group-title="綜合其他",靖天歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv054,1,8',  
'#EXTINF:-1 tvg-id="靖天育乐台" tvg-name="靖天育乐台" tvg-logo="https://logo.doube.eu.org/靖天育乐台.png" group-title="綜合其他",靖天育樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv062,1,8', 
'#EXTINF:-1 tvg-id="靖天国际台" tvg-name="靖天国际台" tvg-logo="https://logo.doube.eu.org/靖天国际台.png" group-title="綜合其他",靖天國際台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv063,1,6', 
'#EXTINF:-1 tvg-id="靖天资讯台" tvg-name="靖天资讯台" tvg-logo="https://logo.doube.eu.org/靖天资讯台.png" group-title="綜合其他",靖天資訊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv065,1,8',
'#EXTINF:-1 tvg-id="民视" tvg-name="民视" tvg-logo="https://logo.doube.eu.org/民视.png" group-title="綜合其他",民視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv002,1,10', 
'#EXTINF:-1 tvg-id="民视台湾台" tvg-name="民视台湾台" tvg-logo="https://logo.doube.eu.org/民视台湾台.png" group-title="綜合其他",民視台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv001,1,6', 
'#EXTINF:-1 tvg-id="民视台湾台" tvg-name="民视台湾台" tvg-logo="https://logo.doube.eu.org/民视台湾台.png" group-title="綜合其他",民視台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6', 
'#EXTINF:-1 tvg-id="民视第一台" tvg-name="民视第一台" tvg-logo="https://logo.doube.eu.org/民视第一台.png" group-title="綜合其他",民視第一台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv003,1,6', 
'#EXTINF:-1 tvg-id="台视" tvg-name="台视" tvg-logo="https://logo.doube.eu.org/台视.png" group-title="綜合其他",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,2', 
'#EXTINF:-1 tvg-id="台视" tvg-name="台视" tvg-logo="https://logo.doube.eu.org/台视.png" group-title="綜合其他",台視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv066,1,6', 
'#EXTINF:-1 tvg-id="中视" tvg-name="中视" tvg-logo="https://logo.doube.eu.org/中视.png" group-title="綜合其他",中視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv040,1,6', 
'#EXTINF:-1 tvg-id="中视经典台" tvg-name="中视经典台" tvg-logo="https://logo.doube.eu.org/中视经典台.png" group-title="綜合其他",中視經典', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv080,1,6',
'#EXTINF:-1 tvg-id="中视菁采台" tvg-name="中视菁采台" tvg-logo="https://logo.doube.eu.org/中视菁采台.png" group-title="綜合其他",中視菁采', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv064,1,8', 
'#EXTINF:-1 tvg-id="华视" tvg-name="华视" tvg-logo="https://logo.doube.eu.org/华视.png" group-title="綜合其他",華視', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv041,1,6', 
'#EXTINF:-1 tvg-id="客家电视台" tvg-name="客家电视台" tvg-logo="https://logo.doube.eu.org/客家电视台.png" group-title="綜合其他",客家電視台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv043,1,6',
'#EXTINF:-1 tvg-id="TVBS" tvg-name="TVBS" tvg-logo="https://logo.doube.eu.org/TVBS.png" group-title="綜合其他",Tvbs', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv073,1,2', 
'#EXTINF:-1 tvg-id="TVBS精采台" tvg-name="TVBS精采台" tvg-logo="https://logo.doube.eu.org/TVBS精采台.png" group-title="綜合其他",Tvbs精采台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv067,1,8', 
'#EXTINF:-1 tvg-id="八大综艺" tvg-name="八大综艺" tvg-logo="https://logo.doube.eu.org/八大综艺.png" group-title="綜合其他",八大綜藝台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv039,1,7', 
'#EXTINF:-1 tvg-id="中天亚洲" tvg-name="中天亚洲" tvg-logo="https://logo.doube.eu.org/中天亚洲.png" group-title="綜合其他",中天亞洲台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv109,1,7', 
'#EXTINF:-1 tvg-id="ARIRANG" tvg-name="ARIRANG" tvg-logo="https://logo.doube.eu.org/ARIRANG.png" group-title="綜合其他",阿里郎', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv079,1,2', 
'#EXTINF:-1 tvg-id="国会频道1" tvg-name="国会频道1" tvg-logo="https://logo.doube.eu.org/国会频道1.png" group-title="綜合其他",國會頻道1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv084,1,6', 
'#EXTINF:-1 tvg-id="国会频道2" tvg-name="国会频道2" tvg-logo="https://logo.doube.eu.org/国会频道2.png" group-title="綜合其他",國會頻道2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv085,1,5', 
'#EXTINF:-1 tvg-id="好消息1" tvg-name="好消息1" tvg-logo="https://logo.doube.eu.org/好消息1.png" group-title="綜合其他",好消息1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,2', 
'#EXTINF:-1 tvg-id="好消息1" tvg-name="好消息1" tvg-logo="https://logo.doube.eu.org/好消息1.png" group-title="綜合其他",好消息1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv16,1,6', 
'#EXTINF:-1 tvg-id="好消息2" tvg-name="好消息2" tvg-logo="https://logo.doube.eu.org/好消息2.png" group-title="綜合其他",好消息2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,2', 
'#EXTINF:-1 tvg-id="好消息2" tvg-name="好消息2" tvg-logo="https://logo.doube.eu.org/好消息2.png" group-title="綜合其他",好消息2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv17,1,6', 
'#EXTINF:-1 tvg-id="民视新闻台" tvg-name="民视新闻台" tvg-logo="https://logo.doube.eu.org/民视新闻台.png" group-title="新聞財經",民視新聞台', 'http://38.64.72.148:80/hls/modn/list/4012/chunklist0.m3u8', 
'#EXTINF:-1 tvg-id="台视新闻台" tvg-name="台视新闻台" tvg-logo="https://logo.doube.eu.org/台视新闻台.png" group-title="新聞財經",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,2', 
'#EXTINF:-1 tvg-id="台视新闻台" tvg-name="台视新闻台" tvg-logo="https://logo.doube.eu.org/台视新闻台.png" group-title="新聞財經",台視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv051,1,6', 
'#EXTINF:-1 tvg-id="台视财经台" tvg-name="台视财经台" tvg-logo="https://logo.doube.eu.org/台视财经台.png" group-title="新聞財經",台視財經', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv056,1,2',
'#EXTINF:-1 tvg-id="中视新闻台" tvg-name="中视新闻台" tvg-logo="https://logo.doube.eu.org/中视新闻台.png" group-title="新聞財經",中視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv074,1,2', 
'#EXTINF:-1 tvg-id="华视新闻" tvg-name="华视新闻" tvg-logo="https://logo.doube.eu.org/华视新闻.png" group-title="新聞財經",華視新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv052,1,2', 
'#EXTINF:-1 tvg-id="TVBS新闻" tvg-name="TVBS新闻" tvg-logo="https://logo.doube.eu.org/TVBS新闻.png" group-title="新聞財經",Tvbs新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv072,1,2',
'#EXTINF:-1 tvg-id="年代新聞" tvg-name="年代新聞" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/ER2.png" group-title="新聞財經",年代新聞', 'http://211.23.114.106:8517/http/60.251.39.91:8081/hls/67/809/ch27.m3u8',
'#EXTINF:-1 tvg-id="非凡新闻" tvg-name="非凡新闻" tvg-logo="https://logo.doube.eu.org/非凡新闻.png" group-title="新聞財經",非凡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv010,1,6', 
'#EXTINF:-1 tvg-id="非凡商业" tvg-name="非凡商业" tvg-logo="https://logo.doube.eu.org/非凡商业.png" group-title="新聞財經",非凡商業', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv048,1,2', 
'#EXTINF:-1 tvg-id="寰宇新闻台" tvg-name="寰宇新闻台" tvg-logo="https://logo.doube.eu.org/寰宇新闻台.png" group-title="新聞財經",寰宇新聞台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn14,1,2', 
'#EXTINF:-1 tvg-id="寰宇新闻台湾台" tvg-name="寰宇新闻台湾台" tvg-logo="https://logo.doube.eu.org/寰宇新闻台湾台.png" group-title="新聞財經",寰宇新聞台灣台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv156,1,6',  
'#EXTINF:-1 tvg-id="东森新闻台" tvg-name="东森新闻台" tvg-logo="https://logo.doube.eu.org/东森新闻台.png" group-title="新聞財經",東森新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv152,1,6', 
'#EXTINF:-1 tvg-id="东森财经新闻台" tvg-name="东森财经新闻台" tvg-logo="https://logo.doube.eu.org/东森财经新闻台.png" group-title="新聞財經",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,2', 
'#EXTINF:-1 tvg-id="东森财经新闻台" tvg-name="东森财经新闻台" tvg-logo="https://logo.doube.eu.org/东森财经新闻台.png" group-title="新聞財經",東森財經新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv153,1,6', 
'#EXTINF:-1 tvg-id="镜电视新闻台" tvg-name="镜电视新闻台" tvg-logo="https://logo.doube.eu.org/镜电视新闻台.png" group-title="新聞財經",鏡新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv075,1,2', 
'#EXTINF:-1 tvg-id="中天新闻" tvg-name="中天新闻" tvg-logo="https://logo.doube.eu.org/中天新闻.png" group-title="新聞財經",中天新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv009,2,7', 
'#EXTINF:-1 tvg-id="第1商业台" tvg-name="第1商业台" tvg-logo="https://logo.doube.eu.org/第1商业台.png" group-title="新聞財經",第1商業台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv104,1,7', 
'#EXTINF:-1 tvg-id="美国之音" tvg-name="美国之音" tvg-logo="https://logo.doube.eu.org/美国之音.png" group-title="新聞財經",美國之音', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv03,1,7', 
'#EXTINF:-1 tvg-id="半岛国际新闻" tvg-name="半岛国际新闻" tvg-logo="https://logo.doube.eu.org/半岛国际新闻.png" group-title="新聞財經",半島新聞', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv10,1,7',
'#EXTINF:-1 tvg-id="緯來體育" tvg-name="緯來體育" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/WRJ2.png" group-title="體育競技",緯來體育ᴴᴰ', 'rtmp://f13h.mine.nu/sat/tv721',
'#EXTINF:-1 tvg-id="DAZN1" tvg-name="DAZN1" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/DAZN.png" group-title="體育競技",DAZN1', 'rtmp://f13h.mine.nu/sat/tv731',
'#EXTINF:-1 tvg-id="DAZN2" tvg-name="DAZN2" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/DAZN.png" group-title="體育競技",DAZN2', 'rtmp://f13h.mine.nu/sat/tv741',
'#EXTINF:-1 tvg-id="博斯魅力" tvg-name="博斯魅力" tvg-logo="https://logo.doube.eu.org/博斯魅力.png" group-title="體育競技",博斯魅力', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn04,5,2', 
'#EXTINF:-1 tvg-id="博斯高球1" tvg-name="博斯高球1" tvg-logo="https://logo.doube.eu.org/博斯高球1.png" group-title="體育競技",博斯高球1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn05,5,2', 
'#EXTINF:-1 tvg-id="博斯高球2" tvg-name="博斯高球2" tvg-logo="https://logo.doube.eu.org/博斯高球2.png" group-title="體育競技",博斯高球2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn06,5,2', 
'#EXTINF:-1 tvg-id="博斯运动1" tvg-name="博斯运动1" tvg-logo="https://logo.doube.eu.org/博斯运动1.png" group-title="體育競技",博斯運動1', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn07,5,2', 
'#EXTINF:-1 tvg-id="博斯运动2" tvg-name="博斯运动2" tvg-logo="https://logo.doube.eu.org/博斯运动2.png" group-title="體育競技",博斯運動2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn08,5,2', 
'#EXTINF:-1 tvg-id="博斯网球1" tvg-name="博斯网球1" tvg-logo="https://logo.doube.eu.org/博斯网球1.png" group-title="體育競技",博斯網球', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn09,5,2', 
'#EXTINF:-1 tvg-id="博斯无限1" tvg-name="博斯无限1" tvg-logo="https://logo.doube.eu.org/博斯无限1.png" group-title="體育競技",博斯無限', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn10,5,2', 
'#EXTINF:-1 tvg-id="博斯无限2" tvg-name="博斯无限2" tvg-logo="https://logo.doube.eu.org/博斯无限2.png" group-title="體育競技",博斯無限2', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn13,4,2', 
'#EXTINF:-1 tvg-id="智林体育台" tvg-name="智林体育台" tvg-logo="https://logo.doube.eu.org/智林体育台.png" group-title="體育競技",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,5', 
'#EXTINF:-1 tvg-id="智林体育台" tvg-name="智林体育台" tvg-logo="https://logo.doube.eu.org/智林体育台.png" group-title="體育競技",智林體育台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv101,1,6', 
'#EXTINF:-1 tvg-id="时尚运动X" tvg-name="时尚运动X" tvg-logo="https://logo.doube.eu.org/时尚运动X.png" group-title="體育競技",時尚運動X', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv014,1,5', 
'#EXTINF:-1 tvg-id="TraceSportStars" tvg-name="TraceSportStars" tvg-logo="https://logo.doube.eu.org/TraceSportStars.png" group-title="體育競技",TRACE SPORTS STARS', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,2', 
'#EXTINF:-1 tvg-id="GINXEsportsTV" tvg-name="GINXEsportsTV" tvg-logo="https://logo.doube.eu.org/GINXEsportsTV.png" group-title="體育競技",GINXEsportsTV', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv053,1,8', 
'#EXTINF:-1 tvg-id="Smart知识台" tvg-name="Smart知识台" tvg-logo="https://logo.doube.eu.org/Smart知识台.png" group-title="生活旅遊",Smart知識台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn19,5,2',
'#EXTINF:-1 tvg-id="Globetrotter" tvg-name="Globetrotter" tvg-logo="https://logo.doube.eu.org/Globetrotter.png" group-title="生活旅遊",GLOBETROTTER', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv016,1,6',
'#EXTINF:-1 tvg-id="民视旅游台" tvg-name="民视旅游台" tvg-logo="https://logo.doube.eu.org/民视旅游台.png" group-title="生活旅遊",民視旅遊', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv07,1,7', 
'#EXTINF:-1 tvg-id="亚洲旅游台" tvg-name="亚洲旅游台" tvg-logo="https://logo.doube.eu.org/亚洲旅游台.png" group-title="生活旅遊",亞洲旅遊台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv076,1,2', 
'#EXTINF:-1 tvg-id="Discovery" tvg-name="Discovery" tvg-logo="https://raw.githubusercontent.com/ideasfeel/IMG/refs/heads/main/ASIA.png" group-title="紀實探索",Discovery', 'http://125.227.210.55:8154/VideoInput/play.ts', 
'#EXTINF:-1 tvg-id="视纳华仁纪实" tvg-name="视纳华仁纪实" tvg-logo="https://logo.doube.eu.org/视纳华仁纪实.png" group-title="紀實探索",視納華仁紀實頻道', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv013,1,6', 
'#EXTINF:-1 tvg-id="amc电影台" tvg-name="amc电影台" tvg-logo="https://logo.doube.eu.org/amc电影台.png" group-title="電影戲劇",amc電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv017,1,6', 
'#EXTINF:-1 tvg-id="影迷數位電影台" tvg-name="影迷數位電影台" tvg-logo="https://logo.doube.eu.org/影迷數位電影台.png" group-title="電影戲劇",影迷數位電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv011,1,6', 
'#EXTINF:-1 tvg-id="龙华洋片台" tvg-name="龙华洋片台" tvg-logo="https://logo.doube.eu.org/龙华洋片台.png" group-title="電影戲劇",龍華洋片', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn02,5,2', 
'#EXTINF:-1 tvg-id="龙华经典台" tvg-name="龙华经典台" tvg-logo="https://logo.doube.eu.org/龙华经典台.png" group-title="電影戲劇",龍華經典', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn21,5,2', 
'#EXTINF:-1 tvg-id="龙华戏剧台" tvg-name="龙华戏剧台" tvg-logo="https://logo.doube.eu.org/龙华戏剧台.png" group-title="電影戲劇",龍華戲劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn18,5,6', 
'#EXTINF:-1 tvg-id="龙华电影台" tvg-name="龙华电影台" tvg-logo="https://logo.doube.eu.org/龙华电影台.png" group-title="電影戲劇",龍華電影', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn03,5,6', 
'#EXTINF:-1 tvg-id="龙华日韩台" tvg-name="龙华日韩台" tvg-logo="https://logo.doube.eu.org/龙华日韩台.png" group-title="電影戲劇",龍華日韓', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn11,5,2', 
'#EXTINF:-1 tvg-id="龙华偶像台" tvg-name="龙华偶像台" tvg-logo="https://logo.doube.eu.org/龙华偶像台.png" group-title="電影戲劇",龍華偶像', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn12,5,2',
'#EXTINF:-1 tvg-id="靖天映画" tvg-name="靖天映画" tvg-logo="https://logo.doube.eu.org/靖天映画.png" group-title="電影戲劇",靖天映畫', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv055,1,8', 
'#EXTINF:-1 tvg-id="靖天电影台" tvg-name="靖天电影台" tvg-logo="https://logo.doube.eu.org/靖天电影台.png" group-title="電影戲劇",靖天電影台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv061,1,7', 
'#EXTINF:-1 tvg-id="靖天戏剧台" tvg-name="靖天戏剧台" tvg-logo="https://logo.doube.eu.org/靖天戏剧台.png" group-title="電影戲劇",靖天戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv058,1,8',
'#EXTINF:-1 tvg-id="靖洋戏剧台" tvg-name="靖洋戏剧台" tvg-logo="https://logo.doube.eu.org/靖洋戏剧台.png" group-title="電影戲劇",靖洋戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv045,1,6', 
'#EXTINF:-1 tvg-id="民视影剧台" tvg-name="民视影剧台" tvg-logo="https://logo.doube.eu.org/民视影剧台.png" group-title="電影戲劇",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,2', 
'#EXTINF:-1 tvg-id="民视影剧台" tvg-name="民视影剧台" tvg-logo="https://logo.doube.eu.org/民视影剧台.png" group-title="電影戲劇",民視影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-ftv09,1,7', 
'#EXTINF:-1 tvg-id="台湾戏剧台" tvg-name="台湾戏剧台" tvg-logo="https://logo.doube.eu.org/台湾戏剧台.png" group-title="電影戲劇",台灣戲劇台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn22,5,2', 
'#EXTINF:-1 tvg-id="公视戏剧" tvg-name="公视戏剧" tvg-logo="https://logo.doube.eu.org/公视戏剧.png" group-title="電影戲劇",公視戲劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv042,1,6', 
'#EXTINF:-1 tvg-id="采昌影剧台" tvg-name="采昌影剧台" tvg-logo="https://logo.doube.eu.org/采昌影剧台.png" group-title="電影戲劇",采昌影劇', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv049,1,8', 
'#EXTINF:-1 tvg-id="CLASSICA古典乐" tvg-name="CLASSICA古典乐" tvg-logo="https://logo.doube.eu.org/CLASSICA古典乐.png" group-title="音樂綜藝",古典音樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv059,1,6', 
'#EXTINF:-1 tvg-id="TraceUrban" tvg-name="TraceUrban" tvg-logo="https://logo.doube.eu.org/TraceUrban.png" group-title="音樂綜藝",TRACE URBAN', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv082,1,6',
'#EXTINF:-1 tvg-id="MezzoLiveHD" tvg-name="MezzoLiveHD" tvg-logo="https://logo.doube.eu.org/MezzoLiveHD.png" group-title="音樂綜藝",MEZZO LIVE', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv083,1,6', 
'#EXTINF:-1 tvg-id="ELTV娱乐" tvg-name="ELTV娱乐" tvg-logo="https://logo.doube.eu.org/ELTV娱乐.png" group-title="音樂綜藝",愛爾達娛樂', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv070,1,7',
'#EXTINF:-1 tvg-id="民视综艺台" tvg-name="民视综艺台" tvg-logo="https://logo.doube.eu.org/民视综艺台.png" group-title="音樂綜藝",民視綜藝', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv004,1,8',
'#EXTINF:-1 tvg-id="TVBS欢乐台" tvg-name="TVBS欢乐台" tvg-logo="https://logo.doube.eu.org/TVBS欢乐台.png" group-title="音樂綜藝",Tvbs歡樂台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv068,1,7', 
'#EXTINF:-1 tvg-id="八大精彩" tvg-name="八大精彩" tvg-logo="https://logo.doube.eu.org/八大精彩.png" group-title="音樂綜藝",八大精彩台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv034,1,6',
'#EXTINF:-1 tvg-id="猪哥亮歌厅秀" tvg-name="猪哥亮歌厅秀" tvg-logo="https://logo.doube.eu.org/猪哥亮歌厅秀.png" group-title="音樂綜藝",豬哥亮歌廳秀', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv006,1,9',
'#EXTINF:-1 tvg-id="龙华卡通台" tvg-name="龙华卡通台" tvg-logo="https://logo.doube.eu.org/龙华卡通台.png" group-title="兒童卡通",龍華卡通', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,2', 
'#EXTINF:-1 tvg-id="龙华卡通台" tvg-name="龙华卡通台" tvg-logo="https://logo.doube.eu.org/龙华卡通台.png" group-title="兒童卡通",龍華卡通', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn01,4,5', 
'#EXTINF:-1 tvg-id="靖天卡通台" tvg-name="靖天卡通台" tvg-logo="https://logo.doube.eu.org/靖天卡通台.png" group-title="兒童卡通",靖天卡通台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv044,1,8', 
'#EXTINF:-1 tvg-id="靖洋卡通台" tvg-name="靖洋卡通台" tvg-logo="https://logo.doube.eu.org/靖洋卡通台.png" group-title="兒童卡通",靖天卡通台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv057,1,8', 
'#EXTINF:-1 tvg-id="达文西频道" tvg-name="达文西频道" tvg-logo="https://logo.doube.eu.org/达文西频道.png" group-title="兒童卡通",達文西頻道', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=4gtv-4gtv018,1,6', 
'#EXTINF:-1 tvg-id="ELTV生活英语台" tvg-name="ELTV生活英语台" tvg-logo="https://logo.doube.eu.org/ELTV生活英语台.png" group-title="兒童卡通",生活英語台', 'http://127.0.0.1:9978/proxy?do=py&type=m3u8&pid=litv-longturn20,5,6' 
]

        return '\n'.join(a)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        # if params['type'] == "media":
        #     return self.proxyMedia(params)
        return None
    def proxyM3u8(self, params):
        pid = params['pid']
        info = pid.split(',')
        a = info[0]
        b = info[1]
        c = info[2]
        timestamp = int(time.time() / 4 - 355017625)
        t = timestamp * 4
        m3u8_text = f'#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:4\n#EXT-X-MEDIA-SEQUENCE:{timestamp}\n'
        for i in range(10):
            m3u8_text += f'#EXTINF:4,\nhttps://ntd-tgc.cdn.hinet.net/live/pool/{a}/litv-pc/{a}-avc1_6000000={b}-mp4a_134000_zho={c}-begin={t}0000000-dur=40000000-seq={timestamp}.ts\n'
            timestamp += 1
            t += 4
        return [200, "application/vnd.apple.mpegurl", m3u8_text]

    def destroy(self):
        return '正在Destroy'


if __name__ == '__main__':
    pass
