current_weather = 0
while not current_weather:
    current_weather = input("what's the weather like today? (sunny/rainy/cold): ")
    if current_weather == "sunny":
        print("wear a t-shirt and sunglasses")
    elif current_weather == "rainy":
        print("don't forget your umbrella and raincoat")
    elif current_weather == "cold":
        print("make sure to wear a warm coat and a scarf")
    else:
        print("sorry, i don't have recommendation for this weather")
    
