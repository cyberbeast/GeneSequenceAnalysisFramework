_author__ = 'Sandesh'

from celery import Celery
import glob
import logging
# import os

if __name__ == '__main__':
	app = Celery('d_process_task', broker='redis://192.168.6.4:6379/0', backend='redis://192.168.6.4:6379/0')

	async_result = []
	logger = logging

	# print(glob.glob(str(os.getcwd() + '/GenomeDataset/Chromosomes/*.fa')))

	# for name in glob.glob('GenomeDataset/Chromosomes/*.fa'):
	# 	# print("DoingThis")
	# 	async_result.append(app.send_task("d_process_task.process", args=(name,)))

	result_dict = {name: app.send_task("d_process_task.process", args=(name,)) for name in glob.glob('GenomeDataset/Chromosomes/*.fa')}

	for key, value in result_dict.items():
		if value.ready():
			logger.info(key + " --> " + value.get()[1])
		else:
			logger.info("waiting")
