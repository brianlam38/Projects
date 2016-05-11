--- SKELETON KEY ---
SELECT title, rental_rate
FROM film
WHERE rental_rate = .99
;

--- BRAINBUSTER 1.5 ---
SELECT first_name, last_name, email
FROM store
WHERE store_id = 2
;

--- BRAINBUSTER 2 ---
SELECT first_name, last_name
FROM actor
WHERE actor_id = 50
;

SELECT
FROM
WHERE
;

--- LECTURE 10 COUNT AND GROUP BY ---
#where count(title) = count the number of titles (count is a function)
select count(title)
from film
where rental_rate = .99
;

select title, rental_rate
from film
group by rental_rate
;

#how many films are we renting at each of those three prices?
select count(title),rental_rate
from film
group by rental_rate
;

#alternative method to "group by" --> group by the number (SQL shortcut)
#where 2 = rental_rate --> if you group by 1 (title), it will show every title
select count(title),rental_rate
from film
group by 2
;

--- BRAINBUSTER 3 ---
#Which rating do we have the most films in? (Rating = PG, G etc.)
#write a query to tell us the number of films we have in each film rating
select count(title),rating
from film
group by 2
;
#ANSWER = PG13 (223 highest count)

--- EXTRA BRAINBUSTER 3 ---
#Which rating is most prevalent in each store? (+extra = each price?)
#Only use ONE QUERY to find that out.
#PART 1: answer = PG13 with 446 store counts
select count(store_id),rating
from film,store
group by rating
;
#PART 2: Which ratings are most prevalent in each price?
select rating, rental_rate, count(film_id)
#note count(film_id) same as count(title) it's just a different way to do it
from film
group by 1, 2
;

--- LECTURE 13 CONNECTING TABLES ---
#Finding the customer id, name(first and last), mailing address

select customer.customer_id, customer.first_name, customer.last_name, address.address #Add the name of the table then a .(dot), then the name of the column that you want to pull the info from
from customer, address #using the customer and address table
where customer.address_id = address.address_id
;


--- BRAINBUSTER 4 (CONNECTING 3 TABLES) ---
#List of every film, the category of that film and the language of that film.

select film.title, category.name, language.name
from film, category, language, film_category
where film.language_id = language.language_id and film.film_id = film_category.film_id and film_category.category_id = category.category_id
;
#Admin's answer (pretty much the same as above, except structured better),
SELECT
	film.title, category.name, language.name
FROM
	film, language, film_category, category
WHERE
	film.film_id = film_category.film_id
    and
    category.category_id = film_category.category_id
    and
    film.language_id = language.language_id
#Extra: SHORTCUTS!
#we can give all the tables nicknames- after you write the title of the table, press [space] + write any nickname that you want:
#Admin's answer with SHORTCUTS
SELECT
	f.title, c.name, l.name
FROM
	film f, language l, film_category FC, category C 
WHERE
	f.film_id = fc.film_id
    and
    c.category_id = fc.category_id
    and
    f.language_id = l.language_id
 ;

 WHERE
 	f.film_id
 	and