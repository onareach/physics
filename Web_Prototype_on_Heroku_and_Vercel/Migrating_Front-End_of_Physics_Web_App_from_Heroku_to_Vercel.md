# Migrating the Frontend of Web App from Heroku to Vercel

This proof-of-concept project shows how the front-end of a three-tier application (database, back-end server, and webpage) can be migrated from Heroku to Vercel. The goal of this project is to convert the Heroku/Flask backend into an API that a Next.js app on Vercel can access.

(Please see https://github.com/onareach/physics/tree/main/Web_Prototype_on_Heroku and for a description of the application prior to migrating the front-end to Vercel.)

#### Target Project File Structure

    physics-formula-viewer/   		# Main project folder
    │── backend/              		# Backend master project folder
    	│── physics_web_app_3/			# Flask/FastAPI app (deployed on Heroku)
    │── frontend/             		# Frontend master project folder
    	│── [Next.js app files]			# Next.js app (to be deployed on Vercel)



### Major Steps to the Conversion

1. Prepare Heroku application backend.
2. Set up a Next.js app locally.
3. Connect Next.js frontend to Heroku backend.
4. Deploy Next.js app on Vercel.
5. Final configuration. (Give public access to Vercel app.)



#### A few notes about Node.js, Next.js, NPM, React, and DOM

**Node.js** is a JavaScript runtime environment that allows you to run JavaScript code outside the browser. It is used to build backend servers, run scripts, and execute JavaScript on the server side. It is required to run Next.js because Next.js uses Node.js to handle server-side rendering (SSR), API routes, and builds. Node.js runs the Next.js development server. You can think of Node.js as the engine that powers JavaScript outside the browser.

**Next.js** is a *React* framework for building full-stack applications. Next.js is built on top of React and provides features like server-side rendering (SSR), static site generation (SSG), and API routes. You can think of Next.js as a framework that makes React more powerful, using Node.js to enable server-side functionality. If you're only using Next.js for front-end development, you don't need extensive Node.js knowledge. But if you're using API routes, server-side rendering, or custom backend logic, knowing Node.js is likely essential.

**Node Package Manager** (npm) plays the same role for JavaScript that pip (Preferred Installer Program) plays for Python. It is used to install, manage, and update JavaScript libraries (called packages or modules) for both backend and frontend development. It comes automatically installed when you install Node.js. A tool called `npx` comes with `npm` and allows you to run a package without installing it globally. For example, the command used below  `npx create-next-app` fetches and runs the Next.js setup script without installing it globally.

**React** is a JavaScript library for building user interfaces (UIs), primarily for single-page applications (SPAs). It was developed by Facebook (now Meta) and is open-source. It enables fast, interactive, and reusable UI components. React is used for building dynamic web apps, creating reusable UI components, and making frontend development more structured and scalable.

The reasons for using React:

- React is **Component-Based**. UIs are built from independent, reusable components.
- **Fast Updates with Virtual DOM** (document object model). React efficiently updates only the necessary parts of the page.
- **Declarative Syntax**. Instead of manually manipulating DOM, you describe how the UI should look, and React updates it.
- **Great for Large-Scale Applications**. Used by companies like Netflix, Facebook, and Uber.
- **Huge Ecosystem**. Works well with Next.js, React Native (for mobile apps), and many UI libraries.



**DOM (Document Object Model)** is a programming interface that represents a web page as a tree-like structure. It allows JavaScript to dynamically update, add, and remove elements on a webpage. In the DOM tree, every HTML element is a node. 

To give an example of how the DOM represents an HTML page, consider the following HTML code:

    html
    
    <!DOCTYPE html>
    <html>
      <head>
        <title>My Page</title>
      </head>
      <body>
        <h1>Hello, World!</h1>
        <p>This is a paragraph.</p>
      </body>
    </html>


The DOM representation (tree structure) is as follows:

    Document
     ├── <html>
     │    ├── <head>
     │    │    ├── <title>My Page</title>
     │    ├── <body>
     │         ├── <h1>Hello, World!</h1>
     │         ├── <p>This is a paragraph.</p>


Every element (&lt;html&gt;, &lt;head&gt;, &lt;body&gt;, &lt;h1&gt;, etc.) is a node in this tree.

JavaScript can access and modify the DOM using the  `document` object. Here's an example of changing text:

 

    js
    
    document.querySelector("h1").textContent = "Hello, React!";

This changes the content of a heading (&lt;h1&gt; Hello, World&lt;/h1&gt; ) to a new value of (&lt;h1&gt; Hello, React&lt;/h1&gt;).

### Major Step 1: Prepare Heroku App Backend

#### 1. Verify Backend is Running on Heroku

    bash
    
    heroku open --app my-physics-formula-viewer-3x

This should open the current app (hosted entirely on Heroku) in the web browser.



#### 2.  Install CORS Package and Regenerate requirements.txt

CORS (Cross-Origin Resource Sharing) is a security feature in web browsers that controls how resources (like fonts, APIs, or data) can be accessed from a different domain than the one that served the web page. By default, browsers follow the Same-Origin Policy (SOP), which blocks JavaScript from sending requests to a different domain. CORS relaxes this policy safely by allowing controlled cross-origin requests. If a frontend app tries to fetch data from an API on a different domain, the browser blocks the request unless the API explicitly allows it via CORS headers. A server can enable CORS from all origins:

    http
    
    Access-Control-Allow-Origin: *

Or, CORS can allow requests from specific domains:

    http
    
    Access-Control-Allow-Origin: https://[allowed_domain].com



Activate the Python virtual environment (venv) inside the project folder and install the flask-cors package:

    venv
    
    pip install flask-cors

Regenerate the requirements.txt file:

    bash
    
    pip freeze > requirements.txt



#### 3.  Replace app.py

Update app.py with the following code:

    # app.py
    # This app.py was created in order to expose an API endpoint for
    # Vercel Next.js to call
    
    from flask import Flask, jsonify
    from flask_cors import CORS
    
    app = Flask(__name__)
    
    # Allow frontend to access backend
    CORS(app, origins=["http://localhost:3000", "https://your-vercel-app.vercel.app"])
    
    @app.route('/api/hello', methods=['GET'])
    def hello():
        return jsonify({"message": "Hello from Flask!"})
    
    if __name__ == '__main__':
        app.run(debug=True)

Note that on the line under the comment '# Allow frontend to access backend,' we are granting localhost access to the backend API. Later, the URL of the Vercel hosted frontend will be inserted.

The `jsonify()` function in the code above converts Python data structures (such as dictionaries and lists) into JSON format and returns an HTTP response. When you return JSON data using  `jsonify()`, Flask automatically sets the response header as follows:

    http
    
    Content-Type: application/json

This tells the client (e.g., a browser) that the response is JSON (in contrast to HTML). Browsers render HTML visually as web pages, whereas JSON is processed by a JavaScript interpreter. After processing the JSON data, browsers such as Chrome, Firefox, and Edge display it in a readable format. (Older browsers may display it as plain text.) A Next.js frontend app that receives JSON from the backend API will use the data to generate a webpage. 

 

#### 4.  Commit and Push Changes to Git

    bash
    
    git add .
    git commit -m "Update requirements.txt and app.py to create the backend API."
    git push heroku main



#### 5.  Restart Heroku App and Verify Its Process Status

    bash
    
    heroku restart my-physics-formula-viewer-3x
    
    heroku ps

(The "ps" in the previous command is short for process status.) 

The output should be similar to the following:

    (terminal output)
    
    Eco dyno hours quota remaining this month: 995h 14m (99%)
    Eco dyno usage for this app: 0h 0m (0%)
    For more information on Eco dyno hours, see:
    https://devcenter.heroku.com/articles/eco-dyno-hours
    
    === web (Eco): gunicorn app:app (1)
    
    web.1: idle 2025/03/08 13:43:07 -0800 (~ 1h ago)



#### 6.  Test the API

    bash
    
    curl https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com/api/hello

The output should be:

    (terminal output)
    
    {"message":"Hello from Flask!"}



### Major Step 2: Setup Next.js Locally

#### 1. Use mkdir and mv to create file structure shown at the introduction of this document

The master folder structure (shown near the beginning of this document) needs to be created with mkdir commands, and the older Heroku project folder needs to be moved, using the mv command, inside the backend subfolder. After this is completed, the top of the folder structures should look like this:

    bash
    
    physics_web_app_nextjs_heroku
    ├── backend
    │   └── physics_web_app_3
    └── frontend



#### 2. Install Next.js Locally

Run the following commands:

    bash
    
    cd physics_web_app_nextjs_heroku
    npx create-next-app@latest my-next-app frontend

When you run these commands, you are given the following options:

    bash
    
    Need to install the following packages:
    create-next-app@15.2.2
    Ok to proceed? (y) y
    ✔ Would you like to use TypeScript? … No / Yes
    ✔ Would you like to use ESLint? … No / Yes
    ✔ Would you like to use Tailwind CSS? … No / Yes
    ✔ Would you like your code inside a `src/` directory? … No / Yes
    ✔ Would you like to use App Router? (recommended) … No / Yes
    ✔ Would you like to use Turbopack for `next dev`? … No / Yes
    ✔ Would you like to customize the import alias (`@/*` by default)? … No / Yes

I chose the following:

| Option                  | Choice | Comment by ChatGPT                                           |
| ----------------------- | ------ | ------------------------------------------------------------ |
| Use TypeScript?         | No     | Fine for now. You can add TypeScript later if needed.        |
| Use ESLint?             | Yes    | Good choice. Helps catch bugs and enforce best practices.    |
| Use Tailwind CSS?       | Yes    | Great choice. Tailwind makes styling faster and more flexible. |
| Use src/ directory?     | Yes    | Great choice. Using the src/ directory is a recommended practice for better project organization. |
| Use App Router?         | Yes    | Recommended. This enables Next.js' latest features like Server Components and better API handling. |
| Use Turbopack?          | Yes    | Good for speed. Turbopack makes development builds faster.   |
| Customize import alias? | No     | Fine for now. The default @/* alias is useful for cleaner imports, but you can add it manually later if needed. |

After choosing the options, the output was as follows:

    bash
    
    Creating a new Next.js app in /Users/davidlong/main_projects/python_projects/physics_web_app_nextjs_heroku/frontend.
    
    Using npm.
    
    Initializing project with template: app-tw 
    
    Installing dependencies:
    - react
    - react-dom
    - next
    
    Installing devDependencies:
    - typescript
    - @types/node
    - @types/react
    - @types/react-dom
    - @tailwindcss/postcss
    - tailwindcss
    
    added 48 packages, and audited 49 packages in 23s
    
    10 packages are looking for funding
      run `npm fund` for details
    
    found 0 vulnerabilities
    Initialized a git repository.
    
    Success! Created frontend at /Users/davidlong/main_projects/python_projects/physics_web_app_nextjs_heroku/frontend
    
    npm notice 
    npm notice New major version of npm available! 9.8.1 -> 11.2.0
    npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.2.0
    npm notice Run npm install -g npm@11.2.0 to update!
    npm notice 

Do not upgrade npm (Node Package Manager), which is the default package manager for Node.js.



#### 3. Start the Development Server

Run the following commands:

    bash
    
    cd frontend
    npm run dev

You should see output like:

    bash
    
    > frontend@0.1.0 dev
    > next dev --turbopack
    
       ▲ Next.js 15.2.2 (Turbopack)
       - Local:        http://localhost:3000
       - Network:      http://192.168.1.65:3000
    
     ✓ Starting...
    Attention: Next.js now collects completely anonymous telemetry regarding usage.
    This information is used to shape Next.js' roadmap and prioritize features.
    You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
    https://nextjs.org/telemetry
    
     ✓ Ready in 1953ms


Open http://localhost:3000 in your browser, and you should see the default Next.js welcome page.



### Major Step 3: Connect the Next.js Frontend to the Heroku Backend

Now we'll configure the frontend to fetch data from the Heroku API.

#### 1.  Create an Environment Variable File

Create a  `.env.local` file inside the  `frontend` folder:

    bash
    
    touch .env.local

Add the following contents that contain the backend API URL to the file:

    NEXT_PUBLIC_API_URL=https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com

Environment variables prefixed with NEXT_PUBLIC_* are exposed to frontend applications and browsers.

You can confirm that this configuration is in place by opening a new browser tab and entering the following URL:

    (web browser)
    
    https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com/api/hello

The following should appear in the browser:

    (web browser)
    
    {"message":"Hello from Flask!"}



#### 2.  Modify page.tsx

Navigate to the frontend/src/app/page.tsx file, replace its contents with the following code, and save it:

    export default function Home() {
      return (
        <div>
          <h1>Physics Formula Viewer</h1>
          <p>Welcome to your Next.js app using the App Router!</p>
        </div>
      );
    }



#### 3.  Restart the Server

In the Terminal app where the server is running, use the following command to stop the frontend app server:

    Ctrl + C

Then restart the server:

    bash
    
    npm run dev

After restarting the server, refresh the browser tab displaying http://localhost:3000. You should now see the following text on that web page (instead of the Next.js welcome page seen previously):

    (browser)
    
    Physics Formula Viewer
    Welcome to your Next.js app using the App Router!

This confirms that the Next.js frontend is running. The frontend project structure now looks like this:

    frontend/
    │── src/                   # Your main project source files
    │   ├── app/               # App Router (instead of "pages/")
    │   │   ├── layout.tsx
    │   │   ├── page.tsx       # Home page (index)
    │   ├── components/        # (Optional) Your reusable UI components
    │   ├── styles/            # Global styles
    │   ├── utils/             # (Optional) Helper functions
    │── public/                # Static assets (images, icons, etc.)
    │── package.json           # npm dependencies
    │── next.config.js         # Next.js config



#### 4.  Modify app.py (backend) to Retrieve Formula Data from the Backend Database, Convert it into a Dictionary, and Process it with `jsonify()`

Replace the code in app.py with the following code:

    # app.py
    # This app.py was created in order to expose an API endpoint for
    # Vercel Next.js to call
    
    import os
    import psycopg2
    from flask import Flask, jsonify
    from flask_cors import CORS
    
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000", "https://your-vercel-app.vercel.app"])
    
    # Get database URL from Heroku environment variables
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    # Function to get formulas from PostgreSQL
    def get_formulas():
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cursor = conn.cursor()
    
        # Query to fetch all formulas
        cursor.execute("SELECT id, formula_name, latex FROM formula;")
        formulas = cursor.fetchall()
    
        # Convert query results to a list of dictionaries
        result = [{"id": row[0], "formula_name": row[1], "latex": row[2]} for row in formulas]
    
        # Close the connection
        cursor.close()
        conn.close()
    
        return result
    
    @app.route('/api/formulas', methods=['GET'])
    def fetch_formulas():
        try:
            formulas = get_formulas()
            return jsonify(formulas)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    if __name__ == '__main__':
        app.run(debug=True)


#### 5.  Git Commit, Push Changes, and Restart Heroku

    bash
    
    git add .
    git commit -m "Update requirements.txt and app.py to create the backend API."
    git push heroku main
    heroku restart



#### 6.  Re-test the API

Re-test the modified API:

    bash
    
    curl https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com/api/formulas

The output should be:

    bash
    
    [{"formula_name":"Momentum","id":1,"latex":"\\vec{p} = m \\vec{v}"},{"formula_name":"Newton's Second Law","id":2,"latex":"F = ma"},{"formula_name":"Test Formula","id":3,"latex":"E=mc^2"}]



#### 7.  Modify page.tsx (frontend)

Replace the contents of page.tsx (in src/app/) with the following code:

    // page.tsx
    
    'use client';
    
    import { useEffect, useState } from 'react';
    
    interface Formula {
      id: number;
      formula_name: string;  // Updated key
      latex: string;
    }
    
    export default function Home() {
      const [formulas, setFormulas] = useState<Formula[]>([]);
      const [error, setError] = useState<string | null>(null);
    
      useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/formulas`)
          .then((res) => {
            if (!res.ok) {
              throw new Error(`HTTP error! Status: ${res.status}`);
            }
            return res.json();
          })
          .then((data) => setFormulas(data))
          .catch((err) => setError(err.message));
      }, []);
    
      return (
        <div>
          <h1>Physics Formula Viewer</h1>
          {error ? (
            <p style={{ color: 'red' }}>Error: {error}</p>
          ) : (
            <ul>
              {formulas.map((formula) => (
                <li key={formula.id}>
                  <strong>{formula.formula_name}:</strong> {formula.latex}
                </li>
              ))}
            </ul>
          )}
        </div>
      );
    }




#### 8.  Restart the Frontend (Local) Server

Press Ctrl + C in the terminal to stop the frontend server, then restart it with:

    npm run dev



#### 9.  Refresh the Browser Tab with the localhost:3000 URL

Refresh the browser window pointing to localhost:3000. You should see the following content:

    (browser)
    
    Physics Formula Viewer
    Momentum: \vec{p} = m \vec{v}
    Newton's Second Law: F = ma
    Test Formula: E=mc^2



#### 10.  Install Better-React-MathJax

Stop the frontend server (Ctrl + C) and run the following command in the frontend directory:

    bash
    
    npm install better-react-mathjax



#### 11.  Modify page.tsx to Use MathJax and Add Spacing

Update src/app/page.tsx:

    // page.tsx
    
    'use client';
    
    import { useEffect, useState } from 'react';
    import { MathJax, MathJaxContext } from 'better-react-mathjax';
    
    interface Formula {
      id: number;
      formula_name: string;
      latex: string;
    }
    
    export default function Home() {
      const [formulas, setFormulas] = useState<Formula[]>([]);
      const [error, setError] = useState<string | null>(null);
    
      useEffect(() => {
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/formulas`)
          .then((res) => {
            if (!res.ok) {
              throw new Error(`HTTP error! Status: ${res.status}`);
            }
            return res.json();
          })
          .then((data) => setFormulas(data))
          .catch((err) => setError(err.message));
      }, []);
    
      return (
        <MathJaxContext>
          <div style={{ marginLeft: '20px', marginTop: '20px' }}>  {/* Added margin */}
            <h1>Physics Formula Viewer</h1>
            {error ? (
              <p style={{ color: 'red' }}>Error: {error}</p>
            ) : (
              <ul>
                {formulas.map((formula) => (
                  <li key={formula.id}>
                    <strong>{formula.formula_name}:</strong>
                    <MathJax>{`\\(${formula.latex}\\)`}</MathJax>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </MathJaxContext>
      );
    }




#### 12.  Restart the Frontend Server and Refresh the Web Browser

    bash
    
    npm run dev

The browser should now render the physics formulas in a proper mathematical format:



<img src="/Users/davidlong/Library/Application Support/typora-user-images/Screenshot 2025-03-12 at 1.13.02 PM.png" alt="Screenshot 2025-03-12 at 1.13.02 PM" style="zoom:50%;" />



### Major Step 4: Deploy to Vercel

#### 1.  Install the Vercel CLI

Run the following command inside the frontend directory:

    bash
    
    sudo npm install -g vercel

Because you are installing Vercel globally, the `sudo` command is necessary to prompt for an administrative password. Enter your password for the machine you are working on.

Note: You may receive warnings that some of Vercel's dependencies have been deprecated. They are likely to be non-critical errors that can be ignored for now.



#### 2.  Run the Vercel Deployment Command

Inside the frontend directory, run the following command:

    bash
    
    vercel

Several configuration prompts will follow. Here's a copy of the login and build dialog:

    Vercel CLI 41.4.0
    > NOTE: The Vercel CLI now collects telemetry regarding usage of the CLI.
    > This information is used to shape the CLI roadmap and prioritize features.
    > You can learn more, including how to opt-out if you'd not like to participate in this program, by visiting the following URL:
    > https://vercel.com/docs/cli/about-telemetry
    > No existing credentials found. Please log in:
    ? Log in to Vercel Continue with Email
    ? Enter your email address: onareach@yahoo.com
    We sent an email to onareach@yahoo.com. Please follow the steps provided inside it and make sure the security code matches Impressive Hyena.
    > Success! Email authentication complete for onareach@yahoo.com
    ? Set up and deploy “~/main_projects/python_projects/physics_web_app_nextjs_heroku/frontend”? yes
    ? Which scope should contain your project? David Long's projects
    ? Link to existing project? no
    ? What’s your project’s name? physics_web_app
    ? In which directory is your code located? ./
    Local settings detected in vercel.json:
    Auto-detected Project Settings (Next.js):
    - Build Command: next build
    - Development Command: next dev --port $PORT
    - Install Command: `yarn install`, `pnpm install`, `npm install`, or `bun install`
    - Output Directory: Next.js default
    ? Want to modify these settings? no
    🔗  Linked to david-longs-projects-14094a66/physics_web_app (created .vercel)
    🔍  Inspect: https://vercel.com/david-longs-projects-14094a66/physics_web_app/AQQVLfb7trZCM5K9tPgrRJvYkkki [2s]
    ✅  Production: https://physicsweb-azec7xnrr-david-longs-projects-14094a66.vercel.app [2s]
    📝  Deployed to production. Run `vercel --prod` to overwrite later (https://vercel.link/2F).
    💡  To change the domain or build command, go to https://vercel.com/david-longs-projects-14094a66/physics_web_app/settings

The production URL to emerge from this is:

    https://physicsweb-azec7xnrr-david-longs-projects-14094a66.vercel.app



#### 3.  Add Production URL (shown just above) to app.py

In the CORS section of the app.py, add the current Vercel URL, so the backend will accept queries from it. 

**NOTE: EVERY TIME YOU RUN THE `vercel --prod` COMMAND, A NEW URL WILL BE GENERATED, AND THE `app.py` FILE WILL NEED TO BE UPDATED.**

    # app.py
    # This app.py was created in order to expose an API endpoint for
    # Vercel Next.js to call
    
    from flask import Flask, jsonify
    from flask_cors import CORS
    import psycopg2
    import os
    
    app = Flask(__name__)
    
    # Add the Vercel production URL to the allowed origins
    CORS(app, origins=[
        "http://localhost:3000",  # Local development
        "https://physicsweb-azec7xnrr-david-longs-projects-14094a66.vercel.app"  # Deployed Vercel site
    ])
    
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    def get_formulas():
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cursor = conn.cursor()
        cursor.execute("SELECT id, formula_name, latex FROM formula;")
        formulas = cursor.fetchall()
        result = [{"id": row[0], "formula_name": row[1], "latex": row[2]} for row in formulas]
        cursor.close()
        conn.close()
        return result
    
    @app.route('/api/formulas', methods=['GET'])
    def fetch_formulas():
        try:
            formulas = get_formulas()
            return jsonify(formulas)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    if __name__ == '__main__':
        app.run(debug=True)




#### 4.  Add the Environment Variables to the Vercel Dashboard

Even though a file named ***.env.local*** exists in the ***frontend/src/app*** directory, Vercel may not automatically detect it, so you need to enter it manually in the *Vercel Dashboard*. To do that, take the following steps:

1. Log in to Vercel (vercel.com). 
2. On the ***Overview*** tab, you will see the project listed as **physics_web_app**.
3. Click on the project name and then click on the ***Settings*** tab. 
4. On the left side of the ***Project Settings*** page, you will find links to various settings. Click on the ***Environment Variables*** link. 
5. On the ***Environment Variables*** page, scroll down to see if the **NEXT_PUBLIC_API_URL** key has been entered. If it has been previously entered, it will be listed just ***above*** the ***Shared Environment Variables*** section. The key name will be visible, but the value will be hidden.
6. If the **NEXT_PUBLIC_API_URL** key does not appear, click on the ***Add Another*** button, enter the key name of **NEXT_PUBLIC_API_URL** and the value of Heroku API URL (which in this case is https://my-physics-formula-viewer-3x-3e0ec7edbc22.herokuapp.com). 
7. Save this new key and value. When you save this value, the Vercel app will be rebuilt and (I believe) its URL will change. However, wait until a later step, when the URL changes again, before updating it in the CORS section of `app.py`.



#### 4.  Rebuild the Vercel App from the Terminal

At this point, you should have two terminal windows open – one for the backend Heroku app and another for the frontend Vercel app.

In the Vercel app Terminal window type the following command to rebuild and restart the app:

    vercel --prod

The output will be similar to the following:

    Vercel CLI 41.4.0
    🔍  Inspect: https://vercel.com/david-longs-projects-14094a66/physics_web_app/5xyyhchwjsehrSNXJwctwVRRRxKU [699ms]
    ✅  Production: https://physicsweb-qzhqw8vdi-david-longs-projects-14094a66.vercel.app [699ms]

Note that the production URL has changed.



#### 5.  Copy the Last Vercel Product URL to app.py

Copy the new Vercel URL into `app.py`. Note the Vercel URL listed in the CORS section just below the localhost entry. (The localhost entry is kept so the program will run both locally (with localhost:3000 and at the public URL provided by Vercel.)

    # app.py
    # This app.py was created in order to expose an API endpoint for
    # Vercel Next.js to call
    
    from flask import Flask, jsonify
    from flask_cors import CORS
    import psycopg2
    import os
    
    app = Flask(__name__)
    
    # Add the Vercel production URL to the allowed origins
    CORS(app, origins=[
        "http://localhost:3000",  # Local development
        "https://physicsweb-qzhqw8vdi-david-longs-projects-14094a66.vercel.app"  # Deployed Vercel site
    ])
    
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    def get_formulas():
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        cursor = conn.cursor()
        cursor.execute("SELECT id, formula_name, latex FROM formula;")
        formulas = cursor.fetchall()
        result = [{"id": row[0], "formula_name": row[1], "latex": row[2]} for row in formulas]
        cursor.close()
        conn.close()
        return result
    
    @app.route('/api/formulas', methods=['GET'])
    def fetch_formulas():
        try:
            formulas = get_formulas()
            return jsonify(formulas)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    if __name__ == '__main__':
        app.run(debug=True)




#### 6.  Git Commit, Push Changes, and Restart Heroku

    bash
    
    git add .
    git commit -m "Update the Vercel URL in app.py."
    git push heroku main
    heroku restart



#### 7.  Launch the App at the Public URL

In a browser window, enter the final Vercel URL:

    https://physicsweb-qzhqw8vdi-david-longs-projects-14094a66.vercel.app

The browser should now display the same content at the public URL as it did when pointing to localhost.



#### 8.  Make the Web Page Public

By default, the Vercel URL is protected with a Vercel login. To make the URL public and remove the login requirement:

1. Log in to Vercel (vercel.com). 
2. On the ***Overview*** tab, you will see the project listed as **physics_web_app**.
3. Click on the project name and then click on the ***Settings*** tab.
4. On the left side of the ***Project Settings*** page, there is a list of links to different types of settings. Click the ***Deployment Protection*** link.
5. Under the **Vercel Authentication** heading, toggle the switch from **Enabled** to **Disabled**, then click **Save**.
6. Open a browser in incognito mode and navigate to the application's URL. The web page should appear without requiring a login.
