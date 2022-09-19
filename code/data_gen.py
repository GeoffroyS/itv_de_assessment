#!/usr/bin/env python
""" Populates a json file with data

This script generates simple 'random' (within a calendar month) timestamps
and populates a json file with the data following the below format:

VideoPlay {
  startTime : an instant in time
  endTime : an instant in time
}
"""

from datetime import datetime, timedelta
from random import randint
import json
import os


def _get_start_end_time():
	"""
    Returns start and end times
    Arguments: /
    Returns:
        start, end: (obj, obj) the 'start' and 'end' datetime objects 
    """
	day			  = randint(1,30)
	hour		  = randint(1,23)
	minutes		  = randint(1,59)
	seconds		  = randint(1,59)
	start  		  = datetime(year=2022, month=8, day=day, hour=hour, minute=minutes, second=seconds)
	delta_minutes = randint(1,120)
	end    		  = start + timedelta(minutes=delta_minutes)
	return(start, end)

def _write_dict_to_json(output_file_name, data_dict):
	"""
	Writes the data to a json file
	Arguments:
		output_file_name - (str): output file name
		data_dict - (dict): dictionary that contains the data to write
	Returns:

	"""
	with open(output_file_name, 'w') as write_file:
		json.dump(data_dict, write_file, indent=4)
	return

def main():
	path = os.getcwd()
	output_path = '{}/sim_data/video_play_data.json'.format(path)

	video_play_dictionary = {}
	for  i in range(1,10000):
		start_time, end_time = _get_start_end_time()

		video_play_dictionary['VideoPlay{}'.format(i)]              = {}
		video_play_dictionary['VideoPlay{}'.format(i)]['startTime'] = str(start_time)
		video_play_dictionary['VideoPlay{}'.format(i)]['endTime']   = str(end_time)

	_write_dict_to_json(output_path, video_play_dictionary)

if __name__ == '__main__':
	main()