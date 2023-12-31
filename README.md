# finsure-backend-engineering-challenge
The Finsure Back-end Engineering Challenge is a way for applicants to
demonstrate their skills and overall approach to application development.
The requirements are intentionally sparse (the devil is in the detail). We
don't want you to do a lot, but what you do should be your best work.
The Objective
- Read and understand the Challenge
- Create solutions that satisfy the requirements

# Background
The first feature in the sprint is to create an API that allows
administrators to manage all the lenders in the system.

# Requirements
Create a RESTful API using Django. The API should be backed by a MariaDB
database, conform to the JSON:API specification and should implement
endpoints that provide the following functionality:
- [X] Create a new Lender
- [X] List all Lenders (five per page)
  - [X] List active lender
- [X] Get a specific Lender
- [X] Update a specific Lender
- [X] Delete a specific Lender
- [X] Bulk upload Lenders in CSV format
- [X] Download Lenders in CSV format

# Additional Info
Below are the attributes of a control. All attributes are required.

| Name                   | Description                                                     |
|-----------------------:|:----------------------------------------------------------------|
|Name                    | Name of the lender                                              |
|Code                    | 3 letter abbreviated name                                       |
|Upfront Commission Rate | A percentage describing the amount of commission taken per Loan |
|Trial Commission Rate   | A percentage describing the amount of commission taken per Loan |
|active                  | A flag to determine if this Lender is active in the system      |

# Setup
Packaged db with 

    mariadb-dump.exe --databases --user=root --password=password lendersdb > db_backup.sql

Restore database with the following command 
        
    cd <./lenders directory>
    mysql --user=root --password=password < db_backup.sql
    python -m venv .venv
    ".venv/Scripts/activate" (source .venv/bin/activate for Linux)
    pip install -r requirements.txt
    python manage.py runserver

  main lenders app exists at url '/lenders'
