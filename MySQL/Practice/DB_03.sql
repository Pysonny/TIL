SELECT * FROM posts;
SHOW COLUMNS FROM posts;


# 문제 1
# 테이블 posts 를 생성하시오.
CREATE TABLE posts (
	postId INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postId)
);


# 문제 2
# 필드 정보를 보고 테이블 posts 에 새로운 필드를 추가하시오.


ALTER TABLE
	posts
ADD writer VARCHAR(100),
ADD created_at DATETIME DEFAULT CURRENT_TIMESTAMP ;


# 문제 3
# 필드 정보를 보고 필드 content 의 속성을 아래와 같이 변경하시오.


ALTER TABLE
	posts
MODIFY content TEXT ;


# 문제 4
# 테이블 posts에서 writer 필드를 삭제하시오
ALTER TABLE
	posts
DROP COLUMN
	writer;
    
    
# 문제 5
# 테이블 posts 를 삭제하시오
DROP TABLE posts;


# 문제 6 
# 테이블 posts 가 존재하지 않으면(NOT EXISTS) 테이블 posts 를 생성하시오.
CREATE TABLE IF NOT EXISTS posts (
	postId INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postId)
);


# 문제 7
# 테이블 posts 가 존재하면 (EXISTS) 테이블 posts 를 삭제하시오.

DROP TABLE IF EXISTS POSTS;