# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import json


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["penseeltje.com"]
    start_urls = [
        "https://www.penseeltje.com/delta/shore_MTc5Mjc4_179278"
    ]

    def start_requests(self):
        # 如果需要自定义Headers，可以在这里添加
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # 尝试解析JSON数据
        try:
            data = json.loads(response.text)
            self.log("Data successfully fetched!")
        except json.JSONDecodeError:
            self.log("Failed to parse JSON")
            return

        # 保存为文件
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        self.log("Data has been saved to result.json")

        # 如果接口返回分页或其他数据，可以继续爬取
        next_page = data.get("next_page_url")
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
