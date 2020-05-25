# pre-airflow-test

#### 1. Насколько похорошела Москва
##### Source
wifi_streets_rating.py

Both apidata.mos.ru API key - DATAMOS_API_KEY and GOOGLE_API_KEY
should be accessible in current user environment.

##### Run example
```bash
$ python wifi_streets_rating.py 
39 WiFi APs on the Bolshaya Gruzinskaya St
37 WiFi APs on the Narodnyy Proyezd
33 WiFi APs on the Ulitsa Mantulinskaya
28 WiFi APs on the Mit'kovskiy Proyezd
27 WiFi APs on the Andropova Ave
 
-----------------
powered by Google
```

#### 2. Статистика оказаний услуг
Oracle SQL
```SQL
select service_name
      ,count(*)
  from visit_history
 group by service_name
 order by count(*) desc
 fetch first 10 rows only;
```

#### 3. Обновление Python
```
$ python3 -V
Python 3.6.9
$ sudo apt-get update
$ sudo apt-get install --no-install-recommends python3.7
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
$ sudo update-alternatives --config python3
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.7   2         auto mode
  1            /usr/bin/python3.6   1         manual mode
  2            /usr/bin/python3.7   2         manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
$ python3 -V
Python 3.7.3
```