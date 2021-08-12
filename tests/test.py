from flask import Flask
import unittest
import requests
from scipy.sparse import data
from werkzeug.wrappers import response
import datetime
app = Flask(__name__)
class InterfaceTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    UPLOAD_URL = "{}/uploading".format(API_URL)
    GRAPHED_URL = "{}/graphed".format(API_URL)
    def test_index_page_loads_html(self):
        print('insure if the content is true')
        response = requests.get(url=InterfaceTest.API_URL)
        self.assertIn(b'Monoprix Main' , response.content)
    def test_upload_page(self):
        print('testing if upload page status is 200 and displays right content')
        r = requests.get(url=InterfaceTest.UPLOAD_URL)
        self.assertEqual(r.status_code,200)
        self.assertIn(b'Monoprix Uploading',r.content)
        print('checking if upload page works with the post method')
        labeling = 'Green'
        textofdisplay = 'Process successful! Would you like to add another dataset to enhance your models ?'
        mydict = {'textofdisplay':textofdisplay,'labeling':labeling}
        tester = app.test_client(self)
        #response = tester.post("/graphed",data=mydict)
        response = requests.post(url=InterfaceTest.UPLOAD_URL,data=mydict)
        #self.assertEqual(response.status_code,200)
    def test_if_args_pass(self):
        print('checking if the page loads (even if it loads empty)')
        res = requests.get(InterfaceTest.GRAPHED_URL)
        self.assertEqual(res.status_code,200)
        self.assertIn(b'Monoprix Forecasting',res.content)
        print('checking if page takes the parameters for the POST method in /graphed')
        data = {"Date":{"0":1388534400000,"1":1391212800000,"2":1393632000000,"3":1396310400000,"4":1398902400000,"5":1401580800000,"6":1404172800000,"7":1406851200000,"8":1409529600000,"9":1412121600000,"10":1414800000000,"11":1417392000000,"12":1420070400000,"13":1422748800000,"14":1425168000000,"15":1427846400000,"16":1430438400000,"17":1433116800000,"18":1435708800000,"19":1438387200000,"20":1441065600000,"21":1443657600000,"22":1446336000000,"23":1448928000000,"24":1451606400000,"25":1454284800000,"26":1456790400000,"27":1459468800000,"28":1462060800000,"29":1464739200000,"30":1467331200000,"31":1470009600000,"32":1472688000000,"33":1475280000000,"34":1477958400000,"35":1480550400000,"36":1483228800000,"37":1485907200000,"38":1488326400000,"39":1491004800000,"40":1493596800000,"41":1496275200000,"42":1498867200000,"43":1501545600000,"44":1504224000000,"45":1506816000000,"46":1509494400000,"47":1512086400000,"48":1514764800000,"49":1517443200000,"50":1519862400000,"51":1522540800000,"52":1525132800000,"53":1527811200000,"54":1530403200000,"55":1533081600000,"56":1535760000000,"57":1538352000000,"58":1541030400000,"59":1543622400000},"predictions":{"0":0.0,"1":0.0,"2":0.0,"3":0.0,"4":0.0,"5":0.0,"6":0.0,"7":0.0,"8":0.0,"9":0.0,"10":0.0,"11":0.0,"12":0.0,"13":0.0,"14":0.0,"15":0.0,"16":0.0,"17":0.0,"18":0.0,"19":0.0,"20":0.0,"21":0.0,"22":0.0,"23":0.0,"24":0.0,"25":0.0,"26":0.0,"27":0.0,"28":0.0,"29":0.0,"30":0.0,"31":23.0,"32":84.0,"33":87.0,"34":43.0,"35":94.0,"36":97.0,"37":42.0,"38":75.0,"39":107.0,"40":152.0,"41":126.0,"42":51.0,"43":130.0,"44":82.0,"45":45.0,"46":76.0,"47":51.0,"48":101.0,"49":61.0,"50":62.0,"51":34.0,"52":105.0,"53":95.0,"54":125.0,"55":54.0,"56":2.0,"57":0.0,"58":18.0,"59":23.0},"shop_id":{"0":1,"1":1,"2":1,"3":1,"4":1,"5":1,"6":1,"7":1,"8":1,"9":1,"10":1,"11":1,"12":1,"13":1,"14":1,"15":1,"16":1,"17":1,"18":1,"19":1,"20":1,"21":1,"22":1,"23":1,"24":1,"25":1,"26":1,"27":1,"28":1,"29":1,"30":1,"31":1,"32":1,"33":1,"34":1,"35":1,"36":1,"37":1,"38":1,"39":1,"40":1,"41":1,"42":1,"43":1,"44":1,"45":1,"46":1,"47":1,"48":1,"49":1,"50":1,"51":1,"52":1,"53":1,"54":1,"55":1,"56":1,"57":1,"58":1,"59":1},"item_id":{"0":283400170,"1":283400170,"2":283400170,"3":283400170,"4":283400170,"5":283400170,"6":283400170,"7":283400170,"8":283400170,"9":283400170,"10":283400170,"11":283400170,"12":283400170,"13":283400170,"14":283400170,"15":283400170,"16":283400170,"17":283400170,"18":283400170,"19":283400170,"20":283400170,"21":283400170,"22":283400170,"23":283400170,"24":283400170,"25":283400170,"26":283400170,"27":283400170,"28":283400170,"29":283400170,"30":283400170,"31":283400170,"32":283400170,"33":283400170,"34":283400170,"35":283400170,"36":283400170,"37":283400170,"38":283400170,"39":283400170,"40":283400170,"41":283400170,"42":283400170,"43":283400170,"44":283400170,"45":283400170,"46":283400170,"47":283400170,"48":283400170,"49":283400170,"50":283400170,"51":283400170,"52":283400170,"53":283400170,"54":283400170,"55":283400170,"56":283400170,"57":283400170,"58":283400170,"59":283400170}}
        ss = [[datetime.date(2014, 1, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 2, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 3, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 4, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 5, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 6, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 7, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 8, 1), 1.127, 0.0, 0.0],
         [datetime.date(2014, 9, 1), 1.127, 0.0, 0.0]]
        data2 = {"Date":{"0":1512086400000,"1":1514764800000},"item_cnt_month":{"0":51.0,"1":101.0}}
        mydict = {'data': data,'data2': data2,'ss': ss}
        response = requests.post(url=InterfaceTest.GRAPHED_URL,data=mydict, allow_redirects=False)
        print('/////----/////////')
        print(response.content)
        self.assertEquals(response.status_code,200)

if __name__=='__main__':
    unittest.main()