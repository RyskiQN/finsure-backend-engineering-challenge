# finsure-backend-engineering-challenge
The Finsure Back-end Engineering Challenge is a way for applicants to
demonstrate their skills and overall approach to application development.
The requirements are intentionally sparse (the devil is in the detail). We
don't want you to do a lot, but what you do should be your best work.
The Objective
- Read and understand the Challenge
- Create solutions that satisfy the requirements
- Send a link to the Git repository containing your solution to:
kevin.nguyen@finsure.com.au

# Background
The first feature in the sprint is to create an API that allows
administrators to manage all the lenders in the system.

# Requirements
Create a RESTful API using Django. The API should be backed by a MariaDB
database, conform to the JSON:API specification and should implement
endpoints that provide the following functionality:
1. Create a new Lender
2. List all Lenders (five per page)
1. List active lenders
3. Get a specific Lender
4. Update a specific Lender
5. Delete a specific Lender
6. Bulk upload Lenders in CSV format
7. Download Lenders in CSV format

# Additional Info
Below are the attributes of a control. All attributes are required.
| Name                   | Description                                                     |
|-----------------------:|:----------------------------------------------------------------|
|Name                    | Name of the lender                                              |
|Code                    | 3 letter abbreviated name                                       |
|Upfront Commission Rate | A percentage describing the amount of commission taken per Loan |
|Trial Commission Rate   | A percentage describing the amount of commission taken per Loan |
|active                  | A flag to determine if this Lender is active in the system      |
