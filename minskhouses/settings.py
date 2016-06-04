BOT_NAME = 'minskhousesspider'

SPIDER_MODULES = ['minskhouses.spiders']
NEWSPIDER_MODULE = 'minskhouses.spiders'

ITEM_PIPELINES = ['minskhouses.pipelines.JsonWithEncodingPipeline']
