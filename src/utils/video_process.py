import cv2
import os
import sys
import time

from threading import Thread
from Queue import Queue


def get_video_meta(cap):
	if cap is None:
		return None

	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	fps = cap.get(cv2.CAP_PROP_FPS)

	return {
		'length': length,
		'width': width,
		'height': height,
		'fps': fps
	}


def get_capture(file_path):
	if not os.path.exists(file_path):
		raise IOError('file %s does not exist'.format(file_path))
	cap = cv2.VideoCapture(file_path)

	while not cap or not cap.isOpened():
		cap = cv2.VideoCapture(file_path)
		cv2.waitKey(1000)
		print 'Wait for the header'

	return cap


class VideoProcess(object):
	def __init__(self, file_path, process_fn):
		self.file_path = file_path
		self.process_fn = process_fn

		self.last_frame_pos = sys.maxint
		self.in_frame_queue = Queue()
		self.out_frame_queue = Queue()
		self.procession_thread = None
		self.cap = None

	def get_procession_thread(self):
		if self.procession_thread is not None:
			return self.procession_thread

		return Thread(
			target=self.process
		)

	def get_file_meta(self):
		if self.cap is None or not self.cap.isOpened:
			self.cap = get_capture(self.file_path)
		return get_video_meta(self.cap)

	def should_stop(self, frame_id):
		if frame_id >= self.last_frame_pos:
			return frame_id >= self.last_frame_pos

	def destroy(self):
		self.procession_thread.join()
		print ('stop processing thread.')
		if self.cap is not None:
			self.cap.release()
			print ('video captrue released.')
		cv2.destroyAllWindows()
		print ('destroy all open windows.')

	def start(self):
		self.procession_thread = self.get_procession_thread()
		# start processing thread
		self.procession_thread.start()
		# start video io process
		self.video_io()

	def frame_read(self):
		flag, frame = self.cap.read()
		# The frame is ready and already captured
		pos_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
		if frame is None:
			print ('no frames! ')
			self.last_frame_pos = pos_frame - 1
		elif flag:
			self.in_frame_queue.put((frame, pos_frame))
			print (str(pos_frame) + ' frames are read')
		else:
			pos_frame = pos_frame - 1
			# The next frame is not ready, so we try to read it again
			self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame)

			# It is better to wait for a while for the next frame to be ready
			cv2.waitKey(1000)

		if pos_frame >= self.cap.get(cv2.CAP_PROP_FRAME_COUNT):
			# If the number of captured frames is equal to the total number of frames,
			# we stop
			pos_frame = sys.maxint

		return pos_frame

	def frame_show(self):
		id = -1
		while not self.out_frame_queue.empty():
			frame, id = self.out_frame_queue.get()
			cv2.imshow('video', frame)
			cv2.waitKey(1)
			print (str(id) + ' frames are shown.')
		return id

	def process(self):
		id = 0
		while True:
			if self.should_stop(id):
				print ('all frames are processed')
				break
			if self.in_frame_queue.empty():
				time.sleep(1)
			else:
				in_frame, id = self.in_frame_queue.get()
				out_frame = self.process_fn(in_frame, self)
				self.out_frame_queue.put((out_frame, id))
				print (str(id) + ' frames are processed.')

	def video_io(self):
		if not self.cap or not self.cap.isOpened:
			self.cap = get_capture(self.file_path)

		in_frame_id = 0
		while True:
			if not self.should_stop(in_frame_id):
				in_frame_id = self.frame_read()
			out_frame_id = self.frame_show()
			if self.should_stop(out_frame_id):
				print ('all frames are shown!')
				break
