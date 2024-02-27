
DELETE FROM Materials;
DELETE FROM MaterialTypes;
DELETE FROM Genres;

DROP TABLE IF EXISTS Materials;
DROP TABLE IF EXISTS MaterialTypes;
DROP TABLE IF EXISTS Genres;

CREATE TABLE `Genres` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL
);

CREATE TABLE `MaterialTypes` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`checkout_days` INTEGER NOT NULL
);

CREATE TABLE `Materials` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`  TEXT NOT NULL,
	`author`  TEXT NOT NULL,
	`material_type_id` INTEGER NOT NULL,
	`genre_id` INTEGER NOT NULL,
	`checkout_date` TEXT,
	FOREIGN KEY(`material_type_id`) REFERENCES `MaterialTypes`(`id`)
	FOREIGN KEY(`genre_id`) REFERENCES `Genre`(`id`)
);

INSERT INTO `MaterialTypes` VALUES (null, 'Book', 21);
INSERT INTO `MaterialTypes` VALUES (null, 'eBook', 14);
INSERT INTO `MaterialTypes` VALUES (null, 'Audio Book', 7);


INSERT INTO `Genres` VALUES (null, 'Sci-Fi');
INSERT INTO `Genres` VALUES (null, 'Fantasy');
INSERT INTO `Genres` VALUES (null, 'Biography');
INSERT INTO `Genres` VALUES (null, 'Literature');
INSERT INTO `Genres` VALUES (null, 'History');
INSERT INTO `Genres` VALUES (null, 'Reference');


INSERT INTO `Materials` (`title`, `author`, `material_type_id`, `genre_id`, `checkout_date`)
VALUES
    ('The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 1, 1, NULL),
    ('The Lord of the Rings', 'J.R.R. Tolkien', 1, 2, NULL),
    ('Steve Jobs', 'Walter Isaacson', 1, 3, NULL),
    ('To Kill a Mockingbird', 'Harper Lee', 1, 4, NULL),
    ('1984', 'George Orwell', 1, 4, NULL),
    ('Dune', 'Frank Herbert', 2, 1, NULL),
    ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 2, 2, NULL),
    ('The Da Vinci Code', 'Dan Brown', 2, 4, NULL),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 2, 4, NULL),
    ('The Art of War', 'Sun Tzu', 2, 5, NULL),
    ('The Hobbit', 'J.R.R. Tolkien', 3, 2, NULL),
    ('The Catcher in the Rye', 'J.D. Salinger', 3, 4, NULL),
    ('The Diary of a Young Girl', 'Anne Frank', 3, 5, NULL),
    ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 3, 5, NULL),
    ('The Odyssey', 'Homer', 3, 4, NULL),
    ('Pride and Prejudice', 'Jane Austen', 1, 4, NULL),
    ('The Girl with the Dragon Tattoo', 'Stieg Larsson', 2, 2, NULL),
    ('The Martian', 'Andy Weir', 3, 1, NULL),
    ('The Catcher in the Rye', 'J.D. Salinger', 1, 4, NULL),
    ('The Hunger Games', 'Suzanne Collins', 2, 4, NULL);
