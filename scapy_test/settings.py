# Scrapy settings for scapy_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scapy_test"

SPIDER_MODULES = ["scapy_test.spiders"]
NEWSPIDER_MODULE = "scapy_test.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scapy_test (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scapy_test.middlewares.ScapyTestSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scapy_test.middlewares.ScapyTestDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scapy_test.pipelines.ScapyTestPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 日志级别
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from scrapy.utils.log import configure_logging

# 动态获取日志配置
LOG_LEVEL = os.getenv('SCRAPY_LOG_LEVEL', 'INFO')
LOG_DIR = os.getenv('SCRAPY_LOG_DIR', 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = os.path.join(LOG_DIR, 'scrapy_output.log')

# 禁用 Scrapy 默认日志处理器
configure_logging(install_root_handler=False)

# 设置日志格式
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
formatter = logging.Formatter(LOG_FORMAT)

# 创建文件日志（按日期分割）
file_handler = TimedRotatingFileHandler(
    filename=LOG_FILE,
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)

# 创建控制台日志
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 配置日志记录器
logger = logging.getLogger()
logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 调整特定模块的日志级别
logging.getLogger('scrapy.downloadermiddlewares').setLevel(logging.WARNING)

# 输出文件的格式，可以是 json、jsonlines、csv、xml 等
FEED_FORMAT = "csv"

# 防止文件被覆盖，每次运行生成时间戳后缀
FEED_URI = "output/cailan_output_%(time)s.csv"
