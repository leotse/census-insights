from models import Session


def use_db(func):
    def inner(*args, **kwargs):
        print(*args, **kwargs)
        session = Session()
        try:
            return func(*args, **kwargs, session=session)
        except:
            session.rollback()
            raise
        finally:
            session.close()

    return inner
