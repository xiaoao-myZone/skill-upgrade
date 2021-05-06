import os
import zipfile

target_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(target_path)
print(os.path.join(target_path, "python_lib.zip"))
zip_obj = zipfile.ZipFile(os.path.join(target_path, "python_lib.zip"), "w", zipfile.ZIP_DEFLATED)
print(zip_obj.namelist())
print(zip_obj.infolist())
print(zip_obj.filename)
print(zip_obj.filelist)
zip_obj.close()

def zip_log_dir(to_zip_path, filepath):
    """
    to_zip_path: dir to zip
    filepath: zip file filepath
    """
    zip_obj = zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED)
    for file_name in os.listdir(to_zip_path):
        abs_file_path = os.path.join(to_zip_path, file_name)
        if os.path.isfile(abs_file_path):
            zip_obj.write(abs_file_path.encode(), file_name)
    zip_obj.close()