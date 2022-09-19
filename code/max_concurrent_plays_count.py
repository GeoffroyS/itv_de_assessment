#!/usr/bin/env python
""" Computes the the maximum number of video plays that were playing concurrently.

Accepts a collection of "plays" that follows the format below:
VideoPlay {
  startTime : an instant in time
  endTime : an instant in time
}
from a json file.
Then gets the maximum concurrent plays from this data and prints it
"""

import json

def _get_max_concurrent_plays(json_file_name):
	"""
    Gets the maximum concurrent plays
    Arguments:
        json_file_name - (str): name of the json file to use
    Returns:
        max(count_list) - (int): the maximum value of concurrent plays
    """
	data_dict = json.load(open(json_file_name))
	sorted_items = sorted(data_dict.values(), key=lambda x:x['startTime'])

	count_list = []

	# iterate through the list of sorted items
	for item in sorted_items:
		current_start_time = item['startTime']
		current_end_time   = item['endTime']

		count = 0

		# iterate through the list of sorted items again
		# to try and match each item's start/end time against the current (current loop) one
		for item2 in sorted_items:
			inner_loop_start_time, inner_loop_end_time = item2['startTime'], item2['endTime']
			# the below "optimisation" breaks off the loop as we're using a list of ordered items,
			# so if one item starts after the "current" item's end time,
			# all the following items will, too
			if inner_loop_start_time >= current_end_time:
				break
			elif inner_loop_start_time >= current_start_time and inner_loop_start_time <= current_end_time:
				count += 1
			elif inner_loop_end_time >= current_start_time and inner_loop_end_time <= current_end_time:
				count += 1

		count_list.append(count)

	return max(count_list)

def main():
	concurrent_plays = _get_max_concurrent_plays('video_play_data.json')
	print('Max concurrent plays: {}'.format(concurrent_plays))

if __name__ == '__main__':
	main()
