# -*- coding: utf-8 -*-

from pororo import Pororo
import crawler

crawler = crawler.news_crawler("code_table.txt")
summary = Pororo(task="summary", lang="kr")

print(crawler.crawl_news("삼성전자", 5))