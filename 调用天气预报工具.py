import requests
from dotenv import load_dotenv
import os

# 加载 .env 文件里的Key
load_dotenv()
AMAP_KEY = os.getenv("AMAP_KEY")

# 郴州的城市编码：431000
CITY_ADCODE = "431000"

def get_amap_weather(adcode, key):
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={key}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data["status"] != "1":
            return f"❌ 查询失败，错误信息：{data['info']}"
        
        live = data["lives"][0]
        return (
            f"\n【{live['city']} 实时天气】\n"
            f"🌤 天气状况：{live['weather']}\n"
            f"🌡 实时温度：{live['temperature']}℃\n"
            f"💨 风向风力：{live['winddirection']} {live['windpower']}级\n"
            f"💧 湿度：{live['humidity']}%\n"
            f"🕐 更新时间：{live['reporttime']}"
        )
    except Exception as e:
        return f"❌ 网络错误：{str(e)}"

if __name__ == "__main__":
    print(get_amap_weather(CITY_ADCODE, AMAP_KEY))