# Ecommerce site
Ecommerce site build with (?), Python with FastAPI and MongoDB. Demo at {todo}
## Configuration
Enter your MongoDB connection string, PayU and Google API credentials, and your randomly generated SECRET_KEY in ```back/src/app/secrets.py```. You can generate your secret key using OpenSSL.
```
openssl rand -hex 32
```
## Running application
### Run API
Enter ```back/src``` folder and install all dependencies.
```
pip install -r requirements.txt
```
Run API using uvicorn server.
```
uvicorn app.main:app --reload
```