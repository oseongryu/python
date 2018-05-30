#파일 기반의 SQLite과 관련하여 다음에 제시된 항목에 대하여 각각 코드를 제시하시오.

import sqlite3
#1. SQLite를 사용하기 위한 connection 객체 생성 코드
#메모리에 생성
conn = sqlite3.connect(":memory:")
#디스크에 생성
conn = sqlite3.connect("test.db")

#2. SQL 명령을 실행시키기 위한 코드
cur = conn.cursor()
cur.execute("CREATE~ , INSERT~, UPDATE~, DELETE~")

#3. 실제 DB에 반영하는 코드
conn.commit()

#4. 테이블을 생성하는 SQL 명령

cur.execute\
("""
CREATE TABLE test
(
      txt1 text
    , txt2 text
    , txt3 text
    , real1 real
    , real2 real
)
""")
#5. 데이터를 SQL로 저장하기 위한 SQL 문

cur.execute\
("""
INSERT INTO stocks
(
      txt1
    , txt2
    , txt3
    , real1
    , real2
)
VALUES
( 
      't1'
    , 't2'
    , 't3'
    , 100
    , 10000
)
""")
