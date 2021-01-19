import argparse
import string
import os
from string import Template


def make_exercise(competition, name):
    path = os.getcwd()
    words = []
    for word in name.split():
        new_word = word[0].upper() + word[1:]
        new_word = new_word.replace("-", "")
        words.append(new_word)

    folder_name = competition + "/" + "".join(words)
    exercise_name = "".join([c if c.isalnum() else "_" for c in name.lower()])
    function = exercise_name.replace("-", "_")
    folder_path = f"{path}/{folder_name}"
    if not os.path.exists(folder_path):
        print(f"Create {folder_path}.")
        os.mkdir(folder_path)
    else:
        print(f"Path {folder_path} already existed.")

    with open("utils/skeleton.py", "r") as f:
        file = f.read().format(exercise_name=exercise_name, function=function)
    with open(f"{folder_path}/{exercise_name}.py", "w") as f:
        f.write(file)

    with open("utils/skeleton_test.py", "r") as f:
        test_file = f.read().format(exercise_name=exercise_name, function=function)
    with open(f"{folder_path}/{exercise_name}_test.py", "w") as f:
        f.write(test_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse arguments for new exercises.")
    parser.add_argument(
        "-c", "--competition", type=str, default="Round696", help="Competition's name"
    )
    parser.add_argument("-n", "--name", type=str, help="Exercise's name.")
    args = parser.parse_args()
    make_exercise(args.competition, args.name)