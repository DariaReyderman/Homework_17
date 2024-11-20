# Exercise 1
info_israel = {"name": "Israel",
               "birth": 1948,
               "population_millions": 9.3,
               "capital": "Jerusalem",
               "language": "Hebrew",
               "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
               "currency": "ILS",
               "area_Kilometer": 22_145,
               "gdp_billion": 450}
print("a. The capital of Israel is", info_israel.get("capital"))
print("b. Keys", list(info_israel.keys()))
print("c. Values:", list(info_israel.values()))

print("d.")
for key, value in info_israel.items():
    print(f"Key -> {key}, Value -> {value}")

info_israel_2 = info_israel.copy()
gpd_billion = info_israel_2.pop('gdp_billion')
print("e + f", info_israel_2)

users_input = dict.fromkeys(info_israel)
for key in users_input:
    users_input[key] = input(f"{key}: ")
print("g", users_input)
print()


# Exercise 2
def length_of_last_word(s: str) -> int:
    if len(s) > 0:
        sentence = s.split()
        for word in sentence:
            if word.isalpha():
                return len(sentence[-1])
            else:
                word.replace(' ', '')
                return len(sentence[-1])


print(length_of_last_word('I love coding'))
