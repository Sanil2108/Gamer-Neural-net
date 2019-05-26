
if __name__ == '__main__':

	import pyautogui
	import cv2
	import numpy as np
	import matplotlib.pyplot as plt
	import time
	import pynput
	from keras.models import Sequential
	from keras.layers import Dense
	from keras.optimizers import Adam
	from keras.utils.np_utils import to_categorical
	from pynput.keyboard import Key, Controller
	from pynput import keyboard as KeyBoard
	import os
	import threading

	keyThread = None

	index = 0

	TIME_WAIT = 0.016

	IMAGE_DIR = 'data/images/'
	INFO_FILE_PATH = 'data/info.csv'

	last_key = None

	f = open(INFO_FILE_PATH, 'w+')
	keyboard = Controller()

	def on_press(key):
	    try: 
	    	k = key.char
	    except: 
	    	k = key.name
	    if k in ['space']:
	        print('Key pressed: ' + k)

	def addListener():
		lis = KeyBoard.Listener(on_press=on_press)
		lis.start() 
		lis.join()

	def init(updateSignal):
		# keyThread = threading.Thread(target=addListener)
		# keyThread.start()
		lis = KeyBoard.Listener(on_press=on_press)
		lis.start() 
		# lis.join()
		
		update(updateSignal)

	def update(signal):
		global index
		global last_key

		while( not isGameOver(None)):
			time.sleep(TIME_WAIT)

			if(signal == 'RECORD'):
				image = np.array(pyautogui.screenshot())
				cv2.imwrite(os.path.join(IMAGE_DIR, '{}.png'.format(index)), image)
				f.write('{}, {}\n'.format(os.path.join(IMAGE_DIR, '{}.png'.format(index)), last_key))
				print('sample no {} done'.format(index))
				index += 1
			else:
				pass

		keyThread.join()
		
		

	# def startGame():
	# 	keyboard.press('JUMP')

	def control(signal):
	    if(signal == 'JUMP'):
	    	keyboard.press(' ')

	# def model():
	#     model = Sequential()
	#     model.add(Convolution2D(24, 5, 5, subsample=(2, 2), input_shape=(250, 1000, 1), activation='elu'))
	#     model.add(Convolution2D(36, 5, 5, subsample=(2, 2), activation='elu'))
	#     model.add(Convolution2D(48, 5, 5, subsample=(2, 2), activation='elu'))
	#     model.add(Convolution2D(64, 3, 3, activation='elu'))
	#     model.add(Convolution2D(64, 3, 3, activation='elu'))
	#     model.add(Flatten())
	#     model.add(Dense(100, activation='elu'))
	#     model.add(Dense(50, activation='elu'))
	#     model.add(Dense(10, activation='elu'))
	#     model.add(Dense(1))
	    
	#     optimizer = Adam(lr=1e-4)
	#     model.compile(loss='mse', optimizer=optimizer)
	    
	def isGameOver(frame):
	    return False

	init('RECORD')