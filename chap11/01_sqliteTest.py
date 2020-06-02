
"""

- https://www.sqlite.org/download.html
    . Precompiled Binaries for Windows -> SQLite-tools-win32-x86-3210000.zip 다운
    . 압축 풀고 SQLite3.exe 실행


- 테이블 생성
sqlite> create table phonebook (
    name char(32),
    phone char(32),
    email char(64) primary key);

sqlite> .schema phonebook

sqlite> drop table phonebook;

- 레코드 추가
sqlite> insert into phonebook (name, phone, email) values('홍길동', '010-1111-1111', 'hkd@hong.co.kr');
sqlite> insert into phonebook (name, phone, email) values('이순신', '010-2222-2222', 'lss@lee.co.kr');
sqlite> insert into phonebook (name, phone, email) values('강감찬', '010-3333-3333', 'kkc@kang.co.kr');


- 데이터 확인
sqlite> select * from phonebook;
sqlite> select * from phonebook where name='홍길동';
sqlite> select * from phonebook where phone like '%2222%';
sqlite> select * from phonebook order by name asc;


- 데이터 수정
sqlite> update phonebook set phone='010-5555-5555', email='python@python.com' where name='강감찬';


- 데이터 삭제
sqlite> delete from phonebook where email='python@python.com';



"""