import scrapy

# 单独爬取某一章的内容
class CailanSpider(scrapy.Spider):
    name = "cailan"

    allowed_domains = ["www.penseeltje.com/delta/shore_MTc5Mjc4_179278"]
    start_urls = ["https://www.penseeltje.com/delta/shore_MTc5Mjc4_179278"]

    def parse(self, response):

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

        # 保存文件
        yield {
            'title': title,
            'content': '\n'.join(content)
        }
