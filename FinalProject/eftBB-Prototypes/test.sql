CREATE TRIGGER T2
    AFTER UPDATE
    ON customer
    FOR EACH ROW BEGIN
        IF old.c_acctbal > 0 THEN 
            IF new.c_acctbal < 0 THEN
                SET new.c_comment = 'Negative balance!!!'
end;

UPDATE customer
SET c_acctbal = -100
WHERE c_nationkey = (select c2.c_nationkey
                        from customer c2, nation
                        where c2.c_nationkey = n_nationkey AND
                                n_regionkey = 3);

SELECT count(c_custkey)
FROM customer
WHERE c_acctbal < 0 AND
        c_nationkey = 6;