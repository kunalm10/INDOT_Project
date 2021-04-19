import datetime, os, time
import cv2
import pyexcel as pe

from multiprocessing import Pool


def get_video(url):
    try:
        print(url)
        cap = cv2.VideoCapture(url)
        for i in range(10):
            cap.read()
        frame = cap.read()[1]
        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute
        outname = ipaddr[url] + '+' + str(datetime.date.today()) + '+' \
                  + str(hour) + '.' + str(minutes) + video_format
        out = cv2.VideoWriter(os.path.join(new_folder_name, outname), fourcc, cap.get(cv2.CAP_PROP_FPS),
                              (frame.shape[1], frame.shape[0]))
        t = time.time()
        while time.time() - t < video_length:
            print(ipaddr[url])
            print('finish %.2f' % ((time.time() - t) / video_length * 100))
            out.write(cap.read()[1])
        out.release()
        cap.release()
    except cv2.error as e:
        with open(os.path.join(new_folder_name, 'erf.csv'), 'at') as erf:
            erf.write(url + ',' + str(datetime.datetime.today()) + ',' + str(e) + '\n')
    except Exception as e:
        with open(os.path.join(new_folder_name, 'erf.csv'), 'at') as erf:
            erf.write(url + ',' + str(datetime.datetime.today()) + ',' + str(e) + '\n')


def get_videos(info_file_path):
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)
    names = dict()
    exist_count = dict()
    for i in pe.iget_records(file_name=info_file_path):
        name = str(i['description']).replace('/', '.')
        if name in exist_count:
            exist_count[name] += 1
            name += '_' + str(exist_count[name])
        else:
            exist_count[name] = 1
        names[i['video_url']] = name
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)
    return names


#  fourcc = cv2.VideoWriter_fourcc(*'XVID')
#  video_format = '.avi'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video_format = '.mp4'
video_length = 4  # seconds
# new_folder_name = 'NewVideos'
new_folder_name = 'E:\\DEC recordings check 3'
ipaddr = get_videos('INDOT_CAMERA_LIST_478_20201013.xlsx')

if __name__ == '__main__':

    pool = Pool(8)

    video_list = []
    for k in ipaddr:
        video_list.append(k)
    # for k in video_list:
    #     print(k)
    while True:
        pool.map(get_video, video_list)
