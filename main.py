from HW_hero import most_intelligence
from HW_YaD import YaUploader
import stackoverflow as st


if __name__ == "__main__":
    """
                     HomeWork with super intellectual heroes
                     body of program in HW_hero
    """
    heroes_list = ["Hulk", "Captain America", "Thanos"]
    print(most_intelligence(heroes_list))

    """
                     HomeWork with Yandex Disk
                     body of program in HW_YaD.py
    """
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "test.txt"  # Where is file
    token = "..."

    if "/" in path_to_file:
        file_name = path_to_file[path_to_file.rfind("/")+1:]
    else:
        file_name = path_to_file

    uploader = YaUploader(token)
    result = uploader.upload(file_name, path_to_file)
    print(f"HTTP code of operation is {result}")

    """
                      HomeWork with stackoverflow
                      body of program in stackoverflow.py
    """
    questions = st.get_questions()
    count = 1
    for key, val in questions.items():
        print(f"{count}) {val}" + "\n" + key + "\n")
        count += 1
