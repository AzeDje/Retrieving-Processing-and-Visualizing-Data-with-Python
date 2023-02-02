# Capstone-Project
Capstone Project: Retrieving, Processing, and Visualizing Data with Python (University of Michigan Through Coursera)

Hello Everyone !

At first, I identified a Data Source from U.S. Energy Information Administration, here is the website:  https://www.eia.gov/

This source contains data and statistics on different sources of energy such as petroleum, natural gas, electricity and their production, consumption, import, export and so on.

I'm interested to perform some analysis on the consumption of petroleum in several locations and its impact on CO2 Emissions over the world.

So I believe that this subject is useful for me personally and professionally. 

At present, I started connecting to the Data source (https://www.eia.gov) from an API using a specific Key, then pull the Data from it and parse it into JSON Format, and at the end insert it to a Database. In fact, this Data source contains almost 4 Millions row of Data, and we are allowed to gather, only up to 5000 records per request.

So, all the Data that is extracted should be processed and cleaned up before analyzing and visualizing, by dropping a duplicate records and deleting some special characters using Pandas, and then insert it to another Database as shown in the Data program structure below. 

![structure](https://user-images.githubusercontent.com/124156831/216390196-00991b2d-7d8e-4e66-9097-d69488b05131.png)

In addition , we need to design a Database model index as demonstrated below, that improve the performance and the speed to retrieve results as demonstrated below.

![mapping](https://user-images.githubusercontent.com/124156831/216390389-2ed058aa-536d-4ddb-99f7-420a7495ce18.png)

So well, here we are in the final step of this capstone project. The outcome of our process is presented in the two pictures below which the first one demonstrate the Data analyzing of the top 10 largest Petroleum consuming in 2021 (in thousand barrels per day), and CO2 Emissions over the world throughout the time (in million metric tonnes carbon dioxide), and the second one display the Data visualizing in HTML browser coding with D3 JS.

![analyze](https://user-images.githubusercontent.com/124156831/216390484-265b111c-cb4b-4641-bed6-f5fd49067f51.png)

![visualize](https://user-images.githubusercontent.com/124156831/216390566-d1920bf1-87b4-4d78-b20b-ca900c118d23.png)

All in all,  in this capstone project, I have been able to try my hands at a few really interesting Data extracting, processing and visualizing, I have learned a lot more than I expected, that was super important for me in how to overcome different problems and find solutions, as well as in how to manage all the stages of this project. 

Thank you Dr. Charles Severance for being such a great professor, and thank you everyone for your attention, its pleasure to share my work with you, I remain available for any feedback or any further information you may need about my project.

Best regards. 




