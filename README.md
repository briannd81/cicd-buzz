How to deploy this application
------------------------------

CICD DEPLOYMENT TO HEROKU
-------------------------
1. Host the code on github
   - requires an account at https://github.com/
2. Connect to Travis CI to run tests on every commit
   - requires an account at https://travis-ci.org/
   - free for public GitHub repo
   - use federated login using GitHub account
   - set up 3 environment variables under the settings view of the repo at Travis CI:
     - DOCKER_EMAIL
     - DOCKER_PASS
     - DOCKER_USER
   - enable Travis CI to start a build at each Push and Pull Request for the repo by flipping the switch in front of your repo
3. Add Better Code Hub to pipeline to check code quality
   - seamlessly integrates with GitHub
   - use federated login using GitHub account
4. Deploy to Docker Hub
   - sign up at https://hub.docker.com/
   - Travis CI will create a docker image at the end of each pipeline build
5. Deploy application to Heroku
   - Heroku is a cloud platform for hosting web applications
   - Travis CI will deploy the Docker image to Heroku
   - sign up at https://signup.heroku.com/
   - create an app in Heroku
   - Go back to Travis CI and create two more variables:
     - HEROKU_API_KEY
     - HEROKU_APP_NAME
6. Commit your GitHub code to start deploying the application


LOCAL DEVELOPMENT DEPLOYMENT
----------------------------
1. Clone the repo to your development machine
2. Start the app using "python app.py"
3. Use web browser to access your app using the ip address of your machine and port 5000, i.e. http://10.5.5.19:5000
4. You can also launch the docker image straight from Docker Hub: docker run -p5000:5000 --rm -it <YOUR_DOCKER_USERNAME>/<YOUR_IMAGE_NAME>:latest

