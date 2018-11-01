/*
 Navicat Premium Data Transfer

 Source Server         : oldboy
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : bbs

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 13/10/2018 09:30:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (11, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (12, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (13, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (14, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (15, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (16, 'Can add article up down', 6, 'add_articleupdown');
INSERT INTO `auth_permission` VALUES (17, 'Can change article up down', 6, 'change_articleupdown');
INSERT INTO `auth_permission` VALUES (18, 'Can delete article up down', 6, 'delete_articleupdown');
INSERT INTO `auth_permission` VALUES (19, 'Can add blog', 7, 'add_blog');
INSERT INTO `auth_permission` VALUES (20, 'Can change blog', 7, 'change_blog');
INSERT INTO `auth_permission` VALUES (21, 'Can delete blog', 7, 'delete_blog');
INSERT INTO `auth_permission` VALUES (22, 'Can add user', 8, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (23, 'Can change user', 8, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (24, 'Can delete user', 8, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (25, 'Can add article', 9, 'add_article');
INSERT INTO `auth_permission` VALUES (26, 'Can change article', 9, 'change_article');
INSERT INTO `auth_permission` VALUES (27, 'Can delete article', 9, 'delete_article');
INSERT INTO `auth_permission` VALUES (28, 'Can add article2 tag', 10, 'add_article2tag');
INSERT INTO `auth_permission` VALUES (29, 'Can change article2 tag', 10, 'change_article2tag');
INSERT INTO `auth_permission` VALUES (30, 'Can delete article2 tag', 10, 'delete_article2tag');
INSERT INTO `auth_permission` VALUES (31, 'Can add tag', 11, 'add_tag');
INSERT INTO `auth_permission` VALUES (32, 'Can change tag', 11, 'change_tag');
INSERT INTO `auth_permission` VALUES (33, 'Can delete tag', 11, 'delete_tag');
INSERT INTO `auth_permission` VALUES (34, 'Can add article detail', 12, 'add_articledetail');
INSERT INTO `auth_permission` VALUES (35, 'Can change article detail', 12, 'change_articledetail');
INSERT INTO `auth_permission` VALUES (36, 'Can delete article detail', 12, 'delete_articledetail');
INSERT INTO `auth_permission` VALUES (37, 'Can add category', 13, 'add_category');
INSERT INTO `auth_permission` VALUES (38, 'Can change category', 13, 'change_category');
INSERT INTO `auth_permission` VALUES (39, 'Can delete category', 13, 'delete_category');
INSERT INTO `auth_permission` VALUES (40, 'Can add comment', 14, 'add_comment');
INSERT INTO `auth_permission` VALUES (41, 'Can change comment', 14, 'change_comment');
INSERT INTO `auth_permission` VALUES (42, 'Can delete comment', 14, 'delete_comment');

-- ----------------------------
-- Table structure for blog_article
-- ----------------------------
DROP TABLE IF EXISTS `blog_article`;
CREATE TABLE `blog_article`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `category_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `comment_count` int(11) NOT NULL,
  `down_count` int(11) NOT NULL,
  `up_count` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  INDEX `blog_article_category_id_7e38f15e_fk_blog_category_nid`(`category_id`) USING BTREE,
  INDEX `blog_article_user_id_5beb0cc1_fk_blog_userinfo_nid`(`user_id`) USING BTREE,
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_nid` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_article_user_id_5beb0cc1_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_article
-- ----------------------------
INSERT INTO `blog_article` VALUES (1, '见证中国团队夺冠 权威媒体报道亚运会盛事', '在今天(8月29日)下午，2018雅加达-巨港亚运会(以下简称：雅加达亚运会)电子体育表演项目《英雄联盟》迎来了总决赛阶段。中国团队和韩国队再度迎来交锋，最终，中国团队的选手们发挥出色，以3-1击败韩国队，摘获了首届亚运会电竞项目金牌!', '2018-09-01 16:17:00.000000', 1, 1, 0, 0, 0);
INSERT INTO `blog_article` VALUES (2, '厂长助EDG锁定第二 季后赛名额悬念尚存', '9月1日，2018LPL夏季赛常规赛第十一周比赛来到倒数第二比赛日的对决。在当天的两场比赛中，EDG依靠决胜局Clearlove赵信的节奏带动，以2:1的比分击败FPX，锁定了常规赛西部第二的席位。而在第二场Snake的季后赛晋级之战中，他们没有顶住压力，以0:2的比分输给表现优异的WE。本场比赛Snake的失利，将西部季后赛名额归属悬念留到了常规赛最后一个比赛日。', '2018-09-01 16:19:00.000000', 1, 1, 0, 0, 0);
INSERT INTO `blog_article` VALUES (3, 'Reddit热议亚运会：Uzi就是世界第一', '恭喜亚运会LOL项目中国队喜提金牌，这场精彩的比赛也在国外引起了很大的关注，来看下reddit网友是怎么评价的吧。', '2018-09-01 16:20:00.000000', 1, 1, 0, 0, 0);
INSERT INTO `blog_article` VALUES (4, '网友热议SKT无缘S8：给Faker买个靠前的座位', '北京时间9月12日，LCK S8预选赛正式开始，首轮由S7冠亚军GEN对战SKT，双方鏖战五局，最终GEN 3-2击败SKT成功挺进下轮，而SKT则宣告着正式无缘S8。赛后网友们开始了热烈讨论。', '2018-06-16 01:59:00.000000', 1, 1, 0, 0, 0);
INSERT INTO `blog_article` VALUES (5, '詹皇曾屏蔽新队友五年！当事人对此表示有点懵', '北京时间9月16日，据TMZ网站报道，最近，勒布朗-詹姆斯开始在IG上关注新队友贾维尔-麦基，而在这之前，詹姆斯一直是屏蔽麦基的账号。对此，麦基也表示不解，不过他现在和詹姆斯相处得很好。', '2017-11-09 06:00:00.000000', 2, 1, 0, 0, 0);
INSERT INTO `blog_article` VALUES (6, '奥尼尔的这些话 充满着对当今篮球的鄙视', '北京时间9月16日，据《湖人国度》报道，篮球名人堂成员奥尼尔在近日接受采访时表示，如果他在当今NBA打球，他肯定能场均得到40分，甚至是50分。  　　奥尼尔无疑是NBA历史上最具统治力的球员之一，特别是在篮下，但是自从进入21世纪之后，篮球比赛更讲究速度和三分球，这使得一批传统中锋逐渐被淘汰。', '2017-08-09 18:00:00.000000', 1, 1, 0, 0, 1);

-- ----------------------------
-- Table structure for blog_article2tag
-- ----------------------------
DROP TABLE IF EXISTS `blog_article2tag`;
CREATE TABLE `blog_article2tag`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  UNIQUE INDEX `blog_article2tag_article_id_tag_id_b0745f42_uniq`(`article_id`, `tag_id`) USING BTREE,
  INDEX `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid`(`tag_id`) USING BTREE,
  CONSTRAINT `blog_article2tag_article_id_753a2b60_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_article2tag
-- ----------------------------
INSERT INTO `blog_article2tag` VALUES (2, 1, 1);
INSERT INTO `blog_article2tag` VALUES (1, 1, 2);
INSERT INTO `blog_article2tag` VALUES (3, 2, 3);
INSERT INTO `blog_article2tag` VALUES (5, 4, 2);
INSERT INTO `blog_article2tag` VALUES (4, 5, 3);
INSERT INTO `blog_article2tag` VALUES (6, 6, 3);

-- ----------------------------
-- Table structure for blog_articledetail
-- ----------------------------
DROP TABLE IF EXISTS `blog_articledetail`;
CREATE TABLE `blog_articledetail`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  UNIQUE INDEX `article_id`(`article_id`) USING BTREE,
  CONSTRAINT `blog_articledetail_article_id_56993a97_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_articledetail
-- ----------------------------
INSERT INTO `blog_articledetail` VALUES (1, '<div class=\"article __reader_view_article_wrap_3794870597070812__\" id=\"artibody\" data-sudaclick=\"blk_content\">\r\n                     \r\n									<div class=\"img_wrapper\">\r\n					<!--//n.sinaimg.cn/www/transform/297/w640h457/20180916/CL6P-hkahyhx5505155.jpg-->\r\n					<img alt=\"奥尼尔\" src=\"//n.sinaimg.cn/www/transform/297/w640h457/20180916/CL6P-hkahyhx5505155.jpg\">\r\n					<span class=\"img_descr\">奥尼尔</span>\r\n				</div><p>　　北京时间9月16日，据《湖人国度》报道，篮球名人堂成员奥尼尔在近日接受采访时表示，如果他在当今NBA打球，他肯定能场均得到40分，甚至是50分。</p>\r\n<p>　　奥尼尔无疑是NBA历史上最具统治力的球员之一，特别是在篮下，但是自从进入21世纪之后，篮球比赛更讲究速度和三分球，这使得一批传统中锋逐渐被淘汰。</p>\r\n<p>　　对于这种观点，奥尼尔并不认同，而且拿自己来举例。</p>\r\n<p>　　“首先，如果我在这个时代打球，我不会投三分。这不是大个子该做的事情。如果我在这个时代打球，我将会场均得到50分，而且没有罚球。”奥尼尔说道，“我将会场均得到50分，因为现在的球员都没有身体对抗。他们只会抱怨和哭泣。我将会惩罚所有人。所有这些人都在谈论跳投，但是你必须防守我。如果你已经身背三、四次犯规，你无法继续防守我。”</p>\r\n<p>　　“所以，如果我在这个时代打球，我肯定能场均得到40分，非常轻松。”他最后说道。</p>\r\n<p>　　（罗森）</p>\r\n					\r\n\r\n                    <!-- 非定向300*250按钮    17/09  wenjing  begin -->\r\n                    <div id=\"left_hzh_ad\">\r\n                        <!-- <script async charset=\"utf-8\" src=\"//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js\"></script>\r\n                    <script language=\"javascript\" type=\"text/javascript\" src=\"//d2.sina.com.cn/d1images/button/rotator.js\"></script>\r\n                    <script type=\"text/javascript\">\r\n                      (function(){\r\n                        var adScript = document.createElement(\'script\');\r\n                        adScript.src = \'//d1.sina.com.cn/litong/zhitou/sinaads/demo/changwy/link/yl_left_hzh_20160119.js\';\r\n                        document.getElementsByTagName(\'head\')[0].appendChild(adScript);\r\n                        })();\r\n                    </script> -->\r\n\r\n                    </div>\r\n                    <!-- 非定向300*250按钮  end -->\r\n                </div>', 6);

-- ----------------------------
-- Table structure for blog_articleupdown
-- ----------------------------
DROP TABLE IF EXISTS `blog_articleupdown`;
CREATE TABLE `blog_articleupdown`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `is_up` tinyint(1) NOT NULL,
  `article_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  UNIQUE INDEX `blog_articleupdown_article_id_user_id_fa3d0c08_uniq`(`article_id`, `user_id`) USING BTREE,
  INDEX `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid`(`user_id`) USING BTREE,
  CONSTRAINT `blog_articleupdown_article_id_9be1a8a2_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_articleupdown
-- ----------------------------
INSERT INTO `blog_articleupdown` VALUES (28, 1, 6, 1);

-- ----------------------------
-- Table structure for blog_blog
-- ----------------------------
DROP TABLE IF EXISTS `blog_blog`;
CREATE TABLE `blog_blog`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `site` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `theme` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  UNIQUE INDEX `site`(`site`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_blog
-- ----------------------------
INSERT INTO `blog_blog` VALUES (1, 'Ban的个人博客', 'ban', 'ban.css');

-- ----------------------------
-- Table structure for blog_category
-- ----------------------------
DROP TABLE IF EXISTS `blog_category`;
CREATE TABLE `blog_category`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `blog_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  INDEX `blog_category_blog_id_80f0723a_fk_blog_blog_nid`(`blog_id`) USING BTREE,
  CONSTRAINT `blog_category_blog_id_80f0723a_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_category
-- ----------------------------
INSERT INTO `blog_category` VALUES (1, 'LOL', 1);
INSERT INTO `blog_category` VALUES (2, 'NBA', 1);

-- ----------------------------
-- Table structure for blog_comment
-- ----------------------------
DROP TABLE IF EXISTS `blog_comment`;
CREATE TABLE `blog_comment`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `article_id` int(11) NOT NULL,
  `parent_comment_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  INDEX `blog_comment_article_id_3d58bca6_fk_blog_article_nid`(`article_id`) USING BTREE,
  INDEX `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid`(`parent_comment_id`) USING BTREE,
  INDEX `blog_comment_user_id_59a54155_fk_blog_userinfo_nid`(`user_id`) USING BTREE,
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid` FOREIGN KEY (`parent_comment_id`) REFERENCES `blog_comment` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_comment_user_id_59a54155_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_comment
-- ----------------------------
INSERT INTO `blog_comment` VALUES (1, '123', '2018-10-11 23:49:44.592880', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (2, '456', '2018-10-12 00:03:23.718681', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (3, 'aaa', '2018-10-12 00:33:08.095132', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (4, 'bbb', '2018-10-12 00:39:58.502674', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (5, 'ccc', '2018-10-12 00:40:58.733573', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (6, 'ddd', '2018-10-12 00:42:17.955279', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (7, 'eee', '2018-10-12 00:43:08.396381', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (8, 'fff', '2018-10-12 00:44:51.091807', 6, NULL, 1);
INSERT INTO `blog_comment` VALUES (9, '666', '2018-10-12 00:46:12.699559', 6, NULL, 1);

-- ----------------------------
-- Table structure for blog_tag
-- ----------------------------
DROP TABLE IF EXISTS `blog_tag`;
CREATE TABLE `blog_tag`  (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `blog_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  INDEX `blog_tag_blog_id_a8c60c42_fk_blog_blog_nid`(`blog_id`) USING BTREE,
  CONSTRAINT `blog_tag_blog_id_a8c60c42_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_tag
-- ----------------------------
INSERT INTO `blog_tag` VALUES (1, 'UZI', 1);
INSERT INTO `blog_tag` VALUES (2, '冠军', 1);
INSERT INTO `blog_tag` VALUES (3, '拼搏', 1);
INSERT INTO `blog_tag` VALUES (4, 'Python', 1);
INSERT INTO `blog_tag` VALUES (5, 'Django', 1);

-- ----------------------------
-- Table structure for blog_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `blog_userinfo`;
CREATE TABLE `blog_userinfo`  (
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `avatar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `blog_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`nid`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `phone`(`phone`) USING BTREE,
  UNIQUE INDEX `blog_id`(`blog_id`) USING BTREE,
  CONSTRAINT `blog_userinfo_blog_id_aa34488f_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog_userinfo
-- ----------------------------
INSERT INTO `blog_userinfo` VALUES ('pbkdf2_sha256$36000$ITzKjBrzEUCS$4r0yigvPp6XFnvanojjWYOiYZHdaNT2C1z5xE/c5Trc=', '2018-10-11 23:38:31.845548', 1, 'ban', '', '', '', 1, 1, '2018-08-31 14:15:00.000000', 1, '13811111111', 'avatars/hmbb.png', '2018-08-31 14:15:11.683012', 1);
INSERT INTO `blog_userinfo` VALUES ('pbkdf2_sha256$36000$CbewDsVICzKW$SWQbVeSbS1Ofvy6eN4g1hvlQd8zdiA+PaXgejh5UzT0=', NULL, 0, 'alex', '', '', 'alex@qq.com', 0, 1, '2018-08-31 16:51:35.575731', 2, NULL, 'avatars/hmbb.png', '2018-08-31 16:51:35.669555', NULL);
INSERT INTO `blog_userinfo` VALUES ('pbkdf2_sha256$36000$5wCxN8Tw0ZBJ$F2LNGzfC+hs3kiA7CNVw1xtO2vsRrtMMXEN55d7eDm4=', '2018-09-02 08:45:53.684253', 0, 'xiaohei', '', '', 'xiaohei@qq.com', 0, 1, '2018-09-02 08:45:39.378034', 3, NULL, 'avatars/doger.jpg', '2018-09-02 08:45:39.437866', NULL);

-- ----------------------------
-- Table structure for blog_userinfo_groups
-- ----------------------------
DROP TABLE IF EXISTS `blog_userinfo_groups`;
CREATE TABLE `blog_userinfo_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `blog_userinfo_groups_userinfo_id_group_id_5f60ecec_uniq`(`userinfo_id`, `group_id`) USING BTREE,
  INDEX `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_userinfo_groups_userinfo_id_f6f0498b_fk_blog_userinfo_nid` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for blog_userinfo_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `blog_userinfo_user_permissions`;
CREATE TABLE `blog_userinfo_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `blog_userinfo_user_permi_userinfo_id_permission_i_7d343093_uniq`(`userinfo_id`, `permission_id`) USING BTREE,
  INDEX `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `blog_userinfo_user_p_userinfo_id_57e76697_fk_blog_user` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2018-09-01 16:16:46.743310', '1', 'Ban的个人博客', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2018-09-01 16:18:36.524100', '1', 'LOL', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (3, '2018-09-01 16:18:47.211796', '2', 'NBA', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (4, '2018-09-01 16:18:52.124659', '1', '见证中国团队夺冠 权威媒体报道亚运会盛事', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (5, '2018-09-01 16:19:48.785566', '2', '厂长助EDG锁定第二 季后赛名额悬念尚存', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (6, '2018-09-01 16:20:35.497935', '3', 'Reddit热议亚运会：Uzi就是世界第一', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (7, '2018-09-07 04:15:25.894291', '1', 'Ban的个人博客', 2, '[]', 7, 1);
INSERT INTO `django_admin_log` VALUES (8, '2018-09-07 04:15:58.190357', '1', 'ban', 2, '[{\"changed\": {\"fields\": [\"last_login\", \"phone\", \"blog\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (9, '2018-09-15 14:51:26.615723', '1', 'UZI', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (10, '2018-09-15 14:51:47.952107', '2', '冠军', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (11, '2018-09-15 14:51:58.948703', '3', '拼搏', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (12, '2018-09-15 14:52:06.525435', '4', 'Python', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (13, '2018-09-15 14:52:13.716201', '5', 'Django', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (14, '2018-09-15 14:52:27.557182', '1', '见证中国团队夺冠 权威媒体报道亚运会盛事-冠军', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (15, '2018-09-15 14:52:36.178779', '2', '见证中国团队夺冠 权威媒体报道亚运会盛事-UZI', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (16, '2018-09-15 14:52:43.665770', '3', '厂长助EDG锁定第二 季后赛名额悬念尚存-拼搏', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (17, '2018-09-16 01:59:38.038548', '4', '网友热议SKT无缘S8：给Faker买个靠前的座位', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (18, '2018-09-16 02:01:09.878268', '5', '詹皇曾屏蔽新队友五年！当事人对此表示有点懵', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (19, '2018-09-16 02:01:47.189121', '6', '奥尼尔的这些话 充满着对当今篮球的鄙视', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (20, '2018-09-16 02:02:06.058820', '4', '詹皇曾屏蔽新队友五年！当事人对此表示有点懵-拼搏', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (21, '2018-09-16 02:02:18.591411', '5', '网友热议SKT无缘S8：给Faker买个靠前的座位-冠军', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (22, '2018-09-16 02:02:27.387967', '6', '奥尼尔的这些话 充满着对当今篮球的鄙视-拼搏', 1, '[{\"added\": {}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (23, '2018-09-16 02:36:07.158572', '1', 'ArticleDetail object', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (24, '2018-09-16 02:40:39.937897', '1', 'ArticleDetail object', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (25, '2018-09-16 02:42:47.219010', '1', 'ArticleDetail object', 2, '[{\"changed\": {\"fields\": [\"content\"]}}]', 12, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (9, 'blog', 'article');
INSERT INTO `django_content_type` VALUES (10, 'blog', 'article2tag');
INSERT INTO `django_content_type` VALUES (12, 'blog', 'articledetail');
INSERT INTO `django_content_type` VALUES (6, 'blog', 'articleupdown');
INSERT INTO `django_content_type` VALUES (7, 'blog', 'blog');
INSERT INTO `django_content_type` VALUES (13, 'blog', 'category');
INSERT INTO `django_content_type` VALUES (14, 'blog', 'comment');
INSERT INTO `django_content_type` VALUES (11, 'blog', 'tag');
INSERT INTO `django_content_type` VALUES (8, 'blog', 'userinfo');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-08-31 12:21:48.609500');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2018-08-31 12:21:48.880531');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-08-31 12:21:49.510561');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2018-08-31 12:21:49.686361');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2018-08-31 12:21:49.698487');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2018-08-31 12:21:49.711077');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2018-08-31 12:21:49.728751');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2018-08-31 12:21:49.749013');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2018-08-31 12:21:49.775714');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2018-08-31 12:21:49.789376');
INSERT INTO `django_migrations` VALUES (11, 'blog', '0001_initial', '2018-08-31 12:21:53.039772');
INSERT INTO `django_migrations` VALUES (12, 'admin', '0001_initial', '2018-08-31 12:21:53.399046');
INSERT INTO `django_migrations` VALUES (13, 'admin', '0002_logentry_remove_auto_add', '2018-08-31 12:21:53.423735');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-08-31 12:21:53.512993');
INSERT INTO `django_migrations` VALUES (15, 'blog', '0002_auto_20180902_1622', '2018-09-02 08:22:16.261444');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('5b1q6v0bsv3w6lfjsb09ofrb6i2sgphi', 'NTNhNTMzZGExN2Q5ZmI0YzZhMjY5NDk3NTgwNDVlNjQzOGJjZmNkNjp7Imd0X3NlcnZlcl9zdGF0dXMiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiIyMTRjN2I2ZTQwYzlkMjU3Mzk3N2ExYjFhNWMwODJhZGE0MDhiNjQ1IiwidXNlcl9pZCI6InRlc3QifQ==', '2018-10-25 23:38:31.867488');
INSERT INTO `django_session` VALUES ('8bqrnsyyzyz0nu5fac7gxmkpt8x957ft', 'MzdmMzQzNmI0YTMzNmVjYmY1YWFkMDYzYmRlZmI5ZjA1M2RmZDMxYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiIyMTRjN2I2ZTQwYzlkMjU3Mzk3N2ExYjFhNWMwODJhZGE0MDhiNjQ1In0=', '2018-09-15 16:09:40.671273');
INSERT INTO `django_session` VALUES ('qaer5c759q4f1gj9wfe2aatxgsjgj3ar', 'MjBjZjQzZmE4NTZjZmFlMTEzYjBhNGUxNWM5YjM3NTIyOTI2OTYxMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjIxNGM3YjZlNDBjOWQyNTczOTc3YTFiMWE1YzA4MmFkYTQwOGI2NDUiLCJ1c2VyX2lkIjoidGVzdCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJndF9zZXJ2ZXJfc3RhdHVzIjoxfQ==', '2018-09-14 15:29:59.401071');
INSERT INTO `django_session` VALUES ('uvcypb7lke5pi5tw77q7serodx2zf327', 'NTFlNmYxYTg1YmMzY2VhYjQ2ODhjZjM4ODhlODBlZmExZjQ2Mzg5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjE0YzdiNmU0MGM5ZDI1NzM5NzdhMWIxYTVjMDgyYWRhNDA4YjY0NSIsInVzZXJfaWQiOiJ0ZXN0IiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJndF9zZXJ2ZXJfc3RhdHVzIjoxfQ==', '2018-09-24 14:26:15.456331');

SET FOREIGN_KEY_CHECKS = 1;
