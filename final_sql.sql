-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: lolin
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api_key`
--

DROP TABLE IF EXISTS `api_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_key` (
  `admin` varchar(100) NOT NULL DEFAULT '0',
  `api_key` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_key`
--

LOCK TABLES `api_key` WRITE;
/*!40000 ALTER TABLE `api_key` DISABLE KEYS */;
INSERT INTO `api_key` VALUES ('admin','RGAPI-d774b00f-1ecd-445d-af8b-3779cfd14429');
/*!40000 ALTER TABLE `api_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_pre`
--

DROP TABLE IF EXISTS `auth_pre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_pre` (
  `nick_name` varchar(100) NOT NULL,
  `img_number` int DEFAULT NULL,
  PRIMARY KEY (`nick_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_pre`
--

LOCK TABLES `auth_pre` WRITE;
/*!40000 ALTER TABLE `auth_pre` DISABLE KEYS */;
INSERT INTO `auth_pre` VALUES ('',10),('%EB%82%98%EB%8A%94%EC%A6%90%EA%B2%9C%EB%9F%AC%EB%8B%B9',8),('dddd',17),('hide on bush',-1),('JSDD SUL',-1),('JSDDSUL',20),('개구리꾀꼬닥',-1),('개불김',-1),('굿또',-1),('꼬마자동차 붕봉',-1),('꼬마자동차봉',3),('꼬마자동차봉봉',18),('꼬마자동차붕봉',14),('나는즐겜러당',-1),('데롱디롱',-1),('숏다리의 꿈',-1),('숏다리의꿈',16),('실버맨',-1),('평양산검은콩',-1);
/*!40000 ALTER TABLE `auth_pre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bangJangList`
--

DROP TABLE IF EXISTS `bangJangList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bangJangList` (
  `room_no` int NOT NULL AUTO_INCREMENT,
  `id` varchar(100) DEFAULT NULL,
  `nick_name` varchar(100) DEFAULT NULL,
  `room_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bangJangList`
--

LOCK TABLES `bangJangList` WRITE;
/*!40000 ALTER TABLE `bangJangList` DISABLE KEYS */;
/*!40000 ALTER TABLE `bangJangList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bangjanglist`
--

DROP TABLE IF EXISTS `bangjanglist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bangjanglist` (
  `room_no` int NOT NULL AUTO_INCREMENT,
  `id` varchar(100) DEFAULT NULL,
  `nick_name` varchar(100) DEFAULT NULL,
  `room_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`room_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bangjanglist`
--

LOCK TABLES `bangjanglist` WRITE;
/*!40000 ALTER TABLE `bangjanglist` DISABLE KEYS */;
INSERT INTO `bangjanglist` VALUES (1,'ybj0749','나는즐겜러당','소환사의협곡승리'),(4,'ybj0749','나는즐겜러당','새로운협곡'),(5,'dyyyyw','평양산검은콩','가자가자'),(6,'dyyyyw','평양산검은콩','바람바람칼바람'),(7,'ldkgang','JSDD SUL','A104 화이팅'),(8,'dyyyyw','평양산검은콩','정신차려');
/*!40000 ALTER TABLE `bangjanglist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatroom`
--

DROP TABLE IF EXISTS `chatroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chatroom` (
  `room_no` int DEFAULT NULL,
  `room_name` varchar(100) DEFAULT NULL,
  `id` varchar(100) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nick_name` varchar(100) DEFAULT NULL,
  `message_data` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatroom`
--

LOCK TABLES `chatroom` WRITE;
/*!40000 ALTER TABLE `chatroom` DISABLE KEYS */;
INSERT INTO `chatroom` VALUES (1,'소환사의협곡','ybj0749','2021-03-23 00:26:56','나는즐겜러당','메세지보내기!!!!!'),(1,'소환사의협곡','ybj0749','2021-03-23 00:27:05','나는즐겜러당','메세지보내기!!!!!'),(1,'소환사의협곡','otherID','2021-03-23 00:27:21','너는즐겜러','메세지보내기!!!!!'),(1,NULL,'helloworld','2021-03-23 00:35:16',NULL,'가나다라마바사아차타카타파'),(1,'소환사의협곡승리','helloworld','2021-03-23 01:06:52',NULL,'가나다라마바사아차타카타파'),(1,'소환사의협곡승리','ybj0749','2021-03-23 01:07:22','나는즐겜러당','가나다라마바사아차타카타파'),(6,'바람바람칼바람','dyyyyw','2021-04-06 20:33:51','평양산검은콩','람바칼'),(6,'바람바람칼바람','dyyyyw','2021-04-06 20:33:53','평양산검은콩','람바칼'),(5,'가자가자','dyyyyw','2021-04-06 21:07:01','평양산검은콩','가자 본선으로'),(5,'가자가자','dyyyyw','2021-04-06 21:09:19','평양산검은콩','가자 울산으로'),(5,'가자가자','giga1615','2021-04-06 06:15:16','데롱디롱','가자 침대로'),(1,'소환사의협곡','dyyyyw','2021-04-06 06:15:16','평양산검은콩','오호호호이ㅣ이'),(5,'가자가자','dyyyyw','2021-04-07 06:51:55','평양산검은콩','앗'),(5,'가자가자','dyyyyw','2021-04-07 06:51:56','평양산검은콩','느린디 ?'),(5,'가자가자','giga1615','2021-04-07 06:53:12','데롱디롱','어..'),(5,'가자가자','giga1615','2021-04-07 06:53:19','데롱디롱','근데 나도 좀 렉걸려'),(5,'가자가자','dyyyyw','2021-04-07 06:53:20','평양산검은콩','그치..'),(5,'가자가자','giga1615','2021-04-07 06:53:26','데롱디롱','오호... 신기해신기해'),(5,'가자가자','dyyyyw','2021-04-07 06:53:28','평양산검은콩','신기해..!!'),(5,'가자가자','dyyyyw','2021-04-07 06:53:39','평양산검은콩','데롱디롱 ~~~><'),(5,'가자가자','giga1615','2021-04-07 07:04:50','데롱디롱','나와라~~~'),(5,'가자가자','giga1615','2021-04-07 07:04:59','데롱디롱','오오오'),(5,'가자가자','hossi','2021-04-07 07:05:03','꼬마자동차 붕봉','안녕하세요'),(5,'가자가자','dyyyyw','2021-04-07 07:05:10','평양산검은콩','안녕하슈'),(5,'가자가자','giga1615','2021-04-07 07:05:12','데롱디롱','방가방가~'),(5,'가자가자','dyyyyw','2021-04-07 07:05:22','평양산검은콩','방가룽'),(5,'가자가자','giga1615','2021-04-07 07:05:23','데롱디롱','갠춘갠춘'),(5,'가자가자','hossi','2021-04-07 07:05:33','꼬마자동차 붕봉','가위바위보 합시다'),(5,'가자가자','hossi','2021-04-07 07:05:35','꼬마자동차 붕봉','3333333333333333'),(5,'가자가자','hossi','2021-04-07 07:05:39','꼬마자동차 붕봉','222222222222222'),(5,'가자가자','hossi','2021-04-07 07:05:41','꼬마자동차 붕봉','11111111111111111'),(5,'가자가자','hossi','2021-04-07 07:05:45','꼬마자동차 붕봉','묵'),(5,'가자가자','giga1615','2021-04-07 07:05:46','데롱디롱','바위'),(5,'가자가자','dyyyyw','2021-04-07 07:05:58','평양산검은콩','가위'),(5,'가자가자','giga1615','2021-04-07 07:06:21','데롱디롱','가위'),(5,'가자가자','hossi','2021-04-07 07:06:21','꼬마자동차 붕봉','묵'),(5,'가자가자','dyyyyw','2021-04-07 07:06:22','평양산검은콩','바위'),(5,'가자가자','dyyyyw','2021-04-07 13:36:51','평양산검은콩','보내지나'),(5,'가자가자','hossi','2021-04-07 13:36:55','꼬마자동차 붕봉','아'),(5,'가자가자','giga1615','2021-04-08 01:27:41','데롱디롱','나는나는?'),(7,'A104 화이팅','ldkgang','2021-04-08 06:07:45','JSDD SUL','화이팅');
/*!40000 ALTER TABLE `chatroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connection`
--

DROP TABLE IF EXISTS `connection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `connection` (
  `id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `my_nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  `connection_check` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connection`
--

LOCK TABLES `connection` WRITE;
/*!40000 ALTER TABLE `connection` DISABLE KEYS */;
INSERT INTO `connection` VALUES ('0','담원 토스트102',0),('1','돌 곰103',0),('10','산뜻한아침햇살112',0),('100','인싸202',0),('101','존잘러203',0),('102','곰스204',0),('103','바운스205',0),('104','뚱이206',0),('105','복서207',0),('106','해충박멸208',0),('107','디스코드209',0),('108','후라이팬210',0),('109','존버211',0),('11','새벽별비처럼113',0),('110','꿀꿀이212',0),('111','나쵸213',0),('112','너구리214',0),('113','아몬드215',0),('114','땅콩216',0),('115','치즈217',0),('116','호떡218',0),('117','만두219',0),('118','대파220',0),('119','부엉이221',0),('12','아수라발탁114',0),('120','프로222',0),('121','록맨223',0),('122','호구맨224',0),('123','레이저225',0),('124','고독226',0),('125','저격227',0),('126','달님228',0),('127','더힐229',0),('128','놀고있네230',0),('129','프리미어231',0),('13','안뇨옹 핑핑아115',0),('130','메이트232',0),('131','바른마음233',0),('132','백구234',0),('133','잇츠235',0),('134','아메리카노236',0),('135','고고고고237',0),('136','오렌지피클238',0),('137','땡땡이239',0),('138','월계수240',0),('139','라이트241',0),('14','암쁘럼인디왕116',0),('140','테슬라242',0),('141','실루엣243',0),('142','시계244',0),('143','레전드245',0),('144','결정246',0),('145','시즌247',0),('146','뉴비248',0),('147','버드249',0),('148','열차250',0),('149','다이아몬드251',0),('15','야채 그 자체117',0),('150','전기피카츄252',0),('151','윈디감옥253',0),('152','빌런맨254',0),('153','데빌255',0),('154','바이바이256',0),('155','호시탐탐257',0),('156','레이븐258',0),('157','세트259',0),('158','물범260',0),('159','극비261',0),('16','얼탱구리없네118',0),('160','다이어트262',0),('161','풀피263',0),('162','레나264',0),('163','야채265',0),('164','푸른점266',0),('165','푸른곰팡이267',0),('166','청둥오리268',0),('167','아이스크림269',0),('168','대나무270',0),('169','바이올린271',0),('17','에바쌔119',0),('170','바이올렛272',0),('171','인터스텔라273',0),('172','팽이274',0),('173','토템275',0),('174','나나276',0),('175','보라돌이277',0),('176','뚜비278',0),('177','뽀오279',0),('178','악어새280',0),('179','마법전사281',0),('18','원거리개조심120',0),('180','나무늘보282',0),('181','범고래283',0),('182','고래밥284',0),('183','마라치킨285',0),('184','사파리286',0),('185','비둘기287',0),('186','포카리스웨트288',0),('187','차이나팜289',0),('188','파머빵290',0),('189','단판빵을291',0),('19','이게 나야 빠끄121',0),('190','다비켜라제발292',0),('191','나는슈퍼원더풀293',0),('192','딜러자동차294',0),('193','뭘파는건데295',0),('194','왜그러는데296',0),('195','뭐하는건데297',0),('196','아진짜이거298',0),('197','언제까지299',0),('198','다하는건가300',0),('199','과연나는301',0),('2','뚜익이104',0),('20','이게 나얌 빠끄122',0),('200','오늘어떤302',0),('201','아이디를303',0),('202','받을까소음304',0),('203','야간대장305',0),('204','절약모드306',0),('205','아바타307',0),('206','우유308',0),('207','커피309',0),('208','모카310',0),('209','초코311',0),('21','장용은123',0),('210','브라우니312',0),('211','댕댕이313',0),('212','삐삐314',0),('213','뚠뚠315',0),('214','강냉이316',0),('215','잠만보317',0),('216','안드로메다318',0),('217','프라하319',0),('218','고인물320',0),('219','갑분싸321',0),('22','재호회계연습124',0),('220','인싸322',0),('221','존잘러323',0),('222','곰스324',0),('223','바운스325',0),('224','뚱이326',0),('225','복서327',0),('226','해충박멸328',0),('227','디스코드329',0),('228','후라이팬330',0),('229','존버331',0),('23','저는버러지125',0),('230','꿀꿀이332',0),('231','나쵸333',0),('232','너구리334',0),('233','아몬드335',0),('234','땅콩336',0),('235','치즈337',0),('236','호떡338',0),('237','만두339',0),('238','대파340',0),('239','부엉이341',0),('24','좋아하고 잘해요126',0),('240','프로342',0),('241','록맨343',0),('242','호구맨344',0),('243','레이저345',0),('244','고독346',0),('245','저격347',0),('246','달님348',0),('247','더힐349',0),('248','놀고있네350',0),('249','프리미어351',0),('25','준규석규앙규127',0),('250','메이트352',0),('251','바른마음353',0),('252','백구354',0),('253','잇츠355',0),('254','아메리카노356',0),('255','고고고고357',0),('256','오렌지피클358',0),('257','땡땡이359',0),('258','월계수360',0),('259','라이트361',0),('26','짓짓짓128',0),('260','테슬라362',0),('261','실루엣363',0),('262','시계364',0),('263','레전드365',0),('264','결정366',0),('265','시즌367',0),('266','뉴비368',0),('267','버드369',0),('268','열차370',0),('269','다이아몬드371',0),('27','촉수 있는 곳이129',0),('270','전기피카츄372',0),('271','윈디감옥373',0),('272','빌런맨374',0),('273','데빌375',0),('274','바이바이376',0),('275','호시탐탐377',0),('276','레이븐378',0),('277','세트379',0),('278','물범380',0),('279','극비381',0),('28','최배다르130',0),('280','다이어트382',0),('281','풀피383',0),('282','레나384',0),('283','야채385',0),('284','푸른점386',0),('285','푸른곰팡이387',0),('286','청둥오리388',0),('287','아이스크림389',0),('288','대나무390',0),('289','바이올린391',0),('29','치킨에진심인사람131',0),('290','바이올렛392',0),('291','인터스텔라393',0),('292','팽이394',0),('293','토템395',0),('294','나나396',0),('295','보라돌이397',0),('296','뚜비398',0),('297','뽀오399',0),('298','악어새400',0),('299','마법전사401',0),('3','띵찬이다105',0),('30','킬각아니당132',0),('300','나무늘보402',0),('301','범고래403',0),('302','고래밥404',0),('303','마라치킨405',0),('304','사파리406',0),('305','비둘기407',0),('306','포카리스웨트408',0),('307','차이나팜409',0),('308','파머빵410',0),('309','단판빵을411',0),('31','하마의심장133',0),('310','다비켜라제발412',0),('311','나는슈퍼원더풀413',0),('312','딜러자동차414',0),('313','뭘파는건데415',0),('314','왜그러는데416',0),('315','뭐하는건데417',0),('316','아진짜이거418',0),('317','언제까지419',0),('318','다하는건가420',0),('319','과연나는421',0),('32','하필그날134',0),('320','오늘어떤422',0),('321','아이디를423',0),('322','받을까소음424',0),('323','야간대장425',0),('324','절약모드426',0),('325','아바타427',0),('326','우유428',0),('327','커피429',0),('328','모카430',0),('329','초코431',0),('33','행복은 퇴사순135',0),('330','브라우니432',0),('331','댕댕이433',0),('332','삐삐434',0),('333','뚠뚠435',0),('334','강냉이436',0),('335','잠만보437',0),('336','안드로메다438',0),('337','프라하439',0),('338','고인물440',0),('339','갑분싸441',0),('34','히포의심장136',0),('340','인싸442',0),('341','존잘러443',0),('342','곰스444',0),('343','바운스445',0),('344','뚱이446',0),('345','복서447',0),('346','해충박멸448',0),('347','디스코드449',0),('348','후라이팬450',0),('349','존버451',0),('35','JSDD KUK137',0),('350','꿀꿀이452',0),('351','나쵸453',0),('352','너구리454',0),('353','아몬드455',0),('354','땅콩456',0),('355','치즈457',0),('356','호떡458',0),('357','만두459',0),('358','대파460',0),('359','부엉이461',0),('36','JSDD BOB138',0),('360','프로462',0),('361','록맨463',0),('362','호구맨464',0),('363','레이저465',0),('364','고독466',0),('365','저격467',0),('366','달님468',0),('367','더힐469',0),('368','놀고있네470',0),('369','프리미어471',0),('37','심ba139',0),('370','메이트472',0),('371','바른마음473',0),('372','백구474',0),('373','잇츠475',0),('374','아메리카노476',0),('375','고고고고477',0),('376','오렌지피클478',0),('377','땡땡이479',0),('378','월계수480',0),('379','라이트481',0),('38','말만 그 자체140',0),('380','테슬라482',0),('381','실루엣483',0),('382','시계484',0),('383','레전드485',0),('384','결정486',0),('385','시즌487',0),('386','뉴비488',0),('387','버드489',0),('388','열차490',0),('389','다이아몬드491',0),('39','또띠 그 자체141',0),('390','전기피카츄492',0),('391','윈디감옥493',0),('392','빌런맨494',0),('393','데빌495',0),('394','바이바이496',0),('395','호시탐탐497',0),('396','레이븐498',0),('397','세트499',0),('398','물범500',0),('399','극비501',0),('4','물빵왕106',0),('40','민래기142',0),('400','다이어트502',0),('401','풀피503',0),('402','레나504',0),('403','야채505',0),('404','푸른점506',0),('405','푸른곰팡이507',0),('406','청둥오리508',0),('407','아이스크림509',0),('408','대나무510',0),('409','바이올린511',0),('41','지 흐 운143',0),('410','바이올렛512',0),('411','인터스텔라513',0),('412','팽이514',0),('413','토템515',0),('414','나나516',0),('415','보라돌이517',0),('416','뚜비518',0),('417','뽀오519',0),('418','악어새520',0),('419','마법전사521',0),('42','Gfriendly144',0),('420','나무늘보522',0),('421','범고래523',0),('422','고래밥524',0),('423','마라치킨525',0),('424','사파리526',0),('425','비둘기527',0),('426','포카리스웨트528',0),('427','차이나팜529',0),('428','파머빵530',0),('429','단판빵을531',0),('43','첫 번째 행운145',0),('430','다비켜라제발532',0),('431','나는슈퍼원더풀533',0),('432','딜러자동차534',0),('433','뭘파는건데535',0),('434','왜그러는데536',0),('435','뭐하는건데537',0),('436','아진짜이거538',0),('437','언제까지539',0),('438','다하는건가540',0),('439','과연나는541',0),('44','버섯 그 자체146',0),('440','오늘어떤542',0),('441','아이디를543',0),('442','받을까소음544',0),('443','야간대장545',0),('444','절약모드546',0),('445','아바타547',0),('446','우유548',0),('447','커피549',0),('448','모카550',0),('449','초코551',0),('45','꽃보다 엔딩147',0),('450','브라우니552',0),('451','댕댕이553',0),('452','삐삐554',0),('453','뚠뚠555',0),('454','강냉이556',0),('455','잠만보557',0),('456','안드로메다558',0),('457','프라하559',0),('458','고인물560',0),('459','갑분싸561',0),('46','김진우 화이팅148',0),('460','인싸562',0),('461','존잘러563',0),('462','곰스564',0),('463','바운스565',0),('464','뚱이566',0),('465','복서567',0),('466','해충박멸568',0),('467','디스코드569',0),('468','후라이팬570',0),('469','존버571',0),('47','자취하는여자149',0),('470','꿀꿀이572',0),('471','나쵸573',0),('472','너구리574',0),('473','아몬드575',0),('474','땅콩576',0),('475','치즈577',0),('476','호떡578',0),('477','만두579',0),('478','대파580',0),('479','부엉이581',0),('48','윤영의십돼지년150',0),('480','프로582',0),('481','록맨583',0),('482','호구맨584',0),('483','레이저585',0),('484','고독586',0),('485','저격587',0),('486','달님588',0),('487','더힐589',0),('488','놀고있네590',0),('489','프리미어591',0),('49','모스맘151',0),('490','메이트592',0),('491','바른마음593',0),('492','백구594',0),('493','잇츠595',0),('494','아메리카노596',0),('495','고고고고597',0),('496','오렌지피클598',0),('497','땡땡이599',0),('498','월계수600',0),('499','라이트601',0),('5','방패왕107',0),('50','귀살대 김성회152',0),('500','테슬라602',0),('501','실루엣603',0),('502','시계604',0),('503','레전드605',0),('504','결정606',0),('505','시즌607',0),('506','뉴비608',0),('507','버드609',0),('508','열차610',0),('509','다이아몬드611',0),('51','상현 1 정민우153',0),('510','전기피카츄612',0),('511','윈디감옥613',0),('512','빌런맨614',0),('513','데빌615',0),('514','바이바이616',0),('515','호시탐탐617',0),('516','레이븐618',0),('517','세트619',0),('518','물범620',0),('519','극비621',0),('52','한권으로끝내기N3154',0),('520','다이어트622',0),('521','풀피623',0),('522','레나624',0),('523','야채625',0),('524','푸른점626',0),('525','푸른곰팡이627',0),('526','청둥오리628',0),('527','아이스크림629',0),('528','대나무630',0),('529','바이올린631',0),('53','실세폰돌남155',0),('530','바이올렛632',0),('531','인터스텔라633',0),('532','팽이634',0),('533','토템635',0),('534','나나636',0),('535','보라돌이637',0),('536','뚜비638',0),('537','뽀오639',0),('538','악어새640',0),('539','마법전사641',0),('54','내무조156',0),('540','나무늘보642',0),('541','범고래643',0),('542','고래밥644',0),('543','마라치킨645',0),('544','사파리646',0),('545','비둘기647',0),('546','포카리스웨트648',0),('547','차이나팜649',0),('548','파머빵650',0),('549','단판빵을651',0),('55','필리핀황금여행157',0),('550','다비켜라제발652',0),('551','나는슈퍼원더풀653',0),('552','딜러자동차654',0),('553','뭘파는건데655',0),('554','왜그러는데656',0),('555','뭐하는건데657',0),('556','아진짜이거658',0),('557','언제까지659',0),('558','다하는건가660',0),('559','과연나는661',0),('56','왜자꾸잉잉거려잉158',0),('560','오늘어떤662',0),('561','아이디를663',0),('562','받을까소음664',0),('563','야간대장665',0),('564','절약모드666',0),('566','가가대소669',0),('567','가가문전670',0),('568','가가호호671',0),('569','가감지인672',0),('57','나는 죽은 사람159',0),('570','가거지지673',0),('571','가고문적674',0),('572','가고문헌675',0),('573','가공가소676',0),('574','가공망상677',0),('575','가급678',0),('576','인족679',0),('577','가관680',0),('578','가담681',0),('579','항설682',0),('58','기운기호랑이범160',0),('580','가담 항어683',0),('581','항 어684',0),('582','가돈685',0),('583','가동 가서686',0),('584','가 서687',0),('585','가동 주졸688',0),('586','주졸689',0),('587','가렴주구690',0),('588','가롱성진691',0),('589','가릉빈가692',0),('59','핫떼떼161',0),('590','가무음곡693',0),('591','가문설화694',0),('592','설화695',0),('593','음 곡696',0),('594','가 신697',0),('595','가신지인698',0),('596','감 이699',0),('597','수통700',0),('598','감정 선갈701',0),('599','감탄고토702',0),('5ujin','개구리꾀꼬닥',1),('6','버섯던지자108',0),('60','GRRRRkakkak162',0),('600','내친구꼬마자동차703',0),('601','꼬마자동차704',0),('602','강 류705',0),('603','석부전706',0),('604','강 목707',0),('605','수생708',0),('606','개 시709',0),('607','귀 류710',0),('608','갱무도리711',0),('609','부릎뜨니숲이였어712',0),('61','neque163',0),('610','월화술먹구토일713',0),('611','옥수수 콧수염차714',0),('612','찰옥수수 수염차715',0),('613','진관홀 왕돈가스716',0),('614','누리관 왕돈까스717',0),('615','누리관 대왕만두718',0),('616','누리관 해물라면 719',0),('617','혜당관 컵밥720',0),('618','바롬관 학식 맛없다721',0),('619','란닝맨722',0),('62','레이디가가렌164',0),('620','광개토관723',0),('621','모짜르트홀724',0),('622','영실관725',0),('623','세종관726',0),('624','원자력 발사727',0),('625','전자전자 왕전자728',0),('626','혜당관 왕만두729',0),('627','혜당관 김치만두730',0),('628','바롬관 육회비빔밥731',0),('629','세종관 사무실732',0),('63','맛있는오레오165',0),('630','꾸마 자동차733',0),('631','꼬마 비행기734',0),('632','꼬마꼬마 왕꼬마735',0),('633','레오날두736',0),('634','크리수티아누 후날두737',0),('635','리오넬 몇시야738',0),('636','앨릭스 니아코739',0),('637','조 두두740',0),('638','까비 드릴조741',0),('639','디그디그 디그다742',0),('64','서니느166',0),('640','니 램프티743',0),('641','존 멘사744',0),('642','제프 시룹745',0),('643','조르당 아유746',0),('644','등짝 스매싱747',0),('645','미드미드트롤748',0),('646','메롱메롱퍼블749',0),('647','숲속에 바론왕750',0),('648','블링블링 왕블링751',0),('649','부푸러 콜라맛752',0),('65','운암사 철중스님167',0),('650','꼬북좌753',0),('651','메보좌754',0),('652','단발좌755',0),('653','왕눈좌756',0),('654','노원구 비둘기757',0),('655','상계동 비둘기아빠758',0),('656','노원구 맛집759',0),('657','빅데이터 전문가760',0),('658','계양구 맛집761',0),('659','가경자762',0),('66','작은집토토로168',0),('660','가는보라색우무763',0),('661','가는쑥부쟁이764',0),('662','가는잎벚나무765',0),('663','가두배추766',0),('664','가라767',0),('665','가락풀768',0),('666','가랑잎769',0),('667','가막살나무770',0),('668','가문비771',0),('669','가새잎머루772',0),('67','햇썽이169',0),('670','가시나무773',0),('671','가시비름774',0),('672','가을배추775',0),('673','가죽나무776',0),('674','가 지777',0),('675','각시붓꽃778',0),('676','감 람779',0),('677','감 자780',0),('678','감 당781',0),('679','감 저782',0),('68','aqq170',0),('680','강원 고사리783',0),('681','개 과784',0),('682','개나리꽃785',0),('683','개양귀비786',0),('684','바닐라 와플787',0),('685','abc 초콜렛마트788',0),('69','c1 혁이171',0),('7','벚꽃냐무109',0),('70','ztzt123172',0),('71','가자 리뽀카로173',0),('72','가자 페카도로174',0),('73','갓 tak175',0),('74','갓 자윤176',0),('75','개소리하면걍박음177',0),('76','곱쓰리178',0),('77','광대인생179',0),('78','광희사우르스180',0),('79','김준이이181',0),('8','블라블라블라썸110',0),('80','끌레드르182',0),('81','닭발에진심인사람183',0),('82','아바타184',0),('83','우유185',0),('84','커피186',0),('85','모카187',0),('86','초코188',0),('87','브라우니189',0),('88','댕댕이190',0),('89','삐삐191',0),('9','사랑했다행복해라111',0),('90','뚠뚠192',0),('91','강냉이193',0),('92','삐삐194',0),('93','뚠뚠195',0),('94','강냉이196',0),('95','잠만보197',0),('96','안드로메다198',0),('97','프라하199',0),('98','고인물200',0),('99','갑분싸201',0),('checkID','실버맨',0),('dayun0','굿또',0),('dyyyyw','평양산검은콩',0),('giga1615','숏다리의 꿈',1),('hossi','꼬마자동차 붕봉',1),('ldkgang','JSDD SUL',1),('wogns0','개불김',1),('ybj0749','나는즐겜러당',1);
/*!40000 ALTER TABLE `connection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-03 20:20:36.749815'),(2,'auth','0001_initial','2021-04-03 20:20:36.983988'),(3,'admin','0001_initial','2021-04-03 20:20:37.552267'),(4,'admin','0002_logentry_remove_auto_add','2021-04-03 20:20:37.890417'),(5,'admin','0003_logentry_add_action_flag_choices','2021-04-03 20:20:37.900411'),(6,'contenttypes','0002_remove_content_type_name','2021-04-03 20:20:38.017873'),(7,'auth','0002_alter_permission_name_max_length','2021-04-03 20:20:38.088639'),(8,'auth','0003_alter_user_email_max_length','2021-04-03 20:20:38.113992'),(9,'auth','0004_alter_user_username_opts','2021-04-03 20:20:38.122778'),(10,'auth','0005_alter_user_last_login_null','2021-04-03 20:20:38.191887'),(11,'auth','0006_require_contenttypes_0002','2021-04-03 20:20:38.199536'),(12,'auth','0007_alter_validators_add_error_messages','2021-04-03 20:20:38.212729'),(13,'auth','0008_alter_user_username_max_length','2021-04-03 20:20:38.289370'),(14,'auth','0009_alter_user_last_name_max_length','2021-04-03 20:20:38.361583'),(15,'auth','0010_alter_group_name_max_length','2021-04-03 20:20:38.383464'),(16,'auth','0011_update_proxy_permissions','2021-04-03 20:20:38.393289'),(17,'auth','0012_alter_user_first_name_max_length','2021-04-03 20:20:38.469738'),(18,'sessions','0001_initial','2021-04-03 20:20:38.500581');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dm`
--

DROP TABLE IF EXISTS `dm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dm` (
  `dm_no` int NOT NULL AUTO_INCREMENT,
  `my_id` varchar(100) DEFAULT NULL,
  `your_id` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `my_nickname` varchar(100) DEFAULT NULL,
  `your_nickname` varchar(100) DEFAULT NULL,
  `message_data` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`dm_no`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dm`
--

LOCK TABLES `dm` WRITE;
/*!40000 ALTER TABLE `dm` DISABLE KEYS */;
INSERT INTO `dm` VALUES (1,'ybj0749','ybj2463','2021-03-24 10:25:49','나는즐겜러당','너는즐겜러','dm보내보'),(4,'dyyyyw','giga1615','2021-04-07 13:39:14','평양산검은콩','데롱디롱','새채팅'),(5,'dyyyyw','giga1615','2021-04-07 13:57:28','평양산검은콩','데롱디롱','허억 !'),(6,'dyyyyw','giga1615','2021-04-07 13:57:36','평양산검은콩','데롱디롱','새채팅이 아닌것만 보이라니까 !'),(7,'dyyyyw',NULL,'2021-04-08 00:27:03','평양산검은콩','돌 곰103','새채팅'),(8,'dyyyyw',NULL,'2021-04-08 00:27:31','평양산검은콩','담원 토스트102','새채팅'),(10,'hossi','giga1615','2021-04-08 03:57:55','꼬마자동차 붕봉','데롱디롱','새채팅'),(23,'giga1615','ldkgang','2021-04-08 06:09:02','데롱디롱','JSDD SUL','새채팅'),(24,'giga1615','ldkgang','2021-04-08 06:09:12','데롱디롱','JSDD SUL','HI'),(25,'giga1615','ldkgang','2021-04-08 06:09:20','데롱디롱','JSDD SUL','뭐하십니까'),(26,'dyyyyw','ldkgang','2021-04-08 06:35:26','평양산검은콩','JSDD SUL','새채팅'),(27,'dyyyyw','ldkgang','2021-04-08 06:35:31','평양산검은콩','JSDD SUL','당신은 이도건'),(28,'ldkgang',NULL,'2021-04-08 06:52:52','JSDD SUL','this.member.nickname','새채팅'),(29,'ldkgang',NULL,'2021-04-08 06:56:45','JSDD SUL','this.member.nickname','새채팅'),(30,'ldkgang',NULL,'2021-04-08 07:47:14','JSDD SUL','this.member.nickname','새채팅');
/*!40000 ALTER TABLE `dm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_list`
--

DROP TABLE IF EXISTS `like_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_list` (
  `no` int NOT NULL AUTO_INCREMENT,
  `my_nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  `my_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  `your_nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_list`
--

LOCK TABLES `like_list` WRITE;
/*!40000 ALTER TABLE `like_list` DISABLE KEYS */;
INSERT INTO `like_list` VALUES (1,'평양산검은콩','dyyyyw','개불김'),(2,'평양산검은콩','dyyyyw','굿또'),(4,'평양산검은콩','dyyyyw','숏다리의꿈'),(5,'평양산검은콩','dyyyyw','디롱데롱'),(6,'평양산검은콩','dyyyyw','나는즐겜러당'),(7,'평양산검은콩','dyyyyw','꼬마자동차붕봉'),(9,'평양산검은콩','dyyyyw','데롱디롱'),(10,'평양산검은콩','dyyyyw','꼬마자동차 붕봉'),(11,'데롱디롱','giga1615','평양산검은콩'),(12,'데롱디롱','giga1615','나는즐겜러당'),(13,'데롱디롱','giga1615','꼬마자동차 붕봉'),(14,'데롱디롱','giga1615','개불김'),(15,'데롱디롱','giga1615','굿또'),(16,'데롱디롱','giga1615','숏다리의 꿈'),(17,'데롱디롱','giga1615','숏다리의꿈'),(18,'데롱디롱','giga1615','나는즐겜러당'),(19,'데롱디롱','giga1615','나는즐겜러당'),(20,'데롱디롱','giga1615','담원 토스트102'),(21,'데롱디롱','giga1615','돌 곰103'),(24,'데롱디롱','giga1615','산뜻한아침햇살112'),(25,'JSDD SUL','ldkgang','담원 토스트102'),(26,'데롱디롱','giga1615','땅콩216'),(27,'JSDD SUL','ldkgang','담원 토스트102'),(29,'JSDD SUL','ldkgang','산뜻한아침햇살112'),(30,'꼬마자동차 붕봉','hossi','존잘러203'),(31,'꼬마자동차 붕봉','hossi','나는즐겜러당'),(32,'JSDD SUL','ldkgang','꼬마자동차 붕봉'),(33,'JSDD SUL','ldkgang','평양산검은콩'),(34,'JSDD SUL','ldkgang','숏다리의 꿈');
/*!40000 ALTER TABLE `like_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` varchar(100) NOT NULL,
  `nick_name` varchar(100) DEFAULT NULL,
  `pw` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES ('5ujin','개구리꾀꼬닥','e2ca1c2129392c66d87334bd2452c572058d406b4e85f43c1f72def10f'),('checkID','실버맨','ed802543874ce3d4ffc1ae72986ef35994dc306e8653be9e09a8e4296b'),('dayun0','굿또','76cd6aec42817189102b808588c5c2bd7c3578bc7348e860bbe9f2a22c'),('dyyyyw','평양산검은콩','76cd6aec42817189102b808588c5c2bd7c3578bc7348e860bbe9f2a22c'),('giga1615','숏다리의 꿈','98d6133ea56028138ca90d9e983cb76a30afd282302ec1fdae4fb52c2b'),('hossi','꼬마자동차 붕봉','096e0a3e75c12b1e713e6bccb479a52a2f4f10fb0eadfa692ad1e136da'),('ldkgang','JSDD SUL','3f1d543498ae7401a67eacd33980bd4b190fdfa3a97f24433873253467'),('wogns0','개불김','69107a50e1df580a69a4324b0eae14541c294fd4022d4253a911698387'),('ybj0749','나는즐겜러당','7feebafc7ad039270b7169911923035f4b3308e36259b649dc3c6f9206');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memberChatRoomList`
--

DROP TABLE IF EXISTS `memberChatRoomList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `memberChatRoomList` (
  `room_no` int NOT NULL,
  `id` varchar(100) NOT NULL,
  `nick_name` varchar(100) DEFAULT NULL,
  `room_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`room_no`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memberChatRoomList`
--

LOCK TABLES `memberChatRoomList` WRITE;
/*!40000 ALTER TABLE `memberChatRoomList` DISABLE KEYS */;
/*!40000 ALTER TABLE `memberChatRoomList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_for_recommend`
--

DROP TABLE IF EXISTS `member_for_recommend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_for_recommend` (
  `no` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  `time_predict` double DEFAULT '19',
  `game_style` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT '솔랭',
  `liked_position` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT '없음',
  `liked` int DEFAULT '0',
  `wins` int DEFAULT '0',
  `losses` int DEFAULT NULL,
  `tier` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT '없음',
  `user_level` int DEFAULT '0',
  `win_rate` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs DEFAULT '없음',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB AUTO_INCREMENT=809 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_for_recommend`
--

LOCK TABLES `member_for_recommend` WRITE;
/*!40000 ALTER TABLE `member_for_recommend` DISABLE KEYS */;
INSERT INTO `member_for_recommend` VALUES (102,'담원 토스트102',0,'솔랭','탑',3,61,38,'Silver',171,'61'),(103,'돌 곰103',0,'솔랭','정글',6,30,20,'Gold',164,'58'),(104,'뚜익이104',0,'솔랭','미드',12,69,77,'Platinum',130,'46'),(105,'띵찬이다105',0,'솔랭','원딜',9,84,84,'Silver',129,'49'),(106,'물빵왕106',1,'솔랭','서포터',7,6,5,'Silver',73,'50'),(107,'방패왕107',1,'솔랭','탑',11,30,20,'Gold',99,'58'),(108,'버섯던지자108',1,'솔랭','정글',5,13,13,'Silver',95,'48'),(109,'벚꽃냐무109',1,'솔랭','미드',6,30,20,'Platinum',151,'58'),(110,'블라블라블라썸110',2,'솔랭','원딜',2,38,37,'Gold',139,'50'),(111,'사랑했다행복해라111',2,'솔랭','서포터',5,30,20,'Gold',64,'58'),(112,'산뜻한아침햇살112',2,'솔랭','탑',6,96,109,'Gold',172,'46'),(113,'새벽별비처럼113',2,'솔랭','정글',9,30,20,'Gold',40,'58'),(114,'아수라발탁114',3,'솔랭','미드',4,30,20,'Silver',106,'58'),(115,'안뇨옹 핑핑아115',3,'솔랭','원딜',6,14,17,'Gold',78,'43'),(116,'암쁘럼인디왕116',3,'솔랭','서포터',2,30,24,'Gold',44,'54'),(117,'야채 그 자체117',3,'솔랭','탑',11,6,11,'Platinum',108,'33'),(118,'얼탱구리없네118',4,'솔랭','정글',1,30,20,'Silver',75,'58'),(119,'에바쌔119',4,'솔랭','미드',6,14,12,'Platinum',174,'51'),(120,'원거리개조심120',4,'솔랭','원딜',10,30,20,'Gold',163,'58'),(121,'이게 나야 빠끄121',15,'솔랭','서포터',4,30,20,'Gold',116,'58'),(122,'이게 나얌 빠끄122',15,'솔랭','탑',3,13,12,'Gold',59,'50'),(123,'장용은123',15,'솔랭','미드',6,50,53,'Gold',69,'48'),(124,'재호회계연습124',15,'솔랭','원딜',6,33,38,'Silver',138,'45'),(125,'저는버러지125',15,'솔랭','서포터',10,49,49,'Gold',153,'49'),(126,'좋아하고 잘해요126',16,'솔랭','탑',6,30,20,'Gold',172,'58'),(127,'준규석규앙규127',16,'솔랭','정글',0,30,20,'Silver',72,'58'),(128,'짓짓짓128',16,'솔랭','미드',10,30,20,'Gold',113,'58'),(129,'촉수 있는 곳이129',16,'솔랭','원딜',7,87,65,'Silver',169,'56'),(130,'최배다르130',16,'솔랭','서포터',6,30,20,'Gold',178,'58'),(131,'치킨에진심인사람131',16,'솔랭','탑',10,12,17,'Silver',52,'40'),(132,'킬각아니당132',17,'솔랭','정글',1,30,20,'Gold',149,'58'),(133,'하마의심장133',17,'솔랭','미드',6,94,104,'Silver',110,'47'),(134,'하필그날134',17,'솔랭','원딜',14,30,20,'Platinum',71,'58'),(135,'행복은 퇴사순135',17,'솔랭','서포터',8,137,116,'Silver',147,'53'),(136,'히포의심장136',17,'솔랭','탑',13,6,4,'Platinum',43,'54'),(137,'JSDD KUK137',22,'솔랭','정글',11,300,290,'Gold',46,'50'),(138,'JSDD BOB138',22,'솔랭','정글',0,30,29,'Silver',70,'50'),(139,'심ba139',10,'솔랭','탑',13,530,489,'Gold',31,'51'),(140,'말만 그 자체140',23,'솔랭','미드',8,508,509,'Gold',65,'49'),(141,'또띠 그 자체141',23,'솔랭','탑',13,123,122,'Bronze',55,'50'),(142,'민래기142',18,'솔랭','원딜',14,120,109,'Bronze',48,'52'),(143,'지 흐 운143',19,'솔랭','탑',0,501,509,'Gold',46,'49'),(144,'Gfriendly144',19,'솔랭','탑',2,210,215,'Gold',56,'49'),(145,'첫 번째 행운145',15,'솔랭','탑',12,130,139,'Gold',115,'48'),(146,'버섯 그 자체146',22,'솔랭','원딜',7,590,600,'Gold',77,'49'),(147,'꽃보다 엔딩147',19,'솔랭','서포터',3,510,489,'Bronze',159,'51'),(148,'김진우 화이팅148',22,'솔랭','서포터',9,533,509,'Silver',83,'51'),(149,'자취하는여자149',23,'솔랭','탑',7,130,122,'Gold',61,'51'),(150,'윤영의십돼지년150',20,'솔랭','미드',7,530,539,'Gold',175,'49'),(151,'모스맘151',22,'솔랭','원딜',1,430,401,'Gold',64,'51'),(152,'귀살대 김성회152',22,'솔랭','서포터',0,530,489,'Gold',63,'51'),(153,'상현 1 정민우153',22,'솔랭','원딜',13,263,290,'Gold',95,'47'),(154,'한권으로끝내기N3154',10,'솔랭','탑',3,160,196,'Bronze',107,'44'),(155,'실세폰돌남155',23,'솔랭','서포터',7,480,489,'Silver',71,'49'),(156,'내무조156',21,'솔랭','미드',13,98,89,'Bronze',153,'52'),(157,'필리핀황금여행157',1,'솔랭','탑',13,43,27,'Gold',73,'60'),(158,'왜자꾸잉잉거려잉158',14,'솔랭','서포터',13,16,8,'Silver',175,'64'),(159,'나는 죽은 사람159',17,'솔랭','미드',11,165,165,'Iron',30,'49'),(160,'기운기호랑이범160',10,'솔랭','탑',4,465,489,'Gold',42,'48'),(161,'핫떼떼161',10,'솔랭','탑',14,324,365,'Bronze',91,'46'),(162,'GRRRRkakkak162',10,'솔랭','원딜',13,230,239,'Silver',152,'48'),(163,'neque163',10,'솔랭','원딜',9,231,239,'Silver',155,'49'),(164,'레이디가가렌164',22,'솔랭','탑',6,465,456,'Platinum',140,'50'),(165,'맛있는오레오165',23,'솔랭','미드',3,516,546,'Platinum',55,'48'),(166,'서니느166',4,'솔랭','서포터',11,150,159,'Platinum',127,'48'),(167,'운암사 철중스님167',18,'솔랭','정글',4,237,239,'Silver',142,'49'),(168,'작은집토토로168',19,'솔랭','서포터',3,154,159,'Iron',147,'49'),(169,'햇썽이169',18,'솔랭','미드',3,246,239,'Silver',130,'50'),(170,'aqq170',20,'솔랭','원딜',5,216,239,'Silver',31,'47'),(171,'c1 혁이171',20,'솔랭','원딜',4,256,239,'Silver',33,'51'),(172,'ztzt123172',21,'솔랭','서포터',5,130,129,'Bronze',45,'50'),(173,'가자 리뽀카로173',18,'솔랭','원딜',12,156,149,'Gold',94,'50'),(174,'가자 페카도로174',18,'솔랭','미드',14,223,223,'Silver',157,'49'),(175,'갓 tak175',8,'솔랭','미드',7,136,129,'Bronze',173,'51'),(176,'갓 자윤176',21,'솔랭','미드',8,153,123,'Gold',63,'55'),(177,'개소리하면걍박음177',21,'솔랭','탑',4,432,423,'Gold',68,'50'),(178,'곱쓰리178',21,'솔랭','정글',10,232,233,'Gold',121,'49'),(179,'광대인생179',22,'솔랭','정글',12,523,532,'Gold',72,'49'),(180,'광희사우르스180',1,'솔랭','정글',13,15,15,'Gold',115,'48'),(181,'김준이이181',21,'솔랭','정글',1,322,333,'Gold',32,'49'),(182,'끌레드르182',22,'솔랭','정글',10,345,354,'Gold',84,'49'),(183,'닭발에진심인사람183',22,'솔랭','탑',1,352,323,'Gold',144,'52'),(184,'아바타184',0,'솔랭','탑',8,211,102,'Silver',140,'67'),(185,'우유185',1,'솔랭','탑',8,210,107,'Silver',88,'66'),(186,'커피186',2,'솔랭','탑',2,150,111,'Silver',139,'57'),(187,'모카187',3,'솔랭','탑',1,145,120,'Silver',104,'54'),(188,'초코188',4,'솔랭','탑',0,133,100,'Silver',71,'56'),(189,'브라우니189',5,'솔랭','탑',12,153,88,'Silver',165,'63'),(190,'댕댕이190',6,'솔랭','탑',0,75,70,'Silver',133,'51'),(191,'삐삐191',7,'솔랭','탑',10,13,10,'Silver',138,'54'),(192,'뚠뚠192',8,'솔랭','탑',6,176,18,'Silver',114,'90'),(193,'강냉이193',9,'솔랭','탑',1,53,79,'Silver',124,'39'),(194,'삐삐194',7,'솔랭','탑',3,27,76,'Silver',99,'25'),(195,'뚠뚠195',8,'솔랭','탑',11,1,49,'Silver',94,'1'),(196,'강냉이196',9,'솔랭','탑',4,94,88,'Silver',143,'51'),(197,'잠만보197',10,'솔랭','탑',1,195,23,'Silver',103,'89'),(198,'안드로메다198',11,'솔랭','탑',7,53,62,'Silver',57,'45'),(199,'프라하199',12,'솔랭','탑',4,63,70,'Silver',98,'47'),(200,'고인물200',13,'솔랭','탑',14,116,80,'Silver',138,'58'),(201,'갑분싸201',14,'솔랭','탑',12,50,85,'Silver',65,'36'),(202,'인싸202',15,'솔랭','탑',5,104,3,'Silver',33,'96'),(203,'존잘러203',16,'솔랭','탑',4,127,5,'Silver',89,'95'),(204,'곰스204',17,'솔랭','탑',0,77,77,'Silver',168,'49'),(205,'바운스205',18,'솔랭','탑',14,137,11,'Silver',95,'91'),(206,'뚱이206',19,'솔랭','탑',4,103,24,'Silver',90,'80'),(207,'복서207',20,'솔랭','탑',9,136,66,'Silver',135,'66'),(208,'해충박멸208',21,'솔랭','탑',5,55,40,'Silver',75,'57'),(209,'디스코드209',22,'솔랭','탑',0,34,66,'Silver',90,'33'),(210,'후라이팬210',23,'솔랭','탑',13,161,4,'Silver',47,'96'),(211,'존버211',0,'솔랭','미드',6,160,86,'Silver',84,'64'),(212,'꿀꿀이212',1,'솔랭','미드',7,186,5,'Silver',101,'96'),(213,'나쵸213',2,'솔랭','미드',2,95,21,'Silver',73,'81'),(214,'너구리214',3,'솔랭','미드',5,130,61,'Silver',32,'67'),(215,'아몬드215',4,'솔랭','미드',6,22,73,'Silver',62,'22'),(216,'땅콩216',5,'솔랭','미드',15,62,36,'Silver',33,'62'),(217,'치즈217',6,'솔랭','미드',7,178,35,'Silver',100,'83'),(218,'호떡218',7,'솔랭','미드',7,22,48,'Silver',72,'30'),(219,'만두219',8,'솔랭','미드',2,21,6,'Silver',30,'75'),(220,'대파220',9,'솔랭','미드',5,1,85,'Silver',53,'1'),(221,'부엉이221',10,'솔랭','미드',6,46,60,'Silver',145,'42'),(222,'프로222',11,'솔랭','미드',13,64,80,'Silver',89,'44'),(223,'록맨223',12,'솔랭','미드',1,15,94,'Silver',130,'13'),(224,'호구맨224',13,'솔랭','미드',13,103,73,'Silver',54,'58'),(225,'레이저225',14,'솔랭','미드',4,22,36,'Silver',150,'37'),(226,'고독226',15,'솔랭','미드',8,100,40,'Silver',106,'70'),(227,'저격227',16,'솔랭','미드',2,104,39,'Silver',54,'72'),(228,'달님228',17,'솔랭','미드',14,78,78,'Silver',70,'49'),(229,'더힐229',18,'솔랭','미드',6,148,36,'Silver',160,'80'),(230,'놀고있네230',19,'솔랭','미드',4,122,95,'Silver',111,'55'),(231,'프리미어231',20,'솔랭','미드',0,190,89,'Silver',44,'67'),(232,'메이트232',21,'솔랭','미드',5,118,29,'Silver',159,'79'),(233,'바른마음233',22,'솔랭','미드',10,139,60,'Silver',32,'69'),(234,'백구234',23,'솔랭','미드',8,187,86,'Silver',105,'68'),(235,'잇츠235',0,'솔랭','원딜',8,74,133,'Silver',101,'35'),(236,'아메리카노236',1,'솔랭','원딜',3,145,24,'Silver',158,'85'),(237,'고고고고237',2,'솔랭','원딜',5,138,19,'Silver',160,'87'),(238,'오렌지피클238',3,'솔랭','원딜',3,130,144,'Silver',144,'47'),(239,'땡땡이239',4,'솔랭','원딜',14,29,16,'Silver',62,'63'),(240,'월계수240',5,'솔랭','원딜',1,144,73,'Silver',149,'66'),(241,'라이트241',6,'솔랭','원딜',9,83,45,'Silver',79,'64'),(242,'테슬라242',7,'솔랭','원딜',13,126,47,'Silver',69,'72'),(243,'실루엣243',8,'솔랭','원딜',8,6,42,'Silver',80,'12'),(244,'시계244',9,'솔랭','원딜',2,40,73,'Silver',163,'35'),(245,'레전드245',10,'솔랭','원딜',14,99,125,'Silver',93,'44'),(246,'결정246',11,'솔랭','원딜',8,29,72,'Silver',99,'28'),(247,'시즌247',12,'솔랭','원딜',11,121,92,'Silver',35,'56'),(248,'뉴비248',13,'솔랭','원딜',1,95,49,'Silver',149,'65'),(249,'버드249',14,'솔랭','원딜',1,112,115,'Silver',161,'49'),(250,'열차250',15,'솔랭','원딜',6,87,92,'Silver',30,'48'),(251,'다이아몬드251',16,'솔랭','원딜',10,50,124,'Silver',84,'28'),(252,'전기피카츄252',17,'솔랭','원딜',1,19,25,'Silver',154,'42'),(253,'윈디감옥253',18,'솔랭','원딜',9,70,124,'Silver',37,'35'),(254,'빌런맨254',19,'솔랭','원딜',9,110,28,'Silver',145,'79'),(255,'데빌255',20,'솔랭','원딜',5,111,22,'Silver',134,'82'),(256,'바이바이256',21,'솔랭','원딜',0,77,21,'Silver',55,'77'),(257,'호시탐탐257',22,'솔랭','원딜',14,22,47,'Silver',144,'31'),(258,'레이븐258',23,'솔랭','원딜',10,21,114,'Silver',76,'15'),(259,'세트259',0,'솔랭','서포터',8,56,88,'Silver',69,'38'),(260,'물범260',1,'솔랭','서포터',13,124,55,'Silver',87,'68'),(261,'극비261',2,'솔랭','서포터',9,56,113,'Silver',47,'32'),(262,'다이어트262',3,'솔랭','서포터',6,98,1,'Silver',97,'98'),(263,'풀피263',4,'솔랭','서포터',4,12,59,'Silver',165,'16'),(264,'레나264',5,'솔랭','서포터',3,111,75,'Silver',54,'59'),(265,'야채265',6,'솔랭','서포터',2,44,144,'Silver',44,'23'),(266,'푸른점266',7,'솔랭','서포터',5,139,114,'Silver',178,'54'),(267,'푸른곰팡이267',8,'솔랭','서포터',1,4,126,'Silver',131,'3'),(268,'청둥오리268',9,'솔랭','서포터',6,20,21,'Silver',90,'47'),(269,'아이스크림269',10,'솔랭','서포터',12,46,18,'Silver',178,'70'),(270,'대나무270',11,'솔랭','서포터',11,101,3,'Silver',140,'96'),(271,'바이올린271',12,'솔랭','서포터',8,12,54,'Silver',139,'17'),(272,'바이올렛272',13,'솔랭','서포터',6,81,97,'Silver',93,'45'),(273,'인터스텔라273',14,'솔랭','서포터',7,89,6,'Silver',169,'92'),(274,'팽이274',15,'솔랭','서포터',4,65,6,'Silver',87,'90'),(275,'토템275',16,'솔랭','서포터',12,136,63,'Silver',49,'68'),(276,'나나276',17,'솔랭','서포터',2,58,99,'Silver',106,'36'),(277,'보라돌이277',18,'솔랭','서포터',7,22,115,'Silver',52,'15'),(278,'뚜비278',19,'솔랭','서포터',0,59,102,'Silver',63,'36'),(279,'뽀오279',20,'솔랭','서포터',10,32,7,'Silver',128,'80'),(280,'악어새280',21,'솔랭','서포터',3,86,112,'Silver',121,'43'),(281,'마법전사281',22,'솔랭','서포터',1,0,117,'Silver',44,'0'),(282,'나무늘보282',23,'솔랭','서포터',13,133,17,'Silver',128,'88'),(283,'범고래283',0,'솔랭','정글',3,137,32,'Silver',179,'80'),(284,'고래밥284',1,'솔랭','정글',8,49,2,'Silver',32,'94'),(285,'마라치킨285',2,'솔랭','정글',13,13,60,'Silver',40,'17'),(286,'사파리286',3,'솔랭','정글',14,111,76,'Silver',77,'59'),(287,'비둘기287',4,'솔랭','정글',2,46,4,'Silver',87,'90'),(288,'포카리스웨트288',5,'솔랭','정글',0,7,17,'Silver',172,'28'),(289,'차이나팜289',6,'솔랭','정글',7,84,101,'Silver',120,'45'),(290,'파머빵290',7,'솔랭','정글',4,104,65,'Silver',56,'61'),(291,'단판빵을291',8,'솔랭','정글',2,13,24,'Silver',38,'34'),(292,'다비켜라제발292',9,'솔랭','정글',11,78,18,'Silver',142,'80'),(293,'나는슈퍼원더풀293',10,'솔랭','정글',6,10,143,'Silver',117,'6'),(294,'딜러자동차294',11,'솔랭','정글',12,86,2,'Silver',129,'96'),(295,'뭘파는건데295',12,'솔랭','정글',11,52,107,'Silver',117,'32'),(296,'왜그러는데296',13,'솔랭','정글',6,77,65,'Silver',166,'53'),(297,'뭐하는건데297',14,'솔랭','정글',14,96,135,'Silver',149,'41'),(298,'아진짜이거298',15,'솔랭','정글',6,87,29,'Silver',70,'74'),(299,'언제까지299',16,'솔랭','정글',4,34,83,'Silver',172,'28'),(300,'다하는건가300',17,'솔랭','정글',1,14,123,'Silver',170,'10'),(301,'과연나는301',18,'솔랭','정글',9,124,99,'Silver',156,'55'),(302,'오늘어떤302',19,'솔랭','정글',14,124,25,'Silver',89,'82'),(303,'아이디를303',20,'솔랭','정글',13,51,32,'Silver',98,'60'),(304,'받을까소음304',21,'솔랭','정글',7,6,86,'Silver',43,'6'),(305,'야간대장305',22,'솔랭','정글',14,113,5,'Silver',43,'94'),(306,'절약모드306',23,'솔랭','정글',5,138,76,'Silver',55,'64'),(307,'아바타307',0,'솔랭','탑',11,211,102,'Bronze',117,'67'),(308,'우유308',1,'솔랭','탑',13,210,107,'Bronze',93,'66'),(309,'커피309',2,'솔랭','탑',1,150,111,'Bronze',81,'57'),(310,'모카310',3,'솔랭','탑',10,145,120,'Bronze',96,'54'),(311,'초코311',4,'솔랭','탑',6,133,100,'Bronze',60,'56'),(312,'브라우니312',5,'솔랭','탑',13,153,88,'Bronze',133,'63'),(313,'댕댕이313',6,'솔랭','탑',4,75,70,'Bronze',155,'51'),(314,'삐삐314',7,'솔랭','탑',12,118,60,'Bronze',44,'65'),(315,'뚠뚠315',8,'솔랭','탑',1,132,9,'Bronze',178,'92'),(316,'강냉이316',9,'솔랭','탑',0,99,19,'Bronze',128,'83'),(317,'잠만보317',10,'솔랭','탑',0,93,75,'Bronze',76,'55'),(318,'안드로메다318',11,'솔랭','탑',12,73,58,'Bronze',116,'55'),(319,'프라하319',12,'솔랭','탑',3,166,40,'Bronze',175,'80'),(320,'고인물320',13,'솔랭','탑',9,107,46,'Bronze',47,'69'),(321,'갑분싸321',14,'솔랭','탑',6,140,11,'Bronze',129,'92'),(322,'인싸322',15,'솔랭','탑',4,98,11,'Bronze',174,'89'),(323,'존잘러323',16,'솔랭','탑',1,14,4,'Bronze',153,'73'),(324,'곰스324',17,'솔랭','탑',10,195,76,'Bronze',64,'71'),(325,'바운스325',18,'솔랭','탑',2,175,9,'Bronze',131,'94'),(326,'뚱이326',19,'솔랭','탑',11,168,92,'Bronze',133,'64'),(327,'복서327',20,'솔랭','탑',5,19,70,'Bronze',93,'21'),(328,'해충박멸328',21,'솔랭','탑',7,49,12,'Bronze',38,'79'),(329,'디스코드329',22,'솔랭','탑',6,174,0,'Bronze',179,'99'),(330,'후라이팬330',23,'솔랭','탑',8,76,89,'Bronze',154,'45'),(331,'존버331',0,'솔랭','미드',10,69,5,'Bronze',52,'92'),(332,'꿀꿀이332',1,'솔랭','미드',10,45,96,'Bronze',67,'31'),(333,'나쵸333',2,'솔랭','미드',4,26,77,'Bronze',152,'25'),(334,'너구리334',3,'솔랭','미드',7,98,12,'Bronze',78,'88'),(335,'아몬드335',4,'솔랭','미드',8,29,36,'Bronze',55,'43'),(336,'땅콩336',5,'솔랭','미드',5,78,85,'Bronze',160,'47'),(337,'치즈337',6,'솔랭','미드',1,16,86,'Bronze',158,'15'),(338,'호떡338',7,'솔랭','미드',7,18,84,'Bronze',129,'17'),(339,'만두339',8,'솔랭','미드',0,193,29,'Bronze',143,'86'),(340,'대파340',9,'솔랭','미드',12,112,93,'Bronze',147,'54'),(341,'부엉이341',10,'솔랭','미드',0,199,16,'Bronze',127,'92'),(342,'프로342',11,'솔랭','미드',9,170,74,'Bronze',164,'69'),(343,'록맨343',12,'솔랭','미드',1,38,71,'Bronze',112,'34'),(344,'호구맨344',13,'솔랭','미드',10,3,92,'Bronze',35,'3'),(345,'레이저345',14,'솔랭','미드',14,113,6,'Bronze',111,'94'),(346,'고독346',15,'솔랭','미드',13,128,1,'Bronze',120,'98'),(347,'저격347',16,'솔랭','미드',8,25,60,'Bronze',88,'29'),(348,'달님348',17,'솔랭','미드',3,127,36,'Bronze',52,'77'),(349,'더힐349',18,'솔랭','미드',7,184,52,'Bronze',117,'77'),(350,'놀고있네350',19,'솔랭','미드',10,167,62,'Bronze',96,'72'),(351,'프리미어351',20,'솔랭','미드',14,122,17,'Bronze',103,'87'),(352,'메이트352',21,'솔랭','미드',13,12,77,'Bronze',45,'13'),(353,'바른마음353',22,'솔랭','미드',6,138,14,'Bronze',35,'90'),(354,'백구354',23,'솔랭','미드',7,126,72,'Bronze',164,'63'),(355,'잇츠355',0,'솔랭','원딜',3,109,70,'Bronze',83,'60'),(356,'아메리카노356',1,'솔랭','원딜',10,25,64,'Bronze',46,'27'),(357,'고고고고357',2,'솔랭','원딜',10,95,132,'Bronze',99,'41'),(358,'오렌지피클358',3,'솔랭','원딜',7,79,148,'Bronze',179,'34'),(359,'땡땡이359',4,'솔랭','원딜',3,52,120,'Bronze',118,'30'),(360,'월계수360',5,'솔랭','원딜',11,141,47,'Bronze',175,'74'),(361,'라이트361',6,'솔랭','원딜',1,114,129,'Bronze',40,'46'),(362,'테슬라362',7,'솔랭','원딜',1,3,77,'Bronze',95,'3'),(363,'실루엣363',8,'솔랭','원딜',4,76,0,'Bronze',176,'98'),(364,'시계364',9,'솔랭','원딜',4,73,67,'Bronze',114,'51'),(365,'레전드365',10,'솔랭','원딜',8,113,68,'Bronze',165,'62'),(366,'결정366',11,'솔랭','원딜',13,1,102,'Bronze',151,'0'),(367,'시즌367',12,'솔랭','원딜',10,57,129,'Bronze',81,'30'),(368,'뉴비368',13,'솔랭','원딜',14,25,39,'Bronze',74,'38'),(369,'버드369',14,'솔랭','원딜',10,119,31,'Bronze',96,'78'),(370,'열차370',15,'솔랭','원딜',9,95,85,'Bronze',78,'52'),(371,'다이아몬드371',16,'솔랭','원딜',13,141,149,'Bronze',75,'48'),(372,'전기피카츄372',17,'솔랭','원딜',11,22,115,'Bronze',110,'15'),(373,'윈디감옥373',18,'솔랭','원딜',14,60,104,'Bronze',148,'36'),(374,'빌런맨374',19,'솔랭','원딜',7,39,36,'Bronze',78,'51'),(375,'데빌375',20,'솔랭','원딜',9,62,52,'Bronze',66,'53'),(376,'바이바이376',21,'솔랭','원딜',9,76,76,'Bronze',66,'49'),(377,'호시탐탐377',22,'솔랭','원딜',3,149,70,'Bronze',103,'67'),(378,'레이븐378',23,'솔랭','원딜',5,53,54,'Bronze',137,'49'),(379,'세트379',0,'솔랭','서포터',2,114,107,'Bronze',46,'51'),(380,'물범380',1,'솔랭','서포터',12,43,43,'Bronze',91,'49'),(381,'극비381',2,'솔랭','서포터',7,88,13,'Bronze',137,'86'),(382,'다이어트382',3,'솔랭','서포터',13,100,13,'Bronze',83,'87'),(383,'풀피383',4,'솔랭','서포터',2,65,135,'Bronze',126,'32'),(384,'레나384',5,'솔랭','서포터',1,32,55,'Bronze',50,'36'),(385,'야채385',6,'솔랭','서포터',13,28,126,'Bronze',141,'18'),(386,'푸른점386',7,'솔랭','서포터',3,97,108,'Bronze',75,'47'),(387,'푸른곰팡이387',8,'솔랭','서포터',5,100,27,'Bronze',73,'78'),(388,'청둥오리388',9,'솔랭','서포터',3,134,142,'Bronze',111,'48'),(389,'아이스크림389',10,'솔랭','서포터',2,7,58,'Bronze',158,'10'),(390,'대나무390',11,'솔랭','서포터',1,120,126,'Bronze',128,'48'),(391,'바이올린391',12,'솔랭','서포터',12,122,84,'Bronze',136,'58'),(392,'바이올렛392',13,'솔랭','서포터',0,53,12,'Bronze',114,'80'),(393,'인터스텔라393',14,'솔랭','서포터',9,53,78,'Bronze',134,'40'),(394,'팽이394',15,'솔랭','서포터',14,83,31,'Bronze',147,'72'),(395,'토템395',16,'솔랭','서포터',0,57,41,'Bronze',156,'57'),(396,'나나396',17,'솔랭','서포터',5,37,61,'Bronze',157,'37'),(397,'보라돌이397',18,'솔랭','서포터',10,44,39,'Bronze',141,'52'),(398,'뚜비398',19,'솔랭','서포터',5,64,52,'Bronze',51,'54'),(399,'뽀오399',20,'솔랭','서포터',10,69,41,'Bronze',104,'62'),(400,'악어새400',21,'솔랭','서포터',5,148,18,'Bronze',37,'88'),(401,'마법전사401',22,'솔랭','서포터',9,94,117,'Bronze',143,'44'),(402,'나무늘보402',23,'솔랭','서포터',2,4,118,'Bronze',123,'3'),(403,'범고래403',0,'솔랭','정글',12,130,146,'Bronze',159,'46'),(404,'고래밥404',1,'솔랭','정글',12,42,73,'Bronze',94,'36'),(405,'마라치킨405',2,'솔랭','정글',9,90,82,'Bronze',115,'52'),(406,'사파리406',3,'솔랭','정글',8,138,146,'Bronze',111,'48'),(407,'비둘기407',4,'솔랭','정글',14,17,96,'Bronze',34,'14'),(408,'포카리스웨트408',5,'솔랭','정글',1,54,17,'Bronze',106,'75'),(409,'차이나팜409',6,'솔랭','정글',10,37,25,'Bronze',98,'58'),(410,'파머빵410',7,'솔랭','정글',4,14,144,'Bronze',143,'8'),(411,'단판빵을411',8,'솔랭','정글',3,78,110,'Bronze',92,'41'),(412,'다비켜라제발412',9,'솔랭','정글',2,18,58,'Bronze',150,'23'),(413,'나는슈퍼원더풀413',10,'솔랭','정글',5,88,116,'Bronze',146,'42'),(414,'딜러자동차414',11,'솔랭','정글',3,15,27,'Bronze',102,'34'),(415,'뭘파는건데415',12,'솔랭','정글',0,93,86,'Bronze',41,'51'),(416,'왜그러는데416',13,'솔랭','정글',8,148,35,'Bronze',171,'80'),(417,'뭐하는건데417',14,'솔랭','정글',8,31,48,'Bronze',101,'38'),(418,'아진짜이거418',15,'솔랭','정글',3,1,8,'Bronze',113,'10'),(419,'언제까지419',16,'솔랭','정글',7,40,26,'Bronze',83,'59'),(420,'다하는건가420',17,'솔랭','정글',11,10,122,'Bronze',47,'7'),(421,'과연나는421',18,'솔랭','정글',3,132,145,'Bronze',104,'47'),(422,'오늘어떤422',19,'솔랭','정글',0,30,14,'Bronze',51,'66'),(423,'아이디를423',20,'솔랭','정글',5,132,20,'Bronze',65,'86'),(424,'받을까소음424',21,'솔랭','정글',12,2,102,'Bronze',142,'1'),(425,'야간대장425',22,'솔랭','정글',14,54,116,'Bronze',33,'31'),(426,'절약모드426',23,'솔랭','정글',5,118,90,'Bronze',162,'56'),(427,'아바타427',0,'솔랭','탑',14,211,102,'Platinum',81,'67'),(428,'우유428',1,'솔랭','탑',10,210,107,'Platinum',39,'66'),(429,'커피429',2,'솔랭','탑',10,150,111,'Platinum',72,'57'),(430,'모카430',3,'솔랭','탑',3,145,120,'Platinum',63,'54'),(431,'초코431',4,'솔랭','탑',1,133,100,'Platinum',71,'56'),(432,'브라우니432',5,'솔랭','탑',12,153,88,'Platinum',137,'63'),(433,'댕댕이433',6,'솔랭','탑',11,75,70,'Platinum',143,'51'),(434,'삐삐434',7,'솔랭','탑',6,98,71,'Platinum',123,'57'),(435,'뚠뚠435',8,'솔랭','탑',10,79,56,'Platinum',156,'58'),(436,'강냉이436',9,'솔랭','탑',5,127,48,'Platinum',84,'72'),(437,'잠만보437',10,'솔랭','탑',10,106,18,'Platinum',69,'84'),(438,'안드로메다438',11,'솔랭','탑',4,68,15,'Platinum',67,'80'),(439,'프라하439',12,'솔랭','탑',7,146,21,'Platinum',98,'86'),(440,'고인물440',13,'솔랭','탑',7,175,73,'Platinum',109,'70'),(441,'갑분싸441',14,'솔랭','탑',1,7,99,'Platinum',70,'6'),(442,'인싸442',15,'솔랭','탑',12,167,20,'Platinum',145,'88'),(443,'존잘러443',16,'솔랭','탑',0,108,7,'Platinum',35,'93'),(444,'곰스444',17,'솔랭','탑',9,151,56,'Platinum',160,'72'),(445,'바운스445',18,'솔랭','탑',14,107,99,'Platinum',67,'51'),(446,'뚱이446',19,'솔랭','탑',1,75,89,'Platinum',126,'45'),(447,'복서447',20,'솔랭','탑',8,64,94,'Platinum',100,'40'),(448,'해충박멸448',21,'솔랭','탑',8,150,93,'Platinum',91,'61'),(449,'디스코드449',22,'솔랭','탑',14,78,17,'Platinum',128,'81'),(450,'후라이팬450',23,'솔랭','탑',2,140,98,'Platinum',36,'58'),(451,'존버451',0,'솔랭','미드',13,162,11,'Platinum',66,'93'),(452,'꿀꿀이452',1,'솔랭','미드',13,30,40,'Platinum',44,'42'),(453,'나쵸453',2,'솔랭','미드',0,111,57,'Platinum',142,'65'),(454,'너구리454',3,'솔랭','미드',4,40,28,'Platinum',97,'57'),(455,'아몬드455',4,'솔랭','미드',6,164,25,'Platinum',32,'86'),(456,'땅콩456',5,'솔랭','미드',5,164,33,'Platinum',137,'82'),(457,'치즈457',6,'솔랭','미드',6,41,3,'Platinum',109,'91'),(458,'호떡458',7,'솔랭','미드',1,112,69,'Platinum',106,'61'),(459,'만두459',8,'솔랭','미드',4,155,80,'Platinum',175,'65'),(460,'대파460',9,'솔랭','미드',4,136,1,'Platinum',75,'98'),(461,'부엉이461',10,'솔랭','미드',5,6,11,'Platinum',121,'33'),(462,'프로462',11,'솔랭','미드',14,96,5,'Platinum',51,'94'),(463,'록맨463',12,'솔랭','미드',10,165,98,'Platinum',162,'62'),(464,'호구맨464',13,'솔랭','미드',10,86,22,'Platinum',179,'78'),(465,'레이저465',14,'솔랭','미드',7,159,32,'Platinum',80,'82'),(466,'고독466',15,'솔랭','미드',2,42,10,'Platinum',134,'79'),(467,'저격467',16,'솔랭','미드',7,179,16,'Platinum',99,'91'),(468,'달님468',17,'솔랭','미드',1,25,14,'Platinum',65,'62'),(469,'더힐469',18,'솔랭','미드',12,68,28,'Platinum',149,'70'),(470,'놀고있네470',19,'솔랭','미드',0,76,6,'Platinum',70,'91'),(471,'프리미어471',20,'솔랭','미드',7,34,66,'Platinum',172,'33'),(472,'메이트472',21,'솔랭','미드',7,166,14,'Platinum',171,'91'),(473,'바른마음473',22,'솔랭','미드',1,47,74,'Platinum',159,'38'),(474,'백구474',23,'솔랭','미드',12,6,92,'Platinum',104,'6'),(475,'잇츠475',0,'솔랭','원딜',12,75,113,'Platinum',164,'39'),(476,'아메리카노476',1,'솔랭','원딜',10,39,8,'Platinum',177,'81'),(477,'고고고고477',2,'솔랭','원딜',14,75,49,'Platinum',62,'60'),(478,'오렌지피클478',3,'솔랭','원딜',12,19,101,'Platinum',53,'15'),(479,'땡땡이479',4,'솔랭','원딜',4,148,137,'Platinum',47,'51'),(480,'월계수480',5,'솔랭','원딜',12,90,39,'Platinum',47,'69'),(481,'라이트481',6,'솔랭','원딜',5,78,122,'Platinum',65,'38'),(482,'테슬라482',7,'솔랭','원딜',5,76,13,'Platinum',155,'84'),(483,'실루엣483',8,'솔랭','원딜',9,141,63,'Platinum',100,'68'),(484,'시계484',9,'솔랭','원딜',1,45,34,'Platinum',156,'56'),(485,'레전드485',10,'솔랭','원딜',8,38,86,'Platinum',152,'30'),(486,'결정486',11,'솔랭','원딜',8,19,135,'Platinum',112,'12'),(487,'시즌487',12,'솔랭','원딜',0,18,138,'Platinum',73,'11'),(488,'뉴비488',13,'솔랭','원딜',9,35,61,'Platinum',149,'36'),(489,'버드489',14,'솔랭','원딜',13,50,69,'Platinum',47,'41'),(490,'열차490',15,'솔랭','원딜',10,44,14,'Platinum',60,'74'),(491,'다이아몬드491',16,'솔랭','원딜',10,87,94,'Platinum',128,'47'),(492,'전기피카츄492',17,'솔랭','원딜',5,58,9,'Platinum',132,'85'),(493,'윈디감옥493',18,'솔랭','원딜',10,23,89,'Platinum',96,'20'),(494,'빌런맨494',19,'솔랭','원딜',5,76,114,'Platinum',54,'39'),(495,'데빌495',20,'솔랭','원딜',10,44,25,'Platinum',103,'62'),(496,'바이바이496',21,'솔랭','원딜',6,145,51,'Platinum',173,'73'),(497,'호시탐탐497',22,'솔랭','원딜',1,119,142,'Platinum',77,'45'),(498,'레이븐498',23,'솔랭','원딜',2,56,5,'Platinum',138,'90'),(499,'세트499',0,'솔랭','서포터',7,8,23,'Platinum',129,'25'),(500,'물범500',1,'솔랭','서포터',14,94,98,'Platinum',50,'48'),(501,'극비501',2,'솔랭','서포터',3,62,13,'Platinum',133,'81'),(502,'다이어트502',3,'솔랭','서포터',6,33,123,'Platinum',38,'21'),(503,'풀피503',4,'솔랭','서포터',7,68,123,'Platinum',60,'35'),(504,'레나504',5,'솔랭','서포터',1,111,38,'Platinum',158,'74'),(505,'야채505',6,'솔랭','서포터',0,6,66,'Platinum',129,'8'),(506,'푸른점506',7,'솔랭','서포터',14,12,12,'Platinum',141,'48'),(507,'푸른곰팡이507',8,'솔랭','서포터',9,25,88,'Platinum',139,'21'),(508,'청둥오리508',9,'솔랭','서포터',4,68,78,'Platinum',94,'46'),(509,'아이스크림509',10,'솔랭','서포터',9,33,83,'Platinum',171,'28'),(510,'대나무510',11,'솔랭','서포터',3,16,130,'Platinum',92,'10'),(511,'바이올린511',12,'솔랭','서포터',5,2,74,'Platinum',71,'2'),(512,'바이올렛512',13,'솔랭','서포터',13,62,87,'Platinum',49,'41'),(513,'인터스텔라513',14,'솔랭','서포터',9,102,97,'Platinum',151,'51'),(514,'팽이514',15,'솔랭','서포터',6,32,19,'Platinum',127,'61'),(515,'토템515',16,'솔랭','서포터',2,148,86,'Platinum',155,'62'),(516,'나나516',17,'솔랭','서포터',9,137,125,'Platinum',65,'52'),(517,'보라돌이517',18,'솔랭','서포터',9,65,99,'Platinum',129,'39'),(518,'뚜비518',19,'솔랭','서포터',4,2,15,'Platinum',120,'11'),(519,'뽀오519',20,'솔랭','서포터',9,69,2,'Platinum',34,'95'),(520,'악어새520',21,'솔랭','서포터',2,102,55,'Platinum',79,'64'),(521,'마법전사521',22,'솔랭','서포터',13,119,131,'Platinum',114,'47'),(522,'나무늘보522',23,'솔랭','서포터',14,0,56,'Platinum',152,'0'),(523,'범고래523',0,'솔랭','정글',2,129,27,'Platinum',91,'82'),(524,'고래밥524',1,'솔랭','정글',1,52,26,'Platinum',118,'65'),(525,'마라치킨525',2,'솔랭','정글',11,128,110,'Platinum',136,'53'),(526,'사파리526',3,'솔랭','정글',11,17,57,'Platinum',148,'22'),(527,'비둘기527',4,'솔랭','정글',5,84,97,'Platinum',152,'46'),(528,'포카리스웨트528',5,'솔랭','정글',6,144,17,'Platinum',136,'88'),(529,'차이나팜529',6,'솔랭','정글',3,7,56,'Platinum',47,'10'),(530,'파머빵530',7,'솔랭','정글',10,110,80,'Platinum',95,'57'),(531,'단판빵을531',8,'솔랭','정글',14,70,112,'Platinum',154,'38'),(532,'다비켜라제발532',9,'솔랭','정글',10,49,59,'Platinum',158,'44'),(533,'나는슈퍼원더풀533',10,'솔랭','정글',8,149,117,'Platinum',149,'55'),(534,'딜러자동차534',11,'솔랭','정글',10,140,51,'Platinum',91,'72'),(535,'뭘파는건데535',12,'솔랭','정글',10,136,75,'Platinum',126,'64'),(536,'왜그러는데536',13,'솔랭','정글',9,119,69,'Platinum',30,'62'),(537,'뭐하는건데537',14,'솔랭','정글',14,141,46,'Platinum',43,'75'),(538,'아진짜이거538',15,'솔랭','정글',12,108,104,'Platinum',94,'50'),(539,'언제까지539',16,'솔랭','정글',3,46,69,'Platinum',163,'39'),(540,'다하는건가540',17,'솔랭','정글',11,57,76,'Platinum',52,'42'),(541,'과연나는541',18,'솔랭','정글',14,63,88,'Platinum',42,'41'),(542,'오늘어떤542',19,'솔랭','정글',11,100,86,'Platinum',175,'53'),(543,'아이디를543',20,'솔랭','정글',10,132,103,'Platinum',117,'55'),(544,'받을까소음544',21,'솔랭','정글',5,117,126,'Platinum',34,'47'),(545,'야간대장545',22,'솔랭','정글',8,129,118,'Platinum',87,'52'),(546,'절약모드546',23,'솔랭','정글',12,54,65,'Platinum',156,'45'),(547,'아바타547',0,'솔랭','탑',4,211,102,'Unranked',40,'67'),(548,'우유548',1,'솔랭','탑',2,210,107,'Unranked',151,'66'),(549,'커피549',2,'솔랭','탑',13,150,111,'Unranked',156,'57'),(550,'모카550',3,'솔랭','탑',13,145,120,'Unranked',148,'54'),(551,'초코551',4,'솔랭','탑',11,133,100,'Unranked',91,'56'),(552,'브라우니552',5,'솔랭','탑',4,153,88,'Unranked',132,'63'),(553,'댕댕이553',6,'솔랭','탑',3,75,70,'Unranked',58,'51'),(554,'삐삐554',7,'솔랭','탑',4,16,36,'Unranked',164,'30'),(555,'뚠뚠555',8,'솔랭','탑',10,176,68,'Unranked',168,'71'),(556,'강냉이556',9,'솔랭','탑',10,157,87,'Unranked',168,'64'),(557,'잠만보557',10,'솔랭','탑',3,3,45,'Unranked',155,'6'),(558,'안드로메다558',11,'솔랭','탑',1,46,79,'Unranked',94,'36'),(559,'프라하559',12,'솔랭','탑',11,58,5,'Unranked',126,'90'),(560,'고인물560',13,'솔랭','탑',7,82,89,'Unranked',166,'47'),(561,'갑분싸561',14,'솔랭','탑',4,44,43,'Unranked',123,'50'),(562,'인싸562',15,'솔랭','탑',14,99,20,'Unranked',90,'82'),(563,'존잘러563',16,'솔랭','탑',14,100,91,'Unranked',49,'52'),(564,'곰스564',17,'솔랭','탑',13,12,56,'Unranked',95,'17'),(565,'바운스565',18,'솔랭','탑',9,132,59,'Unranked',151,'68'),(566,'뚱이566',19,'솔랭','탑',6,1,23,'Unranked',141,'4'),(567,'복서567',20,'솔랭','탑',5,31,7,'Unranked',71,'79'),(568,'해충박멸568',21,'솔랭','탑',8,180,29,'Unranked',52,'85'),(569,'디스코드569',22,'솔랭','탑',8,154,98,'Unranked',170,'60'),(570,'후라이팬570',23,'솔랭','탑',3,117,97,'Unranked',64,'54'),(571,'존버571',0,'솔랭','미드',6,28,77,'Unranked',79,'26'),(572,'꿀꿀이572',1,'솔랭','미드',6,91,96,'Unranked',173,'48'),(573,'나쵸573',2,'솔랭','미드',13,87,30,'Unranked',148,'73'),(574,'너구리574',3,'솔랭','미드',2,41,12,'Unranked',43,'75'),(575,'아몬드575',4,'솔랭','미드',4,199,61,'Unranked',43,'76'),(576,'땅콩576',5,'솔랭','미드',11,15,53,'Unranked',56,'21'),(577,'치즈577',6,'솔랭','미드',2,90,65,'Unranked',119,'57'),(578,'호떡578',7,'솔랭','미드',4,187,70,'Unranked',100,'72'),(579,'만두579',8,'솔랭','미드',2,146,54,'Unranked',113,'72'),(580,'대파580',9,'솔랭','미드',13,105,98,'Unranked',83,'51'),(581,'부엉이581',10,'솔랭','미드',1,74,89,'Unranked',49,'45'),(582,'프로582',11,'솔랭','미드',11,70,8,'Unranked',115,'88'),(583,'록맨583',12,'솔랭','미드',7,68,47,'Unranked',98,'58'),(584,'호구맨584',13,'솔랭','미드',1,67,26,'Unranked',115,'71'),(585,'레이저585',14,'솔랭','미드',2,62,75,'Unranked',102,'44'),(586,'고독586',15,'솔랭','미드',8,173,6,'Unranked',137,'96'),(587,'저격587',16,'솔랭','미드',4,140,33,'Unranked',51,'80'),(588,'달님588',17,'솔랭','미드',13,113,82,'Unranked',112,'57'),(589,'더힐589',18,'솔랭','미드',6,88,73,'Unranked',76,'54'),(590,'놀고있네590',19,'솔랭','미드',6,67,47,'Unranked',167,'58'),(591,'프리미어591',20,'솔랭','미드',14,75,44,'Unranked',127,'62'),(592,'메이트592',21,'솔랭','미드',6,23,24,'Unranked',106,'47'),(593,'바른마음593',22,'솔랭','미드',4,173,61,'Unranked',119,'73'),(594,'백구594',23,'솔랭','미드',1,90,42,'Unranked',96,'67'),(595,'잇츠595',0,'솔랭','원딜',8,118,97,'Unranked',96,'54'),(596,'아메리카노596',1,'솔랭','원딜',9,132,70,'Unranked',162,'65'),(597,'고고고고597',2,'솔랭','원딜',8,103,6,'Unranked',41,'93'),(598,'오렌지피클598',3,'솔랭','원딜',13,23,96,'Unranked',140,'19'),(599,'땡땡이599',4,'솔랭','원딜',13,111,120,'Unranked',96,'47'),(600,'월계수600',5,'솔랭','원딜',9,117,75,'Unranked',31,'60'),(601,'라이트601',6,'솔랭','원딜',6,24,46,'Unranked',139,'33'),(602,'테슬라602',7,'솔랭','원딜',3,9,57,'Unranked',122,'13'),(603,'실루엣603',8,'솔랭','원딜',11,107,65,'Unranked',163,'61'),(604,'시계604',9,'솔랭','원딜',5,5,132,'Unranked',120,'3'),(605,'레전드605',10,'솔랭','원딜',5,46,131,'Unranked',80,'25'),(606,'결정606',11,'솔랭','원딜',11,71,112,'Unranked',160,'38'),(607,'시즌607',12,'솔랭','원딜',10,45,42,'Unranked',82,'51'),(608,'뉴비608',13,'솔랭','원딜',5,76,102,'Unranked',51,'42'),(609,'버드609',14,'솔랭','원딜',10,133,62,'Unranked',128,'67'),(610,'열차610',15,'솔랭','원딜',4,58,107,'Unranked',159,'34'),(611,'다이아몬드611',16,'솔랭','원딜',7,62,138,'Unranked',81,'30'),(612,'전기피카츄612',17,'솔랭','원딜',8,53,4,'Unranked',49,'91'),(613,'윈디감옥613',18,'솔랭','원딜',4,9,35,'Unranked',121,'20'),(614,'빌런맨614',19,'솔랭','원딜',11,147,30,'Unranked',130,'82'),(615,'데빌615',20,'솔랭','원딜',0,12,121,'Unranked',109,'8'),(616,'바이바이616',21,'솔랭','원딜',11,119,81,'Unranked',124,'59'),(617,'호시탐탐617',22,'솔랭','원딜',10,48,0,'Unranked',115,'97'),(618,'레이븐618',23,'솔랭','원딜',2,7,35,'Unranked',174,'16'),(619,'세트619',0,'솔랭','서포터',12,2,59,'Unranked',43,'3'),(620,'물범620',1,'솔랭','서포터',10,138,62,'Unranked',113,'68'),(621,'극비621',2,'솔랭','서포터',13,47,51,'Unranked',105,'47'),(622,'다이어트622',3,'솔랭','서포터',8,115,119,'Unranked',160,'48'),(623,'풀피623',4,'솔랭','서포터',13,104,14,'Unranked',155,'87'),(624,'레나624',5,'솔랭','서포터',0,57,93,'Unranked',117,'37'),(625,'야채625',6,'솔랭','서포터',4,145,148,'Unranked',89,'49'),(626,'푸른점626',7,'솔랭','서포터',6,3,24,'Unranked',63,'10'),(627,'푸른곰팡이627',8,'솔랭','서포터',5,112,37,'Unranked',171,'74'),(628,'청둥오리628',9,'솔랭','서포터',8,2,47,'Unranked',34,'4'),(629,'아이스크림629',10,'솔랭','서포터',12,81,115,'Unranked',80,'41'),(630,'대나무630',11,'솔랭','서포터',3,33,120,'Unranked',115,'21'),(631,'바이올린631',12,'솔랭','서포터',10,52,48,'Unranked',159,'51'),(632,'바이올렛632',13,'솔랭','서포터',11,86,135,'Unranked',119,'38'),(633,'인터스텔라633',14,'솔랭','서포터',9,119,39,'Unranked',89,'74'),(634,'팽이634',15,'솔랭','서포터',0,137,122,'Unranked',58,'52'),(635,'토템635',16,'솔랭','서포터',4,49,28,'Unranked',142,'62'),(636,'나나636',17,'솔랭','서포터',5,144,36,'Unranked',58,'79'),(637,'보라돌이637',18,'솔랭','서포터',13,49,139,'Unranked',134,'25'),(638,'뚜비638',19,'솔랭','서포터',8,96,62,'Unranked',167,'60'),(639,'뽀오639',20,'솔랭','서포터',14,26,93,'Unranked',104,'21'),(640,'악어새640',21,'솔랭','서포터',2,90,18,'Unranked',137,'82'),(641,'마법전사641',22,'솔랭','서포터',1,123,111,'Unranked',46,'52'),(642,'나무늘보642',23,'솔랭','서포터',11,36,148,'Unranked',90,'19'),(643,'범고래643',0,'솔랭','정글',10,32,16,'Unranked',130,'65'),(644,'고래밥644',1,'솔랭','정글',3,135,27,'Unranked',53,'82'),(645,'마라치킨645',2,'솔랭','정글',14,29,65,'Unranked',143,'30'),(646,'사파리646',3,'솔랭','정글',3,91,110,'Unranked',80,'45'),(647,'비둘기647',4,'솔랭','정글',4,126,1,'Unranked',88,'98'),(648,'포카리스웨트648',5,'솔랭','정글',12,94,17,'Unranked',173,'83'),(649,'차이나팜649',6,'솔랭','정글',2,82,129,'Unranked',119,'38'),(650,'파머빵650',7,'솔랭','정글',6,100,112,'Unranked',47,'46'),(651,'단판빵을651',8,'솔랭','정글',7,110,63,'Unranked',150,'63'),(652,'다비켜라제발652',9,'솔랭','정글',4,139,56,'Unranked',127,'70'),(653,'나는슈퍼원더풀653',10,'솔랭','정글',13,12,42,'Unranked',157,'21'),(654,'딜러자동차654',11,'솔랭','정글',9,24,147,'Unranked',76,'13'),(655,'뭘파는건데655',12,'솔랭','정글',5,63,24,'Unranked',179,'71'),(656,'왜그러는데656',13,'솔랭','정글',0,81,35,'Unranked',37,'69'),(657,'뭐하는건데657',14,'솔랭','정글',14,82,5,'Unranked',66,'93'),(658,'아진짜이거658',15,'솔랭','정글',10,81,88,'Unranked',43,'47'),(659,'언제까지659',16,'솔랭','정글',9,47,121,'Unranked',137,'27'),(660,'다하는건가660',17,'솔랭','정글',2,14,9,'Unranked',75,'58'),(661,'과연나는661',18,'솔랭','정글',12,5,148,'Unranked',85,'3'),(662,'오늘어떤662',19,'솔랭','정글',10,124,25,'Unranked',171,'82'),(663,'아이디를663',20,'솔랭','정글',0,57,60,'Unranked',119,'48'),(664,'받을까소음664',21,'솔랭','정글',1,127,9,'Unranked',53,'92'),(665,'야간대장665',22,'솔랭','정글',4,111,80,'Unranked',30,'57'),(666,'절약모드666',23,'솔랭','정글',3,67,95,'Unranked',111,'41'),(669,'가가대소669',0,'솔랭','탑',1,61,38,'Gold',159,'61'),(670,'가가문전670',1,'솔랭','탑',2,30,20,'Gold',147,'58'),(671,'가가호호671',2,'솔랭','탑',3,69,77,'Gold',167,'46'),(672,'가감지인672',3,'솔랭','탑',4,84,84,'Gold',129,'49'),(673,'가거지지673',4,'솔랭','탑',5,6,5,'Gold',112,'50'),(674,'가고문적674',5,'솔랭','탑',6,30,20,'Gold',132,'58'),(675,'가고문헌675',6,'솔랭','탑',7,38,37,'Gold',142,'50'),(676,'가공가소676',7,'솔랭','탑',8,30,20,'Gold',155,'58'),(677,'가공망상677',8,'솔랭','탑',9,96,109,'Gold',35,'46'),(678,'가급678',9,'솔랭','탑',10,30,20,'Gold',34,'58'),(679,'인족679',10,'솔랭','탑',11,14,17,'Gold',36,'43'),(680,'가관680',11,'솔랭','탑',12,30,24,'Gold',37,'54'),(681,'가담681',12,'솔랭','탑',13,6,11,'Gold',44,'33'),(682,'항설682',13,'솔랭','탑',14,14,12,'Gold',39,'51'),(683,'가담 항어683',14,'솔랭','탑',15,13,12,'Gold',36,'50'),(684,'항 어684',15,'솔랭','탑',16,50,53,'Gold',41,'48'),(685,'가돈685',16,'솔랭','탑',17,33,38,'Gold',69,'45'),(686,'가동 가서686',17,'솔랭','탑',18,49,49,'Gold',59,'49'),(687,'가 서687',18,'솔랭','탑',19,87,65,'Gold',312,'56'),(688,'가동 주졸688',19,'솔랭','탑',20,12,17,'Gold',344,'40'),(689,'주졸689',20,'솔랭','탑',21,12,17,'Gold',359,'40'),(690,'가렴주구690',21,'솔랭','탑',22,30,20,'Gold',369,'58'),(691,'가롱성진691',22,'솔랭','탑',23,137,116,'Gold',419,'53'),(692,'가릉빈가692',23,'솔랭','탑',24,6,4,'Gold',309,'54'),(693,'가무음곡693',0,'솔랭','미드',1,61,38,'Gold',302,'61'),(694,'가문설화694',1,'솔랭','미드',2,30,20,'Gold',412,'58'),(695,'설화695',2,'솔랭','미드',3,69,77,'Gold',127,'46'),(696,'음 곡696',3,'솔랭','미드',4,84,84,'Gold',155,'49'),(697,'가 신697',4,'솔랭','미드',5,6,5,'Gold',175,'50'),(698,'가신지인698',5,'솔랭','미드',6,30,20,'Gold',133,'58'),(699,'감 이699',6,'솔랭','미드',7,38,37,'Gold',46,'50'),(700,'수통700',7,'솔랭','미드',8,30,20,'Gold',84,'58'),(701,'감정 선갈701',8,'솔랭','미드',9,14,17,'Gold',71,'43'),(702,'감탄고토702',9,'솔랭','미드',10,30,24,'Gold',85,'54'),(703,'내친구꼬마자동차703',10,'솔랭','미드',11,50,53,'Gold',88,'48'),(704,'꼬마자동차704',11,'솔랭','미드',12,12,17,'Gold',92,'40'),(705,'강 류705',12,'솔랭','미드',13,12,17,'Gold',133,'40'),(706,'석부전706',13,'솔랭','미드',14,96,109,'Gold',122,'46'),(707,'강 목707',14,'솔랭','미드',15,14,12,'Gold',140,'51'),(708,'수생708',15,'솔랭','미드',16,13,12,'Gold',145,'50'),(709,'개 시709',16,'솔랭','미드',17,49,49,'Gold',167,'49'),(710,'귀 류710',17,'솔랭','미드',18,87,65,'Gold',119,'56'),(711,'갱무도리711',18,'솔랭','미드',19,12,17,'Gold',35,'40'),(712,'부릎뜨니숲이였어712',19,'솔랭','미드',20,30,20,'Gold',214,'58'),(713,'월화술먹구토일713',20,'솔랭','미드',21,137,116,'Gold',341,'53'),(714,'옥수수 콧수염차714',21,'솔랭','미드',22,30,20,'Gold',132,'58'),(715,'찰옥수수 수염차715',22,'솔랭','미드',23,137,116,'Gold',111,'53'),(716,'진관홀 왕돈가스716',23,'솔랭','미드',24,6,4,'Gold',144,'54'),(717,'누리관 왕돈까스717',0,'솔랭','원딜',1,61,38,'Gold',441,'61'),(718,'누리관 대왕만두718',1,'솔랭','원딜',2,30,20,'Gold',132,'58'),(719,'누리관 해물라면 719',2,'솔랭','원딜',3,69,77,'Gold',155,'46'),(720,'혜당관 컵밥720',3,'솔랭','원딜',4,84,84,'Gold',179,'49'),(721,'바롬관 학식 맛없다721',4,'솔랭','원딜',5,6,5,'Gold',132,'50'),(722,'란닝맨722',5,'솔랭','원딜',6,30,20,'Gold',144,'58'),(723,'광개토관723',6,'솔랭','원딜',7,38,37,'Gold',132,'50'),(724,'모짜르트홀724',7,'솔랭','원딜',8,30,20,'Gold',35,'58'),(725,'영실관725',8,'솔랭','원딜',9,14,17,'Gold',37,'43'),(726,'세종관726',9,'솔랭','원딜',10,30,24,'Gold',39,'54'),(727,'원자력 발사727',10,'솔랭','원딜',11,12,17,'Gold',44,'40'),(728,'전자전자 왕전자728',11,'솔랭','원딜',12,96,109,'Gold',41,'46'),(729,'혜당관 왕만두729',12,'솔랭','원딜',13,137,120,'Gold',43,'53'),(730,'혜당관 김치만두730',13,'솔랭','원딜',14,12,17,'Gold',56,'40'),(731,'바롬관 육회비빔밥731',14,'솔랭','원딜',15,12,17,'Gold',58,'40'),(732,'세종관 사무실732',15,'솔랭','원딜',16,82,82,'Gold',102,'49'),(733,'꾸마 자동차733',16,'솔랭','원딜',17,83,82,'Gold',120,'50'),(734,'꼬마 비행기734',17,'솔랭','원딜',18,84,82,'Gold',159,'50'),(735,'꼬마꼬마 왕꼬마735',18,'솔랭','원딜',19,33,33,'Gold',133,'49'),(736,'레오날두736',19,'솔랭','원딜',20,34,33,'Gold',76,'50'),(737,'크리수티아누 후날두737',20,'솔랭','원딜',21,120,120,'Gold',56,'49'),(738,'리오넬 몇시야738',21,'솔랭','원딜',22,121,120,'Gold',48,'50'),(739,'앨릭스 니아코739',22,'솔랭','원딜',23,96,109,'Gold',39,'46'),(740,'조 두두740',23,'솔랭','원딜',24,12,17,'Gold',45,'40'),(741,'까비 드릴조741',0,'솔랭','서포터',1,65,42,'Gold',79,'60'),(742,'디그디그 디그다742',1,'솔랭','서포터',2,30,20,'Gold',81,'58'),(743,'니 램프티743',2,'솔랭','서포터',3,12,17,'Gold',88,'40'),(744,'존 멘사744',3,'솔랭','서포터',4,84,84,'Gold',99,'49'),(745,'제프 시룹745',4,'솔랭','서포터',5,12,17,'Gold',103,'40'),(746,'조르당 아유746',5,'솔랭','서포터',6,12,17,'Gold',197,'40'),(747,'등짝 스매싱747',6,'솔랭','서포터',7,44,44,'Gold',214,'49'),(748,'미드미드트롤748',7,'솔랭','서포터',8,33,33,'Gold',217,'49'),(749,'메롱메롱퍼블749',8,'솔랭','서포터',9,33,32,'Gold',238,'50'),(750,'숲속에 바론왕750',9,'솔랭','서포터',10,12,17,'Gold',114,'40'),(751,'블링블링 왕블링751',10,'솔랭','서포터',11,30,20,'Gold',512,'58'),(752,'부푸러 콜라맛752',11,'솔랭','서포터',12,83,82,'Gold',117,'50'),(753,'꼬북좌753',12,'솔랭','서포터',13,121,120,'Gold',142,'50'),(754,'메보좌754',13,'솔랭','서포터',14,13,12,'Gold',157,'50'),(755,'단발좌755',14,'솔랭','서포터',15,12,17,'Gold',188,'40'),(756,'왕눈좌756',15,'솔랭','서포터',16,12,17,'Gold',36,'40'),(757,'노원구 비둘기757',16,'솔랭','서포터',17,96,109,'Gold',67,'46'),(758,'상계동 비둘기아빠758',17,'솔랭','서포터',18,12,17,'Gold',77,'40'),(759,'노원구 맛집759',18,'솔랭','서포터',19,30,24,'Gold',138,'54'),(760,'빅데이터 전문가760',19,'솔랭','서포터',20,12,17,'Gold',139,'40'),(761,'계양구 맛집761',20,'솔랭','서포터',21,12,17,'Gold',124,'40'),(762,'가경자762',21,'솔랭','서포터',21,12,17,'Gold',333,'40'),(763,'가는보라색우무763',22,'솔랭','서포터',8,12,17,'Gold',32,'40'),(764,'가는쑥부쟁이764',23,'솔랭','서포터',7,12,17,'Gold',39,'40'),(765,'가는잎벚나무765',0,'솔랭','정글',7,65,42,'Gold',129,'60'),(766,'가두배추766',1,'솔랭','정글',7,30,20,'Gold',144,'58'),(767,'가라767',2,'솔랭','정글',7,12,17,'Gold',137,'40'),(768,'가락풀768',3,'솔랭','정글',8,84,84,'Gold',166,'49'),(769,'가랑잎769',4,'솔랭','정글',3,12,17,'Gold',142,'40'),(770,'가막살나무770',5,'솔랭','정글',4,12,17,'Gold',31,'40'),(771,'가문비771',6,'솔랭','정글',3,44,44,'Gold',39,'49'),(772,'가새잎머루772',7,'솔랭','정글',5,121,120,'Gold',41,'50'),(773,'가시나무773',8,'솔랭','정글',4,30,24,'Gold',45,'54'),(774,'가시비름774',9,'솔랭','정글',3,12,17,'Gold',59,'40'),(775,'가을배추775',10,'솔랭','정글',7,34,33,'Gold',61,'50'),(776,'가죽나무776',11,'솔랭','정글',8,12,17,'Gold',46,'40'),(777,'가 지777',12,'솔랭','정글',8,87,65,'Gold',35,'56'),(778,'각시붓꽃778',13,'솔랭','정글',12,14,12,'Gold',39,'51'),(779,'감 람779',14,'솔랭','정글',13,6,5,'Gold',441,'50'),(780,'감 자780',15,'솔랭','정글',14,30,20,'Gold',398,'58'),(781,'감 당781',16,'솔랭','정글',14,38,37,'Gold',342,'50'),(782,'감 저782',17,'솔랭','정글',2,12,17,'Gold',333,'40'),(783,'강원 고사리783',18,'솔랭','정글',6,83,82,'Gold',318,'50'),(784,'개 과784',19,'솔랭','정글',6,12,17,'Gold',391,'40'),(785,'개나리꽃785',20,'솔랭','정글',8,84,82,'Gold',492,'50'),(786,'개양귀비786',21,'솔랭','정글',8,6,4,'Gold',64,'54'),(787,'바닐라 와플787',22,'솔랭','정글',7,12,17,'Gold',148,'40'),(788,'abc 초콜렛마트788',23,'솔랭','정글',7,33,38,'Gold',309,'45'),(794,'굿또',0,'솔랭','선호하는 포지션이 없습니다.',0,0,0,'Unranked',46,'0'),(795,'개불김',19,'all','서포터',0,34,37,'Gold',374,'47'),(797,'개구리꾀꼬닥',19,'솔랭','선호하는 포지션이 없습니다.',0,5,9,'Gold',202,'Win Ratio 36%'),(800,'평양산검은콩',19,'솔랭','선호하는 포지션이 없습니다.',1,0,0,'Unranked',247,'승률 0%'),(803,'숏다리의 꿈',19,'솔랭','선호하는 포지션이 없습니다.',1,0,0,'Unranked',4,'승률 0%'),(804,'나는즐겜러당',15,'솔랭','선호하는 포지션이 없습니다.',0,0,0,'Unranked',5,'승률 0%'),(806,'JSDD SUL',18,'솔랭','미드',0,31,45,'Gold',399,'Win Ratio 41%'),(808,'꼬마자동차 붕봉',13,'솔랭','원딜',0,10,11,'Gold',348,'Win Ratio 48%');
/*!40000 ALTER TABLE `member_for_recommend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memberchatroomlist`
--

DROP TABLE IF EXISTS `memberchatroomlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `memberchatroomlist` (
  `room_no` int NOT NULL,
  `id` varchar(100) NOT NULL,
  `nick_name` varchar(100) DEFAULT NULL,
  `room_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`room_no`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memberchatroomlist`
--

LOCK TABLES `memberchatroomlist` WRITE;
/*!40000 ALTER TABLE `memberchatroomlist` DISABLE KEYS */;
INSERT INTO `memberchatroomlist` VALUES (1,'ybj0749','나는즐겜러당','소환사의협곡승리'),(5,'giga1422','숏다리의꿈','가자가자'),(5,'giga1615','데롱디롱','가자가자'),(5,'hossi','꼬마자동차 붕봉','가자가자');
/*!40000 ALTER TABLE `memberchatroomlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-08  8:17:28
