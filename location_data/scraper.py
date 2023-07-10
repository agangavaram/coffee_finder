import requests
import re

URL_TEMPLATES = {
    "Starbucks": "https://www.starbucks.com/store-locator?&place=",
    "Dunkin Donuts": "https://www.dunkindonuts.com/en/locations?location=",
}

ZIP_CODES = {
    "Manhattan": [i for i in range(10001, 10283)],
    "test": [10001]

}


def get_locations(place, city):
    url_temp = URL_TEMPLATES[place]

    locations = set()
    for zip in ZIP_CODES[city]:
        url_temp += str(zip)
        response = requests.get(url_temp)
        print(response.text)
    #     lat_lngs = re.findall(
    #         r'"coordinates":\{"latitude":(.*?)\,"longitude":(.*?)\}', response.text)
    #     lat_lngs = [(float(item[0]), float(item[1])) for item in lat_lngs]
    #     locations.add(lat_lngs)

    # return lat_lngs


def main():
    get_locations("Dunkin Donuts", "test")


if __name__ == "__main__":
    main()
