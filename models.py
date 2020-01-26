import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey,TIMESTAMP,Text,Boolean,Float,Date
from sqlalchemy.orm import relationship
import pytz


Base = declarative_base()

class Url(Base):
      __tablename__='urls'
      id = Column(Integer,primary_key=True)
      url = Column(String(255),unique=True,nullable=False)
      created_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      updated_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')),
                          onupdate=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))

      url_logs = relationship("UrlLog",backref="urls")

      def __init__(self,url):
            self.url=url
      def __repr__(self):
            return "id={0} url={1}".format(self.id,self.url)


class UrlLog(Base):
      __tablename__ = "url_logs"
      id = Column(Integer,primary_key=True)
      created_at = Column(TIMESTAMP, default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      updated_at = Column(TIMESTAMP, default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')),
                          onupdate=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      url_id = Column(Integer,ForeignKey('urls.id'))

      url = relationship("Url",uselist=False,foreign_keys=[url_id])
      file = relationship("FileDownloadLog",backref="url_logs")

      def __init__(self,url_id):
            self.url_id = url_id
      def __repr__(self):
            return "id={0} url_id={1} created_at={2}".format(self.id,self.url_id,self.created_at)


class FileDownloadLog(Base):
      __tablename__='file_download_logs'
      id = Column(Integer,primary_key=True)
      name = Column(String(255),nullable=False,unique=True)
      type = Column(String(20),nullable=False)
      created_at = Column(TIMESTAMP, default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      updated_at = Column(TIMESTAMP, default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')),
                          onupdate=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      url_log_id = Column(Integer,ForeignKey('url_logs.id'))

      url_log = relationship("UrlLog",uselist=False,foreign_keys=[url_log_id])

class ErrorLog(Base):
      __tablename__ = 'error_logs'
      id = Column(Integer,primary_key=True)
      fund_type = Column(String(255))
      details_info = Column(Text)
      is_checked = Column(Boolean,default=0)
      created_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      update_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')),
                         onupdate=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))

      def __init__(self,fundtype,details_info):
            self.fund_type = fundtype
            self.details_info=details_info

class StarCapitalScrapeUld(Base):
      __tablename__ = 'star_capital_scrape_uld'
      id = Column(Integer,primary_key=True)
      country = Column(String(70))
      weight = Column(String(70))
      cape = Column(Float)
      pe = Column(Float)
      pc = Column(Float)
      pb = Column(Float)
      ps = Column(Float)
      dy = Column(String(70))
      rs_226w = Column(Float)
      rs_52w = Column(Float)
      score = Column(Float)
      date_from_site = Column(String(70))
      timestamp = Column(TIMESTAMP)
      created_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))
      update_at = Column(TIMESTAMP,default=datetime.datetime.now(pytz.timezone('Asia/Dhaka')),
                         onupdate=datetime.datetime.now(pytz.timezone('Asia/Dhaka')))

      def __init__(self,dict):
            self.country = dict['Country']
            self.weight = dict['Weight']
            self.cape = dict['CAPE']
            self.pe = dict['PE']
            self.pc = dict['PC']
            self.pb = dict['PB']
            self.ps = dict['PS']
            self.dy = dict['DY']
            self.rs_226w = dict['RS 26W']
            self.rs_52w = dict['RS 52W']
            self.score = dict['Score']
            self.date_from_site = dict['date_from_site']
            self.timestamp = dict['timestamp']

      def __str__(self):
            return self.country

      @classmethod
      def bulk_insert(cls,df):
          objects = []
          df = df.fillna(0)
          for index, row in df.iterrows():
              objects.append(cls(row.to_dict()))
          return objects