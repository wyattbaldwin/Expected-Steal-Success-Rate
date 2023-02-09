# Defining the Expected Steal Success Rate (ESSR) in Major League Baseball
This project aims to define a new advanced baseball statistic, the Expected Steal Success Rate (ESSR), that uses data visualization and machine learning techniques. The purpose of ESSR is to provide a comprehensive measure of a player's ability to successfully steal bases in Major League Baseball.

## Factors affecting ESSR
There are several factors that can influence a player's ability to steal a base, including:

### Runner-
Speed: A runner's speed plays a crucial role in their ability to steal a base. A faster runner will have an easier time stealing a base than a slower runner.
Lead off distance: The distance the runner starts from their base before the pitcher throws the ball, the bigger the lead off, the better the chance to reach the next base.
Jump: A runner's ability to get a quick start and "jump" off the base can also play a role in a successful steal.
### Pitcher-
Delivery time: The pitcher's delivery time to home plate can affect the ability of the runner to steal a base. Faster deliveries make it more difficult for the runner to get a good jump.
### Catcher-
Pop time: The time it takes for the catcher to release the ball after receiving it from the pitcher can play a role in a successful steal.
Arm strength: A catcher with a strong arm will make it more difficult for the runner to reach the next base.
Current Advanced Statistics used by MLB Teams:
One of the advanced statistics currently used by Major League Baseball teams is Baserunning Runs (BsR), which estimates the number of runs a player contributes or subtracts to their team through their baserunning skills. BsR takes into account various factors, such as stolen base attempts, taking extra bases on hits, and advancing on fly balls. However, BsR does not take into account the situation, making it less comprehensive than ESSR.

## Fixed Data:
The distance between home plate and the pitching rubber on a Major League Baseball field is 60 feet, 6 inches (18.44 meters).
The distance between the bases on a Major League Baseball field is 90 feet (27.432 meters).
The distance from home plate to second base in Major League Baseball is about 127 feet and 3 inches (38.71 meters).
Data Information:
ESSR can be used in conjunction with other statistics such as batting average, on-base percentage, and slugging percentage to provide a more complete picture

of a player's overall performance. The data for ESSR will be collected from existing sources such as Major League Baseball's Statcast system, which tracks various aspects of each play, including the speed of the runner, the delivery time of the pitcher, the pop time of the catcher, and more.

## Data Preparation:
The collected data will need to be cleaned and processed before it can be used in the analysis. This will involve removing any missing or irrelevant data, and transforming the data into a format that can be easily used in machine learning algorithms.

## Data Visualization:
Data visualization techniques will be used to explore and understand the relationship between the different factors that affect ESSR. This will help identify the most important factors and the relationships between them.

## Machine Learning Techniques:
Machine learning algorithms such as linear regression, decision trees, or random forests will be used to build a model that predicts ESSR. The model will be trained using the processed data, and its accuracy will be evaluated using cross-validation techniques.

## Conclusion:
The ESSR statistic provides a comprehensive measure of a player's ability to successfully steal bases in Major League Baseball. By combining data visualization and machine learning techniques, ESSR provides a more complete picture of a player's performance than current advanced statistics. This can help teams make more informed decisions about their roster and tactics, leading to improved performance on the field.
