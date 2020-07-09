from pyowm import OWM

owm = OWM('05acfdf80fae9ce5450443646a338ad6')  # You MUST provide a valid API key
def pogoda(city):
    if not (isinstance(city,str)):
        return "Sorry, can you enter a city, not a number or smt like this"
    status="sity: "+str(city)+"\n"
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    situa = observation.weather
    temp = situa.temperature('celsius')
    status+=situa.status+"\n"
    status+="minimum: "+str(temp["temp_min"])+"\n"+"srednyaya: "+str(temp["temp"])+"\n"+"maximum: "+str(temp["temp_max"])+"\n"
    return status
