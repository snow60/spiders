import scrapy
import random
import time


# 从目录爬取整个章节的内容
class CailanThewholebookSpider(scrapy.Spider):
    name = "cailanTheWholebook"
    allowed_domains = ["www.penseeltje.com"]
    start_urls = ["https://www.penseeltje.com/knife/shore_Mjc0ODA_27480"]

    def parse(self, response):
        # 提取每个章节的链接
        chapter_links = response.xpath('//div[@id="list"]//a/@href').getall()

        chapter_links = chapter_links[9:]

        print(chapter_links)

        # 遍历每个章节链接
        for link in chapter_links:
            yield response.follow(link, self.parse_chapter)

    def parse_chapter(self, response):
        # 提取标题
        title = response.xpath('//span[@class="title"]/text()').get()

        # 提取内容
        paragraphs = response.xpath('//div[@id="chaptercontent"]/p')

        # 遍历每个 <p> 标签，提取文本内容
        content = []
        for p in paragraphs:
            # 获取段落的文本
            text = p.xpath('text()').get()
            # 确保文本非空
            if text:
                # 去除首尾空格后添加到列表中
                content.append(text.strip())

        # 随机延迟以避免被封禁
        time.sleep(random.uniform(1, 5))

        yield {
            'title': title,
            'content': '\n'.join(content),
        }
