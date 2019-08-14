import what3words

geocoder = what3words.Geocoder("R4IPMCP6")

res = geocoder.convert_to_coordinates('prom.caee.pump')
print(res)

res2 = geocoder.autosuggest('prom.cane.pump')
print(res2)