import configparser

def get_config(cfg):
    host = cfg.get('DB', 'host'),
    user = cfg.get('DB', 'user'),
    passwd = cfg.get('DB', 'passwd'),
    db = cfg.get('DB', 'db'),
    charset = cfg.get('DB', 'charset'),
    use_unicode = cfg.getboolean('DB', 'use_unicode')
    insert_Sql = cfg.get('DB','sql_insert')


    # cfg값 출력
    print(host, user, passwd, db, charset, use_unicode,insert_Sql)


if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read("./DBInfo.conf")  # 절대주소를 적어주는게 좋다.
    get_config(cfg)
    cfg.set('DB','host','eeeee')

    # save to a file
    with open('./DBInfo.conf', 'w') as configfile:
        cfg.write(configfile)