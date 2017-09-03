import pyowm     #Импорт библиотеки pyowm

city = input ('Какой город вас интересует?: ')

owm = pyowm.OWM ('89b83544ba0c2ed1c4be507026bbb6d6')      #token учетной записи на погодном сервисе openweathermap.org
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperatura = w.get_temperature('celsius') ['temp']    
veter = w.get_wind()
vlash = w.get_humidity()
detalstat = w.get_detailed_status()
print ("В городе " + city + "," + " " + "сейчас температура: " + str (temperatura) + " " + "по Цельсию." )
print ( "Направление и скорость ветра" + " " + str (veter) )
print ("Влажность в городе" + " " + city + " " + str (vlash) )
print ( detalstat + "\n" + "На сегодня все, спасибо за пользование программы!)")

