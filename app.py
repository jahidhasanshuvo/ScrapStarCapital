from connection import Connection
from models import Base,Url,UrlLog,ErrorLog,StarCapitalScrapeUld


conn = Connection()
Base.metadata.drop_all(bind=conn.engine)
Base.metadata.create_all(bind=conn.engine)

# session = conn.session
# star_capital = StarCapitalScrapeUld(timestamp='2020-01-17-15-09-23')
# session.add(star_capital)
# print(session)
# urls = session.query(Url).first()
# print(urls)
# url = session.query(Url).first()
# print(url.url_logs[0].id)
# url_logs = [x for x in url.url_logs if x.id == 1]
# for url_log in url_logs:
#     print(url_log)

# error_log = ErrorLog("Critical Error","Database Connection refused")
# session.add(error_log)
# session.commit()
#
# error_log = session.query(ErrorLog).first()
# error_log.fund_type = "Level 1 Error"
# error_log.is_checked = 1
# session.add(error_log)
# session.commit()

# url = Url("facebook")
# session.add(url)
# session.flush()
# print(url.id)
# url_log = UrlLog(url.id)
# session.add(url_log)
# session.commit()
# urls = session.query(Url).first()
# print(urls)

# for url in urls:
#       print('id-{0} = www.{1}.com'.format(url.id,url.url))
# url = session.query(Url).filter(Url.url=='facebook').first()
# url.url = 'fb'
# session.add(url)
# session.commit()
# new_url = Url("fb")
# session.add(new_url)
# session.commit()
# print("after inserting")
# urls = session.query(Url).all()
# for url in urls:
#       print('id-{0} = www.{1}.com created at {2} updated at {3}'.format(url.id,url.url,url.created_at,url.updated_at))