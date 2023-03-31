# flaskproduct
Task Assignment for Erajaya

The architecture is using MVC design pattern. MVC provides a clear separation of concerns, which can make it easier to develop, maintain and test the backend code of a web application. The Model represents the data and business logic of the application, the View is responsible for presenting the data to the user, and the Controller handles the user input and updates the Model and View accordingly.

When making this Flask RESTful backend, the Model (Product) can hold the data that is stored in a database using SQLAlchemy ORM and MySQL. The View shows the data in JSON response to clients. The Controller handles requests from clients and sends back the right requested data. Using MVC means that the parts of the code that handle data and rules are separate from the parts that show data to users. This makes it simpler to test and change the code. In summary, using the MVC pattern for a RESTful backend provides a clear separation of concerns and makes the code more modular, easier to test and more maintainable, and therefore, this is a part of clean code architecture.

ADD PRODUCT API:
![image](https://user-images.githubusercontent.com/61260701/229066182-7f3cefe0-7362-4da8-8b10-c32736164f73.png)

GET PRODUCT API:
BY PRODUCT NAME (A-Z)
First Request
![image](https://user-images.githubusercontent.com/61260701/229066484-0311e478-6e3a-4c2b-a44c-0860bb3fad97.png)

After Caching, request time reduced to 18ms
![image](https://user-images.githubusercontent.com/61260701/229066590-5f82c9bc-47dd-4569-9478-5f68a14719f5.png)

BY PRODUCT TIME (OLDEST)
![image](https://user-images.githubusercontent.com/61260701/229067199-6bef0782-378a-4a24-8d31-1d2fa0055df3.png)

BY PRODUCT PRICE (CHEAPEST)
![image](https://user-images.githubusercontent.com/61260701/229067269-d81e5982-0079-4000-96be-2e03df16784b.png)

BY PRODUCT NAME (Z-A)
![image](https://user-images.githubusercontent.com/61260701/229067302-92dcd43d-b565-40dc-b0dc-45a5d0b08134.png)

BY PRODUCT PRICE (MOST EXPENSIVE)
![image](https://user-images.githubusercontent.com/61260701/229067347-8f0cf3fb-ac89-463d-9e52-0b973a2ca10e.png)

BY PRODUCT TIME (NEWEST)
![image](https://user-images.githubusercontent.com/61260701/229067393-93635cdd-4052-498e-8d2b-f557e1f02206.png)

