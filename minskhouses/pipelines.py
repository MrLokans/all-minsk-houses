import io
import json


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = io.open('scraped_data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
