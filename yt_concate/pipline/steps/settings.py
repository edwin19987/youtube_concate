from dotenv import load_dotenv  # 讓程式到.env檔找變數
import os  # 到系統的環境變數那邊，添加API_KEY的環境變數，環境變數需要重新讀取

API_KEY = os.getenv('API_KEY')
# print(API_KEY)
load_dotenv()
