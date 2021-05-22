import os
import json


main_path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3])
print(main_path)
with open(os.path.join(main_path, "my_heap/hot_import.json"), "r") as f:
    data = f.read()
    # print(data)
