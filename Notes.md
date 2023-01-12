Factors that can affect a player's ability to steal a base:

    Runner-
- Speed: A runner's speed plays a crucial role in his ability to steal a base. A faster runner will have an easier time stealing a base than a slower runner.
- Lead off distance: The distance the runner starts from his base before the pitcher throws the ball, the bigger the lead off, the better the chance to reach next base.
- Jump: A runner's ability to get a quick start and "jump" off the base can also play a role in a successful steal.

    Pitcher-
- Delivery time: The pitcher's delivery time to home plate can affect the ability of the runner to steal a base. Faster deliveries makes it more difficult for the runner to get a good jump.

    Catcher-
- Pop time: The time it takes for the catcher to release the ball after receiving it from the pitcher can play a role in a successful steal.
- Arm strength: A catcher with a strong arm will make it more difficult for the runner to reach the next base.

Current Advanced Stat MLB Teams Use:
- Baserunning Runs (BsR) is a statistic that estimates the number of runs a player contributes or subtracts to his team through their baserunning skills.
- BsR takes into account various factors, such as stolen base attempts, taking extra bases on hits and advancing on fly balls.
- A positive BsR value indicates that a player is adding value to his team through their baserunning skills.
- A negative BsR value indicates that a player is subtracting value from his team through their baserunning skills.
- BsR is similar to the statistic "+/-" in hockey which measures the impact of a player on the number of goals scored by the team while they were on the ice.
- Both +/- and BsR attempt to capture the overall value of a player's skills within the context of the team and should not be the only measure of a player's performance.
- BsR can be a useful tool in determining the runner's jump.
- BsR does not take into account the situation.

Fixed Data:
- The distance between home plate and the pitching rubber on a Major League Baseball field is 60 feet, 6 inches (18.44 meters).
- The distance between the bases on a Major League Baseball field is 90 feet (27.432 meters).
- The distance from home plate to second base in Major League Baseball is about 127 feet and 3 inches (38.71 meters).

Data Connections:
- Speed: running_splits_2022.csv - used to calculate a player's travel time of 90 feet less the lead off distance.
- Lead off distance: variable data, can be used to coach a player and advise on when to steal a base in certain situations.
- Jump: BsR can be used to determine a player's baserunning awareness.
- Delivery Time: pitch_arsenals_2022.csv - used to calculate the time it takes for a pitch to travel 60.6 inches, this could be useful information to a pitcher to show what pitches they should stay away from if there is a runner on base.
- Pop Time: poptime_2022.csv - data can be used to either use the proven averages of pop time for 2nd and 3rd bases, create own calculation based on throwing speed, catch to throw time and using the distance from home to 2nd (38.71 meters) or home to 3rd (90 feet) based on the situation.
- Arm strength: variable data, it could be dropped, or it could be also be a scale of 0-100 based on if data is found for their lowest and highest actual time to get the ball to the base.

Website Ideas:

- Fields to allow the user to put their own numbers in for the variables (Speed, Lead off distance, Jump, Delivery Time, Pop Time and Arm Strength).
- Ability to select players from dropdowns to create scenerios.
- With more data we can give the ability to select the player and the year which could be used to track a player advancing or regressing in their ability.
- Our team page
- 2nd page for visualization from the pitcher perspective looking at how likely a runner is able to be successful stealing a base against a certain pitcher or certain pitch types, this would be similar to the main page with fields that allow users to enter their own variables (4_seam_fastball,sinker,cutter,slider,changeup,curve,splitter,knuckleball).  

Website Visuals Ideas-
- Birds-Eye view of the field allowing the visual representation of the play in a 2d format
- .gif of Umpire either calling out or safe
- a series of .gifs that the one that has the closest representation of the play appears
