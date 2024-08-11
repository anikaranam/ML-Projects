# ML-Projects
Repo to store my experiments with different ML Algorithms

NBA Player Salary Analysis:
<img width="959" alt="Screenshot 2024-08-10 at 6 06 50 PM" src="https://github.com/user-attachments/assets/5be38bbb-397e-4a23-85aa-8ca4619a6092">

1. Bradley Beal's salary disparity makes sense because he plays for the Suns but is currently on a super max contract from Washington, suffered nagging injuries and didn't play much this season and performed well below his expectations

2. Ben Simmons also has a huge salary disparity and is on one of the worst contracts in the league and struggles to stay healthy while Zion Williamson is on a super max extension but also has had some injuries recently

3. Devin Booker is a bit of a surprising addition to this list, considering he did not seem to have a "down" year, but it could be explained by the fact that he is now playing with 2 superstars in Kevin Durant and Bradley Beal, and his sttas are bound to take a hit.

4. Jordan Poole had a very disappointing year on the Wizards after getting paid by the Warriors just one season ago

<img width="991" alt="Screenshot 2024-08-10 at 6 06 33 PM" src="https://github.com/user-attachments/assets/0d43d1bd-2755-4b04-8e5f-4d4fdfff9d92">

1. According to my model, Jalen Brunson is getting paid a LOT less than what he should be getting paid. This hypothesis is validated by the fact that he was one of the most impactful players in the playoffs this past season and was eligible for a max extension this offseason (but chose to take a team friendly deal)

2. Some other players like Cade Cunningham, Tyrese Haliburton, Jalen Williams, Tyrese Maxey and Alperen Sengun are also on this list, getting paid a lot less than their predicted values. What's one thing in common between them? They are all on rookie contracts! With their second contracts, these players will get paid a lot more money, in alignment with the value they bring to their teams

### Clutch shooting percentage analysis:

In this project, I wanted to understand how players' shooting percentages differ in clutch time (5 point game, < 5 minutes to go) compared to the rest of the game.
The hypothesis is that while you would expect the shooting percentages to go down across the board because of pressure and tighter defense, we can identify players that are the most and least "clutch" (this is more of an abstract term used to describe players who take and make tough shots during clutch time).
If a player has a very significant drop off in regular time vs clutch situations, we can imply that their respective teams would be better off with someone else taking a majority of the shots in clutch time.


![Screenshot 2024-07-09 at 11 34 21 PM](https://github.com/anikaranam/ML-Projects/assets/42919048/27d9f27d-2516-4479-82e6-ed2380777317)


### Defensive distance analysis:

In this project, based on NBA shot log data from the 2014/15 season, I wanted to measure the average close out distance for all NBA players and see if this data correlates with popular perceptions of different players' defensive aptitude.
Some insights:
1. There was an average of ~ 5.5 feet of distance between the shooter and Kobe Bryant when he was the nearest defender. This season was one of Kobe's 4 worst seasons defensively, with a defensive rating of 110.2. Given that a distance of around 6 feet is considered to be a "wide open" shot in the NBA, this explains the poor defensive rating for Kobe.

2. Most of the players with the lowest average feet of distance are centers, which aligns with our understanding of the fact that centers are mostly situated in and around the paint where there is not imuch distance between the shooter and the nearest defender.


![Screenshot 2024-07-09 at 11 34 53 PM](https://github.com/anikaranam/ML-Projects/assets/42919048/42ebd851-31ef-48da-b09b-715ecffa7886)


### Comparison of the popularity of the midrange shot versus the three point shot

An aspect of the modern NBA game that is very different from the late 90s and 2000s is the number of three pointers being attempted and converted on a regular basis. But what kind of shots are teams moving away from in favor of the three? The graph below illustrates the ever declining popularity of the midrange shot (roughly 10-16 feet from the basket) contrasted with the rapid growth of the three pointer in recent years.

Notice when the percentage of three point shots really starts to take off: around 2012-13 / 2013-14. The 5-6 years following that saw a rapid increase in the number of three pointers being attempted league-wide. This just so happens to coincide with the reign of one of the NBA's greatest ever dynasties - the Golden State Warriors. With Mark Jackson and later Steve Kerr, the Warriors embraced small ball, led by arguably the 2 greatest shooters ever bombing threes all game. The Rockets are another team that had a lot of success with the three-heavy approach, led by Mike D'Antoni. 

It's no surprise that the success of these teams inspired a shift in the league paradigm and teams' approach towards the three.


![Screenshot 2024-07-09 at 11 35 14 PM](https://github.com/anikaranam/ML-Projects/assets/42919048/ea9e4cbb-1382-4412-891e-0b3f8a56e54d)


This next chart also shows exactly how the shot proportions changed over the years. The percentage of short distance shots (layups, dunks, floaters etc) remained about the same between 1997/98 and 2019/20, but a huge chunk of the midrange shots were replaced by threes.


![Screenshot 2024-07-09 at 11 35 33 PM](https://github.com/anikaranam/ML-Projects/assets/42919048/433d4f93-33e0-4ceb-9607-7ce2ac66d73a)


<img width="942" alt="Screenshot 2024-07-26 at 11 00 26 PM" src="https://github.com/user-attachments/assets/b3878709-29db-495f-972b-4f42326cb608">



