# Write your MySQL query statement below
select a.name NAME, sum(b.amount) as BALANCE
  from Users a 
  join Transactions b 
    on a.account = b.account
 group by a.name having sum(b.amount) > 10000
