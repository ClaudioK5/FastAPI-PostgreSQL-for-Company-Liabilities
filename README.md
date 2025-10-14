# FastAPI-PostgreSQL-for-Company-Liabilities
This backend REST API built with FastAPI and PostgreSQL is designed to manage and track company **liabilities**. It is part of a **larger system that includes FastAPI + PostgreSQL pipeline handling customer orders, company purchases and company's inventory.**

Together, these four services provide the foundation for the generation of a **financial report** on each semester.

The microservice offers two primary endpoints:
- POST /liabilities/ - **to insert a new liability.**
- GET /inventory/ - **to retrieve all the liabilities.**

All data is saved in a PostgreSQL database (fastapi_company_liabilities) and is containerized with **Docker** to allow easy deployment from anywhere.
