from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    session=''
    engine=''
    def __init__(self):
        # cred = 'mysql+pymysql://mehadiel_jahid_fin_bot:XonhOUzi+Ury@23.92.74.62/mehadiel_financial_bot_antonio'
        cred = 'mysql+pymysql://root:@localhost/scraping'
        self.engine = create_engine(cred, pool_recycle=3600)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
