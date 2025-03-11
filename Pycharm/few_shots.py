few_shots = [
    {
        'Question': "List all customers in France with a credit limit over 20,000.",
        'SQLQuery': "SELECT * FROM customers WHERE country = 'France' AND creditLimit > 20000;",
        'SQLResult': "Result of the SQL query",
        'Answer' : """customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit\n103, Atelier graphique, Schmitt, Carine , 40.32.2555, 54, rue Royale, None, Nantes, None, 44000, France, 1370, 21000.00\n119, La Rochelle Gifts, Labrune, Janine , 40.67.8555, 67, rue des Cinquante Otages, None, Nantes, None, 44000, France, 1370, 118200.00\n146, Saveley & Henriot, Co., Saveley, Mary , 78.32.5555, 2, rue du Commerce, None, Lyon, None, 69004, France, 1337, 123900.00\n171, Daedalus Designs Imports, Rancé, Martine , 20.16.1555, 184, chaussée de Tournai, None, Lille, None, 59000, France, 1370, 82900.00\n172, La Corne D'abondance, Co., Bertrand, Marie, (1) 42.34.2555, 265, boulevard Charonne, None, Paris, None, 75012, France, 1337, 84300.00"""
    },
    {
        'Question': "Get the highest payment amount made by any customer.",
        'SQLQuery': "SELECT MAX(amount) FROM payments;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "120166.58"
    },
    {
        'Question': "Retrieve the names of employees who report to employee number 1002.",
        'SQLQuery': "SELECT firstName, lastName FROM employees where reportsTo = 1002;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Mary Patterson, Jeff Firrelli"
    },
    {
        'Question': "List all products with a stock quantity less than 7000",
        'SQLQuery': "SELECT productName, quantityInStock FROM products WHERE quantityInStock < 7000;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "1996 Moto Guzzi 1100i, 6625"
    },
    {
        'Question': "What is price of '1968 Ford Mustang'",
        'SQLQuery': "SELECT buyPrice, MSRP FROM products WHERE productName = '1968 Ford Mustang' LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "95.34, 194.57"
    },
    {
        'Question': "List customer name who has highest payment amount",
        'SQLQuery': "SELECT c.customerName, MAX(amount) FROM payments p join customers c on c.customerNumber = p.customerNumber GROUP BY c.customerNumber ORDER BY MAX(amount) DESC LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Euro+ Shopping Channel, 120166.58"
    },
    {
        'Question': "which customers has highest orders",
        'SQLQuery': "SELECT c.customerName, MAX(quantityOrdered) FROM orders o join customers c on c.customerNumber = o.customerNumber join orderdetails od on od.orderNUmber = o.orderNumber GROUP BY c.customerNumber ORDER BY MAX(quantityOrdered) DESC LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Mini Caravy, 97"
    },
    {
        'Question': "List best customers",
        'SQLQuery': "select customerName from customers c left join  customer_segments s on c.customerNumber = s.customerNumber where cluster = 3;",
        'SQLResult': "Result of the SQL query",
        'Answer' : ""
    }
]