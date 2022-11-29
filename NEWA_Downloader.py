import pandas as pd
import wget
from datetime import timedelta, date, datetime, time


start_date = '2019-01-01'
end_date = '2019-01-03'
daterange = pd.date_range(start_date, end_date)


# for single_date in daterange:
# 	print(single_date.strftime("%Y-%m-%d"))
# 	url = 'http://opendap.neweuropeanwindatlas.eu:80/opendap/newa/NEWA_MESOSCALE_ATLAS/' + single_date.strftime("%Y") + '/NEWA-'+ single_date.strftime("%Y-%m-%d") + '.nc.nc?QVAPOR[0:1:47][0:0][555:1:974][146:1:524],PRECIP[0:1:47][555:1:974][146:1:524],SWDDIR[0:1:47][555:1:974][146:1:524],SWDDNI[0:1:47][555:1:974][146:1:524],time[0:1:47],height[0:0],west_east[146:1:524],south_north[555:1:974],XLON[555:1:974][146:1:524],XLAT[555:1:974][146:1:524],Times[0:1:47],crs'
# 	a = wget.download(url)

from urllib.request import urlopen





for single_date in daterange:
	print(single_date.strftime("%Y-%m-%d"))
	url = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXSLV.5.12.4/2019/01/MERRA2_400.tavg1_2d_slv_Nx.' + single_date.strftime("%Y%m%d") + '.nc4.nc4?U50M[0:23][280:302][269:291],V50M[0:23][280:302][269:291],lat[280:302],time[0:23],lon[269:291]'
	print(url)
	a = wget.download(url)
	# with urlopen(url) as file:
	# 	print("")


# import requests
# response = requests.get(url,verify=False, auth=('user', 'pass'))
# # print(response.text)

# with open('filename.nc','w') as fout:
#    fout.write(response.text)