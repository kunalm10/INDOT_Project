# INDOT_Project
This Repository contains modules required for INDOT project

There are 3 major files present in this module:
1. making_status_sheet_of_working_camera_links.py
2. record_multi_videos_from_rtspLinks.py
3. INDOT_CAMERA_LIST_478_20201013.xlsx


(1) and (2) uses multiprocessing Package to increase the computation speed by 800% (the CPU I was working on had 8 cores, if it has more cores the speed can be increased more)


## 1. making_status_sheet_of_working_camera_links.py
This program is made to know the stauts of the Cameras live feed, if we are able to fetch live data from camera then it will capture a snap shot of a frame from video, if we are not able to fetch live data then we don't capture anything.
The program also creates a CSV file in which we write the status of each camera with datetime stamp.

## 2. record_multi_videos_from_rtspLinks.py
This program is made to record live videos for a certain amount of time(which can be modified in the code).

## 3. INDOT_CAMERA_LIST_478_20201013.xlsx
This spreadsheet contains 5 columns: cam-id, description, longitude, latitude, and video_url.
Do not change the column headers as the same header is used in Python Scripts to read values from sheet.

### ping_camera.sh
It is a very basic code to check if camera link is working or not. Generally this file is not used in the project but it is present just in case anyone wants to use it.

### making_status_sheet_of_working_camera_links - Latest(under development).py
This code doesn't need to be used as it doesn't do what it is exactly supposed to do. I was trying to figure out a way to share variables between different process, but was not able to do it successfully. If there is a suggestion how to share variables, feel free to send a request.
