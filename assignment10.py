
Q1='''select player. player_id,player.team_id,
player.jersey_no,player.name,player.date_of_birth,
player.age from player inner join matchcaptain on 
matchcaptain.team_id=player.team_id left join 
goaldetails on player.player_id=goaldetails.player_id 
where player. player_id=matchcaptain.captain and
goaldetails.goal_id is null;'''


Q2='''select team_id,count(match_no) from 
matchteamdetails group by team_id;'''


Q3='''select team_id,count(goal_id) *1.0/(select count(player_id)
from player group by team_id) as avg_goal_score from
goaldetails group by team_id;'''


Q4='''select captain,count(captain) 
from matchcaptain group by captain;'''



Q5='''select count(distinct(player_id)) from
matchcaptain mc inner join match m on mc.match_no =m.match_no
inner join player p on  p.team_id=mc.team_id 
where (p.player_id=mc.captain and mc.captain=m.player_of_match) 
and (mc.match_no=m.match_no);'''   



Q6='''select distinct player_id  from player p where exists
(select * from matchcaptain mc where  p.player_id=mc.captain )
and not exists(select * from match m where p.player_id=m.player_of_match);'''



Q7='''select strftime('%m',play_date) as month ,count(match_no) 
as number_of_matches from match group by month 
order by number_of_matches desc;'''



Q8='''select  distinct jersey_no,count(captain)  as cc from matchcaptain
mc inner join player p on mc.captain=p.player_id group by jersey_no order 
by cc desc,jersey_no desc;'''


Q9='''select player_id ,avg(audience)  avgs from matchteamdetails mtd  
inner join player p on  p.team_id=mtd.team_id inner join match m 
on  mtd.match_no=m.match_no  group by p.player_id
order by avgs desc, player_id desc;'''



Q10='''select team_id,avg(age) from player group by team_id;'''



Q11='''select avg(age) from player p inner join matchcaptain mc 
on p.team_id=mc.team_id where mc.captain=p.player_id;'''



Q12='''select strftime("%m",date_of_birth) as month ,count(player_id) as no_of_players
from player where month=strftime("%m",date_of_birth) group by month order by 
no_of_players desc,month desc'''



Q13='''select captain,count(win_lose) as wl from matchteamdetails 
mtd inner join matchcaptain mc on mtd.team_id=mc.team_id
 where  mc.match_no=mtd.match_no and win_lose='W'group by captain order by wl desc ;'''



