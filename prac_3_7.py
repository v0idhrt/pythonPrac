def build_city_country_map(country_city_list):
    city_country_map = {}

    for country_info in country_city_list:
        parts = country_info.split(':')
        country = parts[0].strip()
        cities = parts[1].strip().split(',')  

        for city in cities:
            city_country_map[city.strip()] = country 

    return city_country_map

def find_cities_in_countries(city_country_map, cities_to_query):
    results = []
    for city in cities_to_query:
        if city in city_country_map:
            results.append(f"{city} is in {city_country_map[city]}")
        else:
            results.append(f"{city} is not found")
    return results

if __name__ == "__main__":
    n = int(input("Введите количество стран и городов: "))
    country_city_list = []

    for _ in range(n):
        country_city_list.append(input("Введите страну и города (формат: страна: город1, город2): "))

    m = int(input("Введите количество запросов по городам: "))
    cities_to_query = []

    for _ in range(m):
        cities_to_query.append(input("Введите название города: "))

    city_country_map = build_city_country_map(country_city_list)

    results = find_cities_in_countries(city_country_map, cities_to_query)

    print("\nРезультаты:")
    for result in results:
        print(result)
