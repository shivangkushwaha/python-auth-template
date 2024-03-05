# Tool Marketplace

Tools market Place API's for RUV

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)

## Installation

```
pip install -r requirements.txt
```

## Database Schema

### `tools` Table

```sql
CREATE TABLE `tools` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) DEFAULT NULL,
  `description` TEXT,
  `instruction` TEXT,
  `capabilities` JSON DEFAULT NULL,
  `github_link` VARCHAR(255) DEFAULT NULL,
  `run_commands` TEXT,
  `conversation_starters` JSON DEFAULT NULL,
  `file_path` VARCHAR(255) DEFAULT NULL,
  `file_size` INT DEFAULT NULL,
  `content_type` VARCHAR(255) DEFAULT NULL,
  `file_extension` VARCHAR(255) DEFAULT NULL,
  `uuid` VARCHAR(255) DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `active` INT DEFAULT '1',
  `comment` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

### `tools` Table
```sql
CREATE TABLE `tool_metadata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tool_id` INT NOT NULL,
  `score` FLOAT DEFAULT NULL,
  `metadata` JSON DEFAULT NULL,
  `uuid` VARCHAR(255) DEFAULT NULL,
  `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `active` INT DEFAULT '1',
  `comment` TEXT,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_tool_metadata_tool_id` FOREIGN KEY (`tool_id`) REFERENCES `tools` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

### `roles` Table
```sql
CREATE TABLE `roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `isBasic` INT NOT NULL DEFAULT 0,
  `code` VARCHAR(255),
  `uuid` CHAR(36),
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### `users` Table
```sql
CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255),
  `phone` VARCHAR(255),
  `password` VARCHAR(255),
  `status` INT NOT NULL DEFAULT 1, -- Assuming `appConstant.STATUS.ACTIVE` equals 1
  `is_token_expire` INT NOT NULL DEFAULT 0, -- Assuming `appConstant.STATUS.INACTIVE` equals 0
  `is_email_verify` BOOLEAN NOT NULL DEFAULT FALSE,
  `is_phone_verify` BOOLEAN NOT NULL DEFAULT FALSE,
  `country_code` VARCHAR(255) NOT NULL,
  `is_profile_complete` BOOLEAN NOT NULL DEFAULT FALSE,
  `uuid` CHAR(36) NOT NULL ,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` DATETIME,
  PRIMARY KEY (`id`),
  INDEX `email_idx` (`email`),
  FULLTEXT INDEX `full_text` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;