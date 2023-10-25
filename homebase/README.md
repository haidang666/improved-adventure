# START EXPRESS API

run code in terminal
```
cd express-api
npm install
npm run start
```

## Call API by CURL
### Post User
```
curl --location --request POST 'http://localhost:3000/api/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "alex",
    "email": "alex@gmail.com"
}'
```

### Get User
```
curl --location --request GET 'http://localhost:3000/api/users/1'
```

### Get All Users
```
curl --location --request GET 'http://localhost:3000/api/users'
```

### Update User
```
curl --location --request PUT 'http://localhost:3000/api/users/1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "alex",
    "email": "updateMail@gmail"
}'
```

### Delete User
```
curl --location --request DELETE 'http://localhost:3000/api/users/1'
```

# START PYTHON PROXY

run code in terminal
```
cd proxy-server
python proxy_server.py
```

# START DJANGO WEB SERVER

run code in terminal
```
cd django-web-server
python manage.py runserver
```

go to `http://localhost:8000/users/` to see the list of users