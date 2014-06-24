create table `articles`(
	`ID` integer primary key,
	`title` text,
	`abstract` text,
	`doi` text,
	`pmid` text,
	`arxivId` text,
	`started` integer,
	`added` integer,
	`note` text,
	`privacy` integer,
	`jId` integer,
	`page` text,
	`issue` text,
	`volume` text,
	`year` integer
);

create table `authors` (
	`ID` integer,
	`firstName` text,
	`lastName` text
);

create table `collections` (
	`cId` integer primary key,
	`name` text,
	`parent` integer,
	`privacy` integer
) 

create table `journals` (
	`jId` integer primary key,
	`name` text,
	`abbrev` text,
	`issn` text,
	`factor` real,
	`five` real,
	`issue` integer,
	`halflife` text,
	`immediacyIndex` real, 
	`eigenfactor` real, 
	`influenceScore` real,
	`language` text,
	`publisher` text,
	`country` text
)

create table `documents`(
	docId integer primary key,
);