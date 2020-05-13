Q1='''select a.id,a.fname,a.lname,a.gender from actor a inner join cast c 
on a.id=c.pid inner join movie m on m.id=c.mid where m.name like 'Annie%';'''


Q2='''select m.id,m.name,m.rank,m.year from movie m inner
join moviedirector  md on m.id=md.mid inner join director d on d.id=md.did 
where (d.fname ='Biff' and d.lname='Malibu') and (m.year in ( 1999,1994,2003) )
order by  m.rank desc ,m.year asc;'''   

Q3='''select m.year,count(m.id) from movie m group by year
having (avg(rank) > (select avg(rank) from movie))  order by m.year asc;'''

Q4='''select m.id,m.name,m.year,m.rank from movie m  where m.year = 2001 and 
rank < ( select avg(rank) from movie where year=2001) 
order by m.rank desc limit 10;'''

Q6='''select distinct a.id from actor a inner join cast c on
a.id=c.pid group by c.pid,c.mid 
having count(distinct(c.role))>1 order by c.pid asc; '''  

Q7='''select  fname,count(fname) from director 
group by director.fname having count(fname) > 1; '''
 
 
 
