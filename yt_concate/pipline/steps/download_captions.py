import os
import time
from pytube import YouTube
from .step import Step
from .step import StepException
from .settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs,utils):  #data會接到影片連結的清單
        start = time.time()
        for url in data:
            print('download caption for ',url)
            if utils.caption_file_exist(url):
                print("found exist file")
                continue
            # download the package by:  pip install pytube
            # print(data)
            try:
                source = YouTube(url)   
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except KeyError:
                print('keyerror when downloading caption for',url)
                continue
            except AttributeError:
                print('the video does not have caption')
                continue            
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w",encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
                # break  #測試，寫完第一個就停
        end = time.time()
        print("Take: ",start-end)