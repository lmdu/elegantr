create table `articles`(
	`id` integer primary key,
	`title` text,
	`abstract` text,
	`doi` text,
	`pmid` text,
	`arxiv` text,
	`favorite` integer,
	`added` integer,
	`note` text,
	`privacy` integer,
	`page` text,
	`issue` text,
	`volume` text,
	`year` integer,
	`authors` text,
	`folder` integer,
	`resource` integer,
	`factor` real,
	`issn` text,
	`publisher` text,
	`md5` text,
	`type` text
);

create table `folders` (
	`id` integer primary key,
	`name` text,
	`privacy` integer
)