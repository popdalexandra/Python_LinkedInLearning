
import requests  # pachet care nu e standard. pentru a functiona trebuie sa instalam PIP

# Pentru a nu repeta aceiasi pasi pentru fiecare oras, vom folosi clasele
class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        # apelam metoda get_data in __init__ pentru fiecare data cand instantiem un obiect 
        self.get_data()

    # creeam o metoda ce iasa si colecteaza informatii
    def get_data(self):
        # Implementam cazul in care nu exista acces la WI-FI
        try:
            # Q: Cum obtinem datele JSON in proiect?
            # A: Folosim "requests.get" pentru a iesi si obtine informatiile de la adresa URL
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=98365aac8b47ae14e786e1bdb5d4602c")
            # am adaugat in link units=metric pentru a genera corect temperatura
        except: 
            print("No internet access :( ")

        self.response_json = response.json() # variabila in care vom pastra datele JSON
        # Lucram cu obiectele din JSON
        self.temp = self.response_json ["main"]["temp"] # afisaeaza valoarea temperaturii din dictionarul cu cheia "main"
        self.temp_min = self.response_json ["main"]["temp_min"]
        self.temp_max = self.response_json ["main"]["temp_max"]

    # creeam o metoda care afiseaza datele de temperatura
    def temp_print(self):
        units_symbol = "C"
        if self.units =="imperial":
            units_symbol = "F"     

        print(f"In {self.name} it is currently {self.temp}°{units_symbol} ")
        print(f"Today's High: {self.temp_max}° {units_symbol}")
        print(f"Today's Low: {self.temp_min}° {units_symbol}")

# instanta:
my_city = City("Tokyo", 35.6762, 139.6503)
my_city.temp_print()

vacation_city = City("Portland", 45.5152, -122.6784, units="imperial")
vacation_city.temp_print()
# print(vacation_city.response_json)

local_city = City("Romania", 45.7494, 21.2272)
local_city.temp_print()
