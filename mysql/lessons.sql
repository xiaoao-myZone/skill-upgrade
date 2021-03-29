/*
## Lesson

### 1
*/

SELECT
    state, SUM(`quantityOrdered` * `priceEach`)
FROM
    `orders`
INNER JOIN `orderdetails`
    USING (`orderNumber`)
GROUP BY
    `state`;

/*
+------------+------------+
| status     | amount     |
+------------+------------+
| Cancelled  |  238854.18 |
| Disputed   |   61158.78 |
| In Process |  135271.52 |
| On Hold    |  169575.61 |
| Resolved   |  134235.88 |
| Shipped    | 8865094.64 |
+------------+------------+
*/
/*
### 2
*/

SELECT
    YEAR(`orderDate`), SUM(`quantityOrdered` * `priceEach`) as `total`
FROM `orders`
INNER JOIN `orderdetails`
    USING(`orderNum`)
WHERE
    `statue`='Shipped'
GROUP BY
    YEAR(`orderDate`);
/*
+-----------------+----------------------------------+
| YEAR(orderDate) | SUM(quantityOrdered * priceEach) |
+-----------------+----------------------------------+
|            2003 |                       3223095.80 |
|            2004 |                       4300602.99 |
|            2005 |                       1341395.85 |
+-----------------+----------------------------------+
*/
-- ### 3
SELECT
    `firstName`, `lastName`
FROM
    `employees`
WHERE
    `officeCode` in (SELECT
            `officeCode`
        FROM
            `offices`
        WHERE
            `country` = 'USA'
    );

-- ### 4
SELE