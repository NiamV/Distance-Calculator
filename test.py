import requests

lat1 = str(50)
lon1 = str(0)
lat2 = str(40)
lon2 = str(4)

appID = "QV50Cg9nKusKIxU0xuxn"
appCode = "MtWxs2XaYo4z_X8jc1n_9Q"


r = requests.get("https://image.maps.api.here.com/mia/1.6/mapview?poi=" + lat1 + "%2C" + lon1 + "%2C" + lat2 + "%2C" + lon2 + "&app_id=" + appID + "&app_code=" + appCode)

# image_path = tempfile.mktemp()
# open(image_path, 'wb').write(r.content)

print("https://image.maps.api.here.com/mia/1.6/mapview?poi=" + lat1 + "%2C" + lon1 + "%2C" + lat2 + "%2C" + lon2 + "&app_id=" + appID + "&app_code=" + appCode)