## Updating the PostgreSQL Database with New Formulas

The instructions for inserting a new formula below are not generalized. They assume you can customize the commands and queries for the file paths, column names, and values with which you are working.

#### 1.  Navigate to folder where the Git database for the application is located.

    bash
    
    cd main_projects/python_projects/physics_web_app_nextjs_heroku/backend/physics_web_app_3



#### 2.  Launch a Heroku PostgreSQL Session

    bash
    
    heroku pg:psql



#### 3.  INSERT New Formula

    psql
    
    INSERT INTO formula (formula_name, latex)
    VALUES ('Conservation of momementum',
    '\vec{p}_1 (initial) + \vec{p}_2 (initial) = \vec{p}_1 (final) + \vec{p}_2 (final)');



#### 4.  Run a SELECT to Confirm the INSERT Worked

    psql
    
    SELECT * FROM formula;



#### 5.  Refresh Web Page

If the formula information looked correct in step 4 above, refresh the website to confirm the formula is correctly displayed.



#### 6.  Update (Correct) the Formula If Necessary

In case the LaTeX is not correct and the formula is not displayed correctly in the web page, update the LaTeX as follows:

    psql
    
    UPDATE formula SET latex = '\vec{p}_1 (initial) + \vec{p}_2 (initial) = \vec{p}_1 (final) + \vec{p}_2 (final)' WHERE id = 34;

