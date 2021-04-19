# INDOT_Project
This Repository contains modules required for INDOT project

There are 2 major codes present in this module:
1. making_status_sheet_of_working_camera_links.py
2. record_multi_videos_from_rtspLinks.py

Both of them uses multiprocessing Package to increase the computation speed by 800% (the CPU had 8 cores, if it has more cores the speed can be increased by more)


## 1. making_status_sheet_of_working_camera_links.py
This program is made to know the stauts of the Cameras live feed, if we are able to fetch live data from camera then it will capture a snap shot of the image, if we are not able to fetch live data then we don't capture anything.
The program also creates a CSV file in which we write the status of each camera with datetime stamp.

## 2. record_multi_videos_from_rtspLinks.py
This program is made to record live videos for a certain amount of time(which can be modified in the code).
