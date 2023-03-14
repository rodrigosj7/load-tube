import os 
import re 
import moviepy.editor as mp

def convert_mp4_for_wav(path, title):
	for file in os.listdir(path):
		if re.search(title.translate(str.maketrans('','','#')), file.translate(str.maketrans('','','#'))):
			mp4_path = os.path.join(path, file)
			wav_path = os.path.join(path, os.path.splitext(file)[0]+'.wav')
			new_file = mp.AudioFileClip(mp4_path)
			new_file.write_audiofile(wav_path)
			os.remove(mp4_path)

		else:
			print("não convertido")
	return