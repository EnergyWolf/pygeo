This is an Android app. It's a GUI for the GeoIP database by MaxMind(https://www.maxmind.com)
using the pygeoip module to access the GeoLiteCity.dat file provided by them free of charge
for developers here:
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
So a big thanks to them!

The GUI was created with the Kivy Framework(www.kivy.org)

Large apk size(17mb) is due to:
1. The GeoLiteCity.dat file, which is the actual database being queried
in the app. It's packaged into the apk and is 14mb by itself.
2. The fact that kivy basically lumps in a lot of cruft that you generally
don't need into the apk. Stuff like the entire python standard library as well
as other kivy related paraphenalia. But being able to write Android apps in Python
is worth it.
