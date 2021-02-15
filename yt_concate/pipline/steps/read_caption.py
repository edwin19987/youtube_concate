import os
from pprint import pprint
from .step import Step
from .settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}  #裝時間與字幕的字典
            with open(os.path.join(CAPTIONS_DIR,caption_file),'r') as f: #因為乎要檔案的main.py是不同資料夾要對path做處理
                # print(f)
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line=True
                        time = line.strip()
                        continue
                    if time_line: #如果time_line是true那下一行就是字幕
                        caption = line.strip()
                        captions[caption] = time  #用字幕當key的原因是: 當用forloop字典時，return的值會是key
                        time_line = False
            data[caption_file] = captions
        pprint(data)
        return data