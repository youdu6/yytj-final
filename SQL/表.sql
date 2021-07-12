use football;
drop table if exists 球员;


CREATE TABLE IF NOT EXISTS `球员` (
  id int(11) NOT NULL AUTO_INCREMENT,
  名称 varchar(20) DEFAULT NULL,
  国籍 varchar(20) DEFAULT NULL,
  位置 varchar(20) DEFAULT NULL,
  速度 varchar(20) DEFAULT NULL,
  力量 varchar(20) DEFAULT NULL,
  防守 varchar(20) DEFAULT NULL,
  盘带 varchar(20) DEFAULT NULL,
  传球 varchar(20) DEFAULT NULL,
  射门 varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 ;
