def read_input():
    countries = input().split(", ")
    capitals = input().split(", ")
    return {countries[i]: capitals[i] for i in range(len(countries))}
 
 
def unpack_info(info):
    return [print_result(country, city) for country, city in info.items()]
 
 
def print_result(country, city):
    print(f"{country} -> {city}")
 
 
country_info = read_input()
unpack_info(country_info)