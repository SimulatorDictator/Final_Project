# Board Game Reservations App

## Project Brief

For this project I was given the brief to design, produce, and deploy a flask web app of my choosing. The app must include integration with a MySQL database, and CRUD functionality. It must contain at least two tables sharing a one-to-many relationship. The structure of this app is shown in the diagram below.

![Component-level Diagram](https://user-images.githubusercontent.com/111743157/198574205-273effbf-f633-463f-912d-6e30fbaa0e97.jpg)

The app must be hosted and deployed using containers, and a CI/CD pipeline must be used to automatically test, build, and delpoy the application. 

## App Design

I have built a python flask app for use in a board games cafe. Current board games can be added to the database, as can customers with their name, table number, and board game reservation (create functionality). The index page shows the current games and reservations (read functionality). Both games and reservations can be edited (update functionality), and removed from the database (delete functionality).

The two tables created are “Board Games” and “Customers”, with each game associated with multiple customers (one-to-many relationship). The ERD for these databases is shown below.

![ERD](https://user-images.githubusercontent.com/111743157/198567114-1e20b2eb-1a0e-4f41-be14-f1492af27c17.jpg)

## Pipeline

This project requires the integration of a CI pipeline, including version control, virtual environment, containers, and a build server.

Git was used as version control, with the project repository hosted on Github. This allows changes to be made and committed, while keeping the commit history for other versions. I began by committing a working flask app to the main branch. Changes used for tests and containerisation were implemented on separate branches. A .gitignore file is used to prevent the upload of the created database, and unnecessary information.

The application was originally created in Visual Studio Code, using a virtual environment. The develop environment was created using a python3 virtual environment hosted on a virtual machine using Ubuntu 20.04. This allows pip installs, and ensures that running the app will not conflict with any other pip installs on the same machine.

Docker containers were used in this project to create 3 packages: the flask application, the MySQL database, and Nginx. Deploying these 3 containers hosts the application on the local public IP, connects it to the database, and allows access via a reverse proxy. These were uploaded to Dockerhub for use with the Dockercompose and Dockerswarm. A docker compose file was used to define and run these containers using a single command. This was further expanded by using docker swarm deployment. Using two virtual machines (master and worker nodes), I am able to run the containers as a service, and deploy them across two machines. I can access my app via the public IP addresses of the machines.

Jenkins was used as a CI server. It was connected to the git repository, and automatically tested, built, and deployed the application using the docker compose file. It connected to a webhook, which triggered an automatic Jenkins build when a change is made to the code.

This pipeline is shown in the diagram below.

![CICD Diagram](https://user-images.githubusercontent.com/111743157/198567069-f30ce1d7-b904-4b70-817d-2c51469f6cda.jpg)

## Requirements

For this project, I used two virtual machines, one Master, and one Worker. The Master requires: Docker, Dockercompose, Jenkins, Python, Pip. The Worker requires: Docker, Python, Pip. Port 80 must be open on both machines to access the application.

## Risk Assessment

Below is the risk assessment for the project. It has been updated with issues I encountered while developing the project.

![Risk Assessment-1](https://user-images.githubusercontent.com/111743157/198567132-b8cb6ad9-712d-40e2-90b5-1bd0486ca86a.png)

## Testing

Testing is required for the project. In this case, unit testing using pycharm was implemented. This tests the functionality of the app. Unit tests were written for the create, read, update, and delete functionality. These tests feed in a test game, and a test reservation. Using this information, we are testing that the routes of my app return a 200 response.

The tests I have written currently have poor coverage, as they encounter import error. This has been added to my list of work for the future. The coverage is shown below, with test_.py only reaching 5% coverage.

![test coverage](https://user-images.githubusercontent.com/111743157/198889848-9f177e53-f7d2-4416-bec7-9b329158404b.png)


## Future Work

My first priority is creating functioning tests. This will ensure that my application is functional before deploying it from Jenkins.

Currently, I am using two virtual machine. The master node is also hosting Jenkins. In the future I will run Jenkins on a third separate machine.

I will implement environment variables to ensure that sensitive information is not uploaded to GitHub.

I would like to implement a queue system for board game reservations. As two customers can reserve one board game, it would be useful to see who reserved it first, and at what time.

Finally, I will improve the layout and aesthetics of the application. I will create a traditional table display for the board games and reservations.
