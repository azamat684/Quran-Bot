import requests



def get_quran_surahs(step, count):
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json"
    response = requests.get(url).json()
    chapters = response.get("chapters")
    data = {}
    start = (step - 1) * count 
    stop = count * step
    for chapter in chapters[start:stop]:
        data[chapter.get("name")] = chapter.get("chapter")
    return data


def get_oyatlar(chapter, index):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{chapter}.json"
    response = requests.get(url).json()
    chapter = response.get("chapter")[index - 1]
    return chapter
