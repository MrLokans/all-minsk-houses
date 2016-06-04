import io
import os
import json


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self._file = io.open('scraped_data.json', 'w', encoding='utf-8')
        self._write_header()

    def _write_header(self):
        self._file.write(u'{"items": [\n')

    def _write_footer(self):
        self._file.write(u']}')

    def _add_last_empty_item(self):
        """This is a hack to avoid dealing with last coma in UTF files"""
        dumped_item = json.dumps({"url": "", "name": "", "houses": []})
        self._file.write(u'  ' + dumped_item + u'\n')

    def process_item(self, item, spider):
        dumped_item = json.dumps(dict(item), ensure_ascii=False)
        self._file.write(u'  ' + dumped_item + u',\n')
        return item

    def close_spider(self, spider):
        self._add_last_empty_item()
        self._write_footer()
        self._file.close()
