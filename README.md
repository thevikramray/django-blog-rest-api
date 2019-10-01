STEPS TO USE THIS PROFILE REST API IN LOCALSERVER-

# 1--> INSTALL MINICONDA https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
# 2-->conda create -n test_env python=3.5.4
        (this will create a virtual env with python 3.5.4 without any packages) #
# 3-->conda activate test_env
# 4-->pip install -r requirements.txt
# 5-->python manage.py makemigrations
        (optional)
# 6-->python manage.py migrate
# 7-->python manage.py createsuperuser
        (put all credentials and yes for all prompt)
# 8-->python manage.py runserver
# 9-->head over to 
    http://localhost:8000/api/ for api root.
    http://localhost:8000/api/profile/  for creating user , then 
    http://localhost:8000/api/login for generating Token for MOD HEADER . ##
    http://localhost:8000/admin for Django admin and login from the credentials from step 7.

    ## follow this link to get yourself authenticated 
#       https://stackoverflow.com/questions/39320657/how-do-i-set-up-token-authentication-properly-with-django-rest-framework

if you face any difficulties , follow this-
#    https://coderwall.com/p/aykl2w/setup-an-existing-django-project



# FEATURES -

# CREATE USERS AND EACH USER CAN LOGIN USING THEIR TOKENS
# LOGGED-IN USERS CAN VIEW ALL USERS POSTS, ADD NEW POST, EDIT, DELETE THEIR OWN POST
# NOT-LOGGED-IN USER CANNOT ADD POSTS BUT HE CAN VIEW ALL POSTS
# SEARCH FUNCTIONALITY IN USER AND BLOG -- http://localhost:8000/api/profile/?search=amit
# security:
    - USER CANNOT EDIT OR DELETE OTHER USER POST




----------------------------------------------------------------------------------------------------------------
#conda create will "Create a new conda environment from a list of specified packages."
 ( https://conda.io/docs/commands/conda-create.html )

What list??!? The .condarc file is the conda configuration file.

https://conda.io/docs/user-guide/configuration/use-condarc.html#overview

-------------------------------------------------------------------------------------------

To avoid conda from installing all default packages you can try this

 conda create --name foot35 --no-deps python=3.5

 ----------------------------------------------------------------------------------------
 # NOTE: THIS API WORKS PERFECT IN LOCALSERVER ,IF YOU WANT HOST THIS API IN SERVERS 
 # , YOU WILL NEED SOME CHANGES IN settings.py FILE 


 # YOU CAN SHARE OR USE THIS AS A PERSONAL PROJECT.