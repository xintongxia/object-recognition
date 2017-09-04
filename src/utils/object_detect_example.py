from video_process import VideoProcess
from visualization_utils import random_bbox, draw_rect
import cv2

filename = './snowboarding.mp4'


def object_detection(frame, others):
	frame = cv2.flip(frame, 2)

	file_meta = others.get_file_meta()
	bbox = random_bbox(1, file_meta['width'], 1, file_meta['height'])
	draw_rect(frame, bbox)
	return frame


def main():
	vp = VideoProcess(file_path=filename, process_fn=object_detection)
	vp.start()
	vp.destroy()


if __name__ == '__main__':
	main()
