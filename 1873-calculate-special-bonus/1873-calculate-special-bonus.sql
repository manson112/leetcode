# Write your MySQL query statement below

select employee_id,
       if(name not like 'M%' and mod(employee_id, 2) != 0, salary, 0) as bonus
  from Employees
  order by employee_id