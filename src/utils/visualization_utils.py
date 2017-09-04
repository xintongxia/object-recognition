import random
import math
import cv2

PALETTE_MAP = dict({
	'BLACK': (0, 0, 0),  # #000000 black
	'BLUE': (46, 145, 193),  # #2e91c1 blue
	'BLUE_DARK': (10, 74, 98),  # #0a4a62 dark blue
	'GRAY': (157, 157, 157),  # #9d9d9d grey
	'GREEN': (75, 171, 124),  # #4bab7c green
	'ORANGE': (236, 171, 32),  # #ecab20 orange
	'RED': (252, 67, 94),  # #fc435e red
	'RED_DARK': (131, 29, 21),  # #831d15 dark red
	'WHITE': (255, 255, 255)  # #ffffff white
})


def pick_color():
	sorted_keys = PALETTE_MAP.keys()
	rand_idx = random.randrange(len(sorted_keys))
	color_key = sorted_keys[rand_idx]
	return PALETTE_MAP[color_key]


def rand_number(min_number, max_number):
	return random.randrange(min_number, max_number)


def get_coordinates(left, right, top, bottom):
	assert left < right
	assert top < bottom
	width = right - left
	height = bottom - top

	return {
		'xmin': left + int(math.ceil(width * random.random())),
		'ymin': top + int(math.ceil(height * random.random())),
		'xmax': left + int(math.ceil(width * random.random())),
		'ymax': top + int(math.ceil(height * random.random()))
	}


def random_bboxes(count, left, right, top, bottom):
	bboxes = []
	for i in range(count):
		bboxes.append(random_bbox(left, right, top, bottom))
	return bboxes


def random_bbox(left, right, top, bottom):
	coord = get_coordinates(left, right, top, bottom)
	color = pick_color()
	return {
		'color': color,
		'top': (coord['xmin'], coord['ymin']),
		'bottom': (coord['xmax'], coord['ymax'])
	}


def draw_rect(frame, bbox):
	cv2.rectangle(frame, bbox['top'], bbox['bottom'], bbox['color'], 3)
