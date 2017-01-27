Jats
======

A dead simple task list manager where tasks can be assigned to people.

The point of this project is to demonstrate the following:

1. Using Node.js build tools with Django is fun and easy with the great work from (Owais)[] on django-webpack-loader.
2. Using something like webpack with Vuejs can make asset pipelines really simple in PaaS environments.
3. Builds in a Heroku dyno can be reasonably fast with multiple buildpacks.
4. Single Page Applications or any JavaScript heavy application is possible with Django.

Installation
---------------

This application assumes a modern python development environment that
includes:

Python 3.6, virtualenv, pip, etc. Installing python 3 now means getting
the others by default but it is the onus of the user to create a virtual
environment tied to python 3.

The other main environmental dependency is Node.js version 6.x.

Database: Postgres 9.5

### Steps

1. Clone the repository

2. Install Python dependencies (inside your activated virtualenv):
    ```
    pip install -r requirements/dev.txt
    ```
3. Install Node.js dependencies:
    ```
    npm install
    ```
4. Copy the environment variables template:
    ```
    cp .env.template .env
    ```
Now you should set that up to your heart's content!
The rest of this guide assumes that you have in fact used the alias I provided for the management script.

5. Migrate your database
    ```
    manage migrate
    ```

6. Create a superuser:
    ```
    manage createsuperuser
    ```

Now you have everything you need to do all of the fun stuff:

* Run the development server (`manage runserver`)

* Run the webpack watcher (`webpack --watch`) *NOTE*: this assumes you have webpack installed globally (not always a great idea) so choose your binaries wisely with this one.

* Check out the browsable API at `/api/`

* Make some tasks at `/` (assuming you've logged in with the credentials you've made)

