import os.path
import glob
import time
import shutil

error_file_image = 0
error_file_mp4 = 0
jpg_source_files = r'*.JPG'
jpg_target_folder = r'C:\Users\Haciv\OneDrive\Resimler\Go Pro Pictures'
jpg_count = 0

jpg_ = glob.glob(jpg_source_files)
for jpg_image in jpg_:
    try:
        shutil.move(jpg_image, jpg_target_folder)
        jpg_count += 1
    except shutil.Error as image_error:
        if shutil.Error:
            print(' JPG ERROR! --> {} could not moved'.format(image_error))
            error_file_image += 1


print('\n')

mp4_source_files = r'*.MP4'
mp4_target_folder = r'C:\Users\Haciv\Videos\Go Pro'
mp4_count = 0

mp4 = glob.glob(mp4_source_files)

for videos in mp4:
    try:
        shutil.move(videos, mp4_target_folder)
        mp4_count += 1
    except shutil.Error as video_error:
        if shutil.Error:
            print(' MP4 ERROR! --> {} could not moved'.format(video_error))
            error_file_mp4 += 1

print('\n')

dir_name = os.getcwd()
delete = os.listdir(dir_name)
count_LRV = 0
count_THM = 0

for item in delete:
    if item.endswith('.LRV'):
        count_LRV += 1
        os.remove(os.path.join(dir_name, item))
    if item.endswith('.THM'):
        count_THM += 1
        os.remove(os.path.join(dir_name, item))
print('\t\t** RESULTS **')
print('\n')
print('Total LRV Files Removed:', count_LRV)
print('Total THM Files Removed:', count_THM)
print('Total Videos has been moved:', mp4_count)
print('Total Pictures has been moved:', jpg_count)
print(f'\nERRORS\nImage error: {error_file_image} \nVideo error: {error_file_mp4}')

time.sleep(10)
