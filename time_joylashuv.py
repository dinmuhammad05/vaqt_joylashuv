from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

try:
    joy_nomi = input("Joy nomini kiriting: ")

    geolocator = Nominatim(user_agent="my_time_app_dinmuhammad")
    joy = geolocator.geocode(joy_nomi)

    if joy:
        
        tf = TimezoneFinder()
        vaqt_zona_nomi = tf.timezone_at(lng=joy.longitude, lat=joy.latitude)

        if vaqt_zona_nomi:
            hozir = datetime.now(pytz.timezone(vaqt_zona_nomi))

            
            print(f"\n📍 {joy_nomi} uchun vaqt:")
            print(f"🕒 {hozir.strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"🌍 Vaqt zonasi: {vaqt_zona_nomi}")
            print(f"📌 Koordinatalar: {joy.latitude}, {joy.longitude}")
            print(f"🏙️ Manzil: {joy.address}")
            print(f"📍 Joyning kenglik va uzunligi: {joy.latitude}, {joy.longitude}")
            
        else:
            print("Vaqt zonasi aniqlanmadi.")
    else:
        print("Joy topilmadi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
