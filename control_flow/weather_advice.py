#weather_avice.py
#prompt the user for weather input
weather = input("what's the weather like toay? (sunny/rainy/cold):").strip().lower()
#provide clothing recommendations based on input
if weather =="sunny":
    print("wear a t-shirt and sunglasses.")
elif weather =="rainy":
    print("don't forget your umbrella and a raincoat.")
elif weather =="cold":
    print("make sure to wear a warm coat and a scarf.")
else:print("sorry, i don't have recommendations for this weather")

    
