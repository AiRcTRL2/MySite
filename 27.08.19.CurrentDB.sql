-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mysite-games
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mysite-games
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mysite-games` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mysite-games` ;

-- -----------------------------------------------------
-- Table `mysite-games`.`game_database`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysite-games`.`game_database` (
  `game_id` INT(11) NOT NULL AUTO_INCREMENT,
  `game_name` VARCHAR(45) NULL DEFAULT NULL,
  `game_trailer` VARCHAR(45) NULL DEFAULT NULL,
  `date_recorded` DATE NULL DEFAULT NULL,
  `image_loc` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`game_id`),
  UNIQUE INDEX `game_name_UNIQUE` (`game_name` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 27
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mysite-games`.`current_pricing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysite-games`.`current_pricing` (
  `date_time` DATETIME NOT NULL,
  `game_id_number` INT(11) NOT NULL,
  `current_lowest_price` INT(11) NULL DEFAULT NULL,
  `historical_lowest_price` INT(11) NULL DEFAULT NULL,
  `average_price` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`date_time`),
  INDEX `fk.game_id_number_idx` (`game_id_number` ASC) VISIBLE,
  CONSTRAINT `fk.game_id_number`
    FOREIGN KEY (`game_id_number`)
    REFERENCES `mysite-games`.`game_database` (`game_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mysite-games`.`game_genres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysite-games`.`game_genres` (
  `table_id` INT(11) NOT NULL AUTO_INCREMENT,
  `game_id_num` INT(11) NOT NULL,
  `game_genre` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`table_id`),
  INDEX `fk.game_id_idx` (`game_id_num` ASC) VISIBLE,
  CONSTRAINT `fk.game_id`
    FOREIGN KEY (`game_id_num`)
    REFERENCES `mysite-games`.`game_database` (`game_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mysite-games`.`game_platform_ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysite-games`.`game_platform_ratings` (
  `game_platform` VARCHAR(45) NOT NULL,
  `game_id_number_plat` INT(11) NOT NULL,
  `game_rating` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`game_platform`, `game_id_number_plat`),
  INDEX `fk.game_id_number_plt_idx` (`game_id_number_plat` ASC) VISIBLE,
  CONSTRAINT `fk.game_id_number_plt`
    FOREIGN KEY (`game_id_number_plat`)
    REFERENCES `mysite-games`.`game_database` (`game_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mysite-games`.`game_vendors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysite-games`.`game_vendors` (
  `game_name` VARCHAR(45) NULL DEFAULT NULL,
  `vendor_id` INT(11) NOT NULL AUTO_INCREMENT,
  `vendor_name` VARCHAR(45) NULL DEFAULT NULL,
  `game_id` INT(11) NOT NULL,
  `game_platform` VARCHAR(45) NULL DEFAULT NULL,
  `vendore_store_link` VARCHAR(45) NULL DEFAULT NULL,
  `affiliate_id_link` VARCHAR(45) NULL DEFAULT NULL,
  `current_price_at_vendor` INT(11) NULL DEFAULT NULL,
  `previous_price_at_vendor` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`vendor_id`, `game_id`),
  UNIQUE INDEX `vendor_id_UNIQUE` (`vendor_id` ASC) VISIBLE,
  INDEX `fk.game.id_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk.game_platform_idx` (`game_platform` ASC) VISIBLE,
  INDEX `fk.game_name_idx` (`game_name` ASC) VISIBLE,
  CONSTRAINT `fk.game.id`
    FOREIGN KEY (`game_id`)
    REFERENCES `mysite-games`.`game_database` (`game_id`),
  CONSTRAINT `fk.game_name`
    FOREIGN KEY (`game_name`)
    REFERENCES `mysite-games`.`game_database` (`game_name`),
  CONSTRAINT `fk.game_platform`
    FOREIGN KEY (`game_platform`)
    REFERENCES `mysite-games`.`game_platform_ratings` (`game_platform`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
