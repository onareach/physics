# Modify the Database and Change the Display on Vercel

The purpose of this modification is to control the order in which formulas are displayed on the webpage.

(Please see https://github.com/onareach/physics/tree/main/Web_Prototype_on_Heroku and https://github.com/onareach/physics/blob/main/Web_Prototype_on_Heroku_and_Vercel/Migrating_Front-End_of_Physics_Web_App_from_Heroku_to_Vercel.md for description of the application prior to modifying the database and web page.)



### Major Steps to the Modification

- **Modify the database table: Add a `display_order` column.**
- **Assign `display_order` values.**
- **Update the API.**



#### 1.  Navigate to the folder where the application's Git database is located.

    bash
    
    cd main_projects/python_projects/physics_web_app_nextjs_heroku/backend/physics_web_app_3



#### 2.  Launch a Heroku PostgreSQL Session

    bash
    
    heroku pg:psql



#### 3.  Assign  `display_order` Values:

    psql
    
    ALTER TABLE formula ADD COLUMN display_order INT;



#### 4.  Enter Display Order Values:

    psql
    
    UPDATE formula SET display_order = 1 WHERE id = 1;
    UPDATE formula SET display_order = 2 WHERE id = 34;
    UPDATE formula SET display_order = 3 WHERE id = 2;
    UPDATE formula SET display_order = 4 WHERE id = 3;



#### 5.  Add an `ORDER BY` Clause to the `SELECT` Statement in `app.py`:

Navigate to the `app.py` file in the `backend/physics_web_app_3` directory. Open the file and modify the `cursor.execute` statement to include an `ORDER BY` clause as follows:

    cursor.execute("SELECT id, formula_name, latex FROM formula ORDER BY display_order;")

Save the file.



#### 6.  Git Commit, Push Changes, and Restart Heroku

    bash
    
    git add .
    git commit -m "Update the Vercel URL in app.py."
    git push heroku main
    heroku restart



#### 7.  Refresh Web Page

Refresh the web page to confirm that the formulas appear in the desired order.
