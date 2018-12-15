# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

class TutorialPipeline(object):
    def __init__(self):
        try:
            self.f = open('../spiders/csgo_{}.csv'.format(str(datetime.date.today())), 'a+',encoding='utf-8')
        except:
            self.f=self.f = open('../spiders/csgo_{}.csv'.format(str(datetime.date.today())), 'w+',encoding='utf-8')
        self.fields = ["name", "selling_price", "selling_date"]  # define fields to use
        # self.f.write("{}\n".format(','.join(str(field)
        #                                     for field in self.fields)))  # write header

    def process_item(self, item, spider):
        self.f.write("{}\n".format(','.join(str(item['{}'.format(field)])
                                            for field in self.fields)))  # write items

        return item
