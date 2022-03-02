[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6713246&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

## Repository URL

[Repository](https://github.com/ucl-comp0035/comp0034-cw1-i-Yaseen048.git)

## Requirements
No additional requirements were needed to install part from the ones already give (in the requirements.txt)

## Target audience and questions

The target audience for this dash app are cinema CEOs to help them understand how cinemas and the movie industry were affected due to covid-19 in the UK.

The dashboard is intended to address the following questions:
1) How were sales of movies in cinemas affected due to covid-19?
2) How was the release of movies affected due to covid-19?
3) What were the main movie distributors of films in cinemas during the pandemic?


## Visualisation design

The target audience (cinema CEOs) should have alot of experinece dealing with statistics and graphs as part of theier job is to make big decisions which are often supported by data. Because of this, most CEOs should be able to understand most 2D types of graphs. For example bar, pie, histograms, line charts etc.

The following questions above will be addressed by a bar chart, histogram and pie chart respectivley which cinema CEOs should be comfortable with seeing.

### Question/Chart 1 - Bar chart
The first question addresses sales of movies and is represensted by a bar chart. I have chosen a bar chart due to its simplicty. The bar chart only tells you how much money was made from a movie which is sufficient to give cinema CEOs an undertsanding of the general perfomance of films in cinemas at a given time. No additional information is needed as the questions is about how much money was made and not why. The data required for this bar chart are the weekend gross of movies in the different months.

### Question/Chart 2 - Histogram
The second questions addresses the release of movies in cinemas and is representated by a histogram. This type of chart was chosen beacuse it is easy to look at (comparable to a bar chart) but addresses slighlty more information. The bar chart focuses mainly on one variable (sales - weekend gross) but to answer the second question we need to look at how long the since the movies were orignally released and how many of the movies were new. To do this we define new movies as movies that were released within 3 months, recent movies as movies released between 3 and 12 months, and old movies as movies released over 12 months ago. A histogram helps depict this as the new, recent and old movies can be represented by different class size on the histogram. The data required is the number of weeks since the intial release of the films.

### Question/Chart 3 - Pie chart
The final questions addresses the main movie distributors. This means we take a look at who dominated the movie industry. To show this, a pie chart makes easy to show what portion of films at a given time in cinema were made by a movie distributor. The data required is knowing what distributor made each film that was released in cinema at a given time.



## Evaluation

### Question/Chart 1 - Bar chart
The bar chart was easy to look at and was simple enough for anyone to understand. It was clear to see how movies din comparison to each other in a weekend of a chosen month. However, the bar chart became more difficult to read when comparing 2 or more different months together.Although the contrasting coloured bars help distinguish which movies were from what month, the data was grouped together by month so the surrounding bars for a movie were from movies released in the same month. As a result it made it hard to compare the weekend sales (the length of the bar) of different month since they were not next to eachother. Additonally, the bar chart became too overcrowded when comparing all three time periods. Overall, the bar chart did very well in presenting the data for individual months, there are should be some improvements for when comparing. This could be done reducing the number of films from each month when comparing (best 5 movies from each month) and also ordering the bars by length (weekend sales).

### Question/Chart 2 - Histogram
The histogram wsa able to display its data claerly. It was simplistic and readable. Not just for the individual months but when comparing them as well. The colours helped distinguish the months while the histogram allowed us to group movies based on how old they were. A slight improvement would be to change the class size to make more specific. For example changing the bar width to 8 weeks long. This is because the current visualtion displays every 19 weeks when comparing all 3 months. While 19 weeks helped to split the movies into recent and old movies, it does not quite tell us how new some movies were especially between lockdowns in August. For example, if a movie shown in cinema inbetween lockdowns (Augsut 2020) was placed in the 0-19 weeks since its intial releasw, we cannot tell if it was a brand new movie that just came out or if it was a movie that came out just before the first lockdown (March 2020).

### Question/Chart 3 - Pie chart
The pie chart also worked well. it clearly showed which movie distribtors were making the most movies at a given time. The contrasting colours representing the movie distrutors helped to point out the fraction of the market. But while it was clear to see which movie distributors did the most work, it was a bit hard to read the smallest proportions of the film distributors.To improve this i could group the small fractions together and label them 'other' on the pie chart and then spcify on  table what distributors made up the 'other' section.
