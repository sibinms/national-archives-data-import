# National Archives Open Data API based Data import


- **How to build the code ?**
  - Install docker desktop : https://docs.docker.com/desktop/
  - Clone the project directory from GitHub
  ```
  git clone https://github.com/sibinms/national-archives-data-import.git
  ```
  - Move to the project directory 
  ```
   cd national-archives-data-import
  ```
  - Create .env file
  ``` 
    touch .env
  ```
  - Add the following values to the .env values
  ```
    DEBUG=1
    SECRET_KEY=jjFOtlCde0mHjUGfh23rH0ArHIpDvycY5taHc8Eq
    DJANGO_ALLOWED_HOSTS=*
  ```
  - Run the docker
  ```
  docker-compose up 
  ```
  - Open a new terminal in the same folder and run the following commands
  ```
    docker-compose exec web sh
    python manage.py migrate
    python manage.py createsuperuser
  ```
  - Now your development server is ready , if needed check the admin http://0.0.0.0:8000/admin/login/


- **How to run the output ?**
  - Now we can import the data using management command.
  - Open a new terminal in the same folder and execute the following commands.
     _Note: Replace <record_id> with actual record ID you wanted to import_
  ```
    docker-compose exec web sh
    python manage.py import_record_by_id <record_id> 
  ```
  - Once you successfully imported the data go to : http://0.0.0.0:8000/archive-records/
  - You will be able to see the following page
<img width="447" alt="Screenshot 2022-10-18 at 7 51 05 PM" src="https://user-images.githubusercontent.com/32489487/196457202-6efa9080-92e6-4feb-adf9-f25450f966c9.png">

  
