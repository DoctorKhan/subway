<header>
# [Riding the New York City Subway in the Rain](https://insightcatalyst.wordpress.com/2014/08/27/12/)

</header>

<h3>Introduction</h3>

On average, the New York city subway system transports over a thousand individuals every hour. Predicting subway ridership may be useful in the planning and maintenance of the subway system. Greater ridership may require more maintenance but also increases income, which may be considered during budgeting.

Now consider the effect of weather on ridership. On a typical rainy day, I would rather not drive, so this makes me more inclined to use mass transit, such as a subway system. In the following blog post I answer the question: Do passengers use the New York City subway system more on rainy days? It is found that there is indeed a 1.4% increase in ridership on rainy days with p < 0.025 in the the Mann-Whitney U-test.

<h3>Background</h3>

In New York City, the subway system opened in 1904\. It was initially developed by two private companies: Brooklyn Rapid Transit Company and Interborough Rapd Transit Comany. The lines were mostly built by the city and leased to the companies, but in 1932 the city created its own system, the Independent Subway System. Due to the expensive cost of operating and maintaining a subway system, and the lack of investment by the city, the fares were approximately double the normal fare. In 1940, the city bought both competing systems and integrated them into one unified system.

<h3>Question</h3>

Do passengers use the New York City subway more on rainy days? Additional passengers may increase some operating costs and maintenance on rainy days, but also contribute additional income from fares.

<h3>Analysis</h3>

First let’s make a histogram of hourly turnstile entries on rainy days and non-rainy days to see if there is an apparent difference.

[![RainHist](./Insight Catalyst _ Data science aspirations_files/rainhist1.png)](https://insightcatalyst.wordpress.com/2014/08/rainhist1.png)
<img src=rainhist1.png>
The histogram above (logarithmic y-scale) shows a consistently greater ridership on rainy days than non-rainy days, but this is a qualitative statement.

To compute the mean hourly turnstile entries for rainy vs. non-rainy days, I wrote a mapreduce in python. There were two keys: rainy and non-rainy. The corresponding values were the houlry turnstile entries. For a larger dataset, in a cluster with nodes greater than two, it would make sense to assign more keys, possibly one for every hour of the day. This would allow batch processing of 24 datasets at a time vs. two.

For our data, the entries were averaged by the reducer to find the average ridership on rainy vs. non-rainy days. On rainy days we averaged 1105 entries, while on non-rainy days we averaged 1090.

To test the statistical significance of this difference, I used the Mann-Whitney U-test. In agreement with the above histogram, this test does not assume the distributions are normal. This test ranks the data in each distribution and compreas them. For example, if the distributions are the same, then the mean ranks should also be the same. The test indicates we can reject the null hypothesis with p < 0.025.

Additionally, I performed a linear regression to see if ridership can be predicted using the features rain, precipitation, hour, mean temperature. The residual distribution plotted below appears roughly normal, so it appears the model is explaining the data well.

[![Residuals](./Insight Catalyst _ Data science aspirations_files/residuals.png)](https://insightcatalyst.wordpress.com/2014/08/residuals.png)

In this case, R-squared = 0.31, however we have not established that the trend is statistically significant.

<h3>Conclusion</h3>

It seems that more people use the subway when there is rain than otherwise, and this difference is statistically significant, p < 0.025\. On the rainy days we get an average of 1105 users while on the non-rainy days we get 1090\. That’s about a 1.4% increase. This doesn’t seem like much, but we are talking about averages here.

One thing to consider is where these additional passengers are coming from. Does this mean that there are on average 15 fewer drivers on the road every hour? An interesting next step might involve gathering non-subway traffic data and attempt to find a correlation.

In any case, we have shown that statistically significant differences in ridership as a function of weather can be found and modeled using linear regression.
