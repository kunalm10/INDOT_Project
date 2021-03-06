import datetime, os, time
import cv2
import pyexcel as pe
import xlsxwriter
from multiprocessing import Pool
import socket

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
all_ip_address_of_pc = socket.gethostbyname_ex(hostname)
ip_address_of_pc = socket. gethostbyname(hostname + ".local")
# ip_address_of_pc =  all_ip_address_of_pc[2][2]
# print(all_ip_address_of_pc)
# print(ip_address_of_pc)


def get_video(url):
    # To write the results in excel sheet
    with open(os.path.join(new_folder_name, 'StatusOf_ip{}_hostname{}_{}.csv'
            .format(ip_address_of_pc, hostname, datetime.datetime.now().strftime("%h-%d-%Y"))), 'at') as erf:
        try:
            print(url)
            cap = cv2.VideoCapture(url)
            success, frame = cap.read()
            hour, minutes = datetime.datetime.now().hour, datetime.datetime.now().minute
            outname = cameras_info[url][1] + '+' + cameras_info[url][0] + '+' + str(datetime.date.today()) + '+' \
                      + str(hour) + '.' + str(minutes) + image_format
            print(outname)
            if success:
                print('success')
                erf.write(cameras_info[url][1] + ',' + cameras_info[url][0] + ',' + url + ',' + str(
                    datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ',' + 'working' + '\n')
                cv2.imwrite(os.path.join(new_folder_name, outname), frame)
            else:
                print('not success')
                erf.write(cameras_info[url][1] + ',' + cameras_info[url][0] + ',' + url + ',' + str(
                    datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ',' + 'not working' + '\n')
            cap.release()

        except cv2.error as e:
            erf.write(cameras_info[url][1] + ',' + cameras_info[url][0] + ',' + url + ',' + str(
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ',' + str(e) + '\n')
        except Exception as e:
            erf.write(cameras_info[url][1] + ',' + cameras_info[url][0] + ',' + url + ',' + str(
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ',' + str(e) + '\n')


def get_rtsp_links_and_camera_names_and_camIDs(info_file_path):
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)
    rtsp_link_and_camera_names_and_camIDs = dict()

    exist_count_1 = dict()
    exist_count_2 = dict()
    for i in pe.iget_records(file_name=info_file_path):
        camera_name = str(i['description']).replace('/', '.')

        if camera_name in exist_count_1:
            exist_count_1[camera_name] += 1
            camera_name += '_' + str(exist_count_1[camera_name])
        else:
            exist_count_1[camera_name] = 1

        cam_id = str(i['cam-id'])
        if cam_id in exist_count_2:
            exist_count_2[camera_name] += 1
            camera_name += '_' + str(exist_count_2[camera_name])
        else:
            exist_count_2[camera_name] = 1

        rtsp_link_and_camera_names_and_camIDs[i['video_url']] = camera_name, cam_id

    return rtsp_link_and_camera_names_and_camIDs


image_format = '.jpg'
new_folder_name = 'CameraStatus_IP_{}_{}'.format(ip_address_of_pc, datetime.datetime.now().strftime("%h-%d-%Y_%H.%M"))
cameras_info = get_rtsp_links_and_camera_names_and_camIDs('INDOT_CAMERA_LIST_478_20201013.xlsx')
# print(cameras_info)

if __name__ == '__main__':

    # This is the line of code which generates a folder in which all the outputs will be stored.
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)
    # Making excel sheet
    with open(os.path.join(new_folder_name, 'StatusOf_ip{}_hostname{}_{}.csv'
            .format(ip_address_of_pc, hostname, datetime.datetime.now().strftime("%h-%d-%Y"))), 'at') as erf:
        erf.write('cam_id' + ',' + 'description' + ',' + 'cameras_info' + ',' + 'date_time' + ',' + 'status' + '\n')

    pool = Pool(8)

    rtsp_link_list = []
    for k in cameras_info:
        rtsp_link_list.append(k)
    # for k in video_list:
    #     print(k)

    # If user wants to make this code running for indefinite time then uncomment next 2 lines i.e. while loop, and
    # comment out 3rd line and do vic-versa if the user wants to run it just for one time i.e. go over the cameras just once

    # while True:
    #     pool.map(get_video, rtsp_link_list)
    pool.map(get_video, rtsp_link_list, chunksize=1)
