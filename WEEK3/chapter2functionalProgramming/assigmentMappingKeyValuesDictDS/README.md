# Lab Instructions: Mapping key-values to Dictionary data structures 

So far you have learned that Python has different techniques to modify a given iterator sequence such as list or dictionary using comprehensions,  
map() function and so on. Now you will be utilising what you have learned. Let’s say you have a list of employee data for the Little Lemon company.  
You want to create login accounts for the employees and you will create usernames for these employees in the first example. 

You also want to update the roster for these employees on the calendar and want easy access to their initials and employee IDs, as they are all unique.  
To get that, in the second example, you will create a dictionary with the required information. 
<br><br>

## Exercise Instructions

1. Open the `comprehensions.py` file

2. Implement the `to_mod_list()` function by using the `map()` function to apply `mod()`
   to all elements within `employee_list`.  
    Assign the result of it to a new variable called `map_emp`. Convert `map_emp` to a list and return it. 
   - The `mod()` function returns a string value for example such as `“Lisa_Cold Storage”` from the dictionary passed to it. <br><br>

3. At this point you should have a list of the values such as: `“Lisa_Cold Storage”` mentioned above.  
But that is no good for a username with the whitespace present in it.  
    - Implement the `generate_usernames()` method by using list comprehension and the `replace()` over `mod_list`  
  to replace all spaces `(" ")` with underscores `("_")`. 
    - Return the resulting list. <br><br>

4. We want to create a dictionary that stores employees' first initials and IDs. 
    - Implement `map_id_to_initial()` by using dictionary 
comprehension over the `employee_list` to create a dictionary   
where each key is the 
first letter of an employee's name and the value is the employee's ID.<br><br>

5. Run the script by opening the terminal and executing the command:
    ```
    python3 comprehensions.py
    ```

<br>


## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 