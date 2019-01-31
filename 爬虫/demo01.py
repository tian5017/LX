from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

# 爬取网易云音乐播放数大于500万的歌单
if __name__ == "__main__":
    url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
    # 获取浏览器驱动
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    csv_file = open("playlist.csv", "w", newline="\n", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["标题", "播放数", "链接"])

    while url != "javascript:void(0)":
        # 用webdriver加载页面
        driver.get(url)
        # 切换到内容的iframe
        driver.switch_to.frame("contentFrame")
        # 定位歌单标签
        data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
        # 解析一页中的所有歌单
        for i in range(len(data)):
            # 获取播放数
            nb = data[i].find_element_by_class_name("nb").text
            if "万" in nb and int(nb.split("万")[0]) > 500:
                # 获取播放量大于500万的歌单的封面
                msk = data[i].find_element_by_css_selector("a.msk")
                # 将数据写入csv文件
                writer.writerow([msk.get_attribute("title"), nb, msk.get_attribute("href")])
        # 找到“下一页”的链接
        url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")

    csv_file.close()





