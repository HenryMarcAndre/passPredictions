<html>
    <body>
        <h1>Predicting Passes That Become Goals</h1>
        <p>The data used for this project is MLS locations data and event data. The data was merged together, creating a dataset 
        with all passes, along with the position on the field of each player when the pass was made. Features were 
        then added to the data to help further descibe the play, things such as how many players were ahead of the ball and how
        many teammates or opponents were within a certain proximity of the ball. </p>
        <p>The data in this project was very random and imbalanced, which made the predictive analysis very hard. After evaluating 
        all of the data it became apparent that these 3 features were the best predictors: </p>
        <p>(What these graphs are showing us is the mean of each value in the feature. A goal is equal to 1, and no goal is equal to 0. For example on the graph above, when there are 3 more defenders ahead of the ball when a pass is made, the mean goals average goals scored on the play is around 0.09 goals.)</p>
        <ul>
            <li>Outnumbered Ahead of Ball - this describes the difference between attackers and defenders ahead of the ball when the pass is made.
             If the number is negative there are more defenders than attackers. </li>
            <img src="feature1.png" alt="image">
            <p>(What these graphs are showing us is the mean of each value in the feature. A goal is equal to 1, and no goal is equal to 0. For example on the graph above, when there are 3 more defenders ahead of the ball when a pass is made, the average amount goals scored on the play is around 0.09 goals.)</p>
            <li>Outnumbered Within 10 Yards - This describes the difference in attackers and defenders within 10 yards of the ball when the pass is made.  </li>
            <img src="feature2.png" alt="image">
            <li>Players Ahead of Ball - This describes the total number of players ahead of the ball when the pass is made. It does not take into account which team the players are on. </li>
            <img src="feature3.png" alt="image">
        </ul>
        <h1>Predicitve Analysis</h1>
        <p>To make predictions on the data I tried multiple different classification models, and logistic regression worked the best. Like I said earlier, the randomness and imbalance of the data made it very hard to predict. 
            However, the model was able to predict accurately 82% of the time. 
        </p>
        <p>Accuracy: 0.82</p> 
        <p>Percision: 0.18</p> 
        <p>Recall: 0.36</p>
        <p>F1 Score: 0.24</p>
        <img src="auc.png" alt="image">
        
    </body>
</html>
