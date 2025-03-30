FROM python:3.9-alpine

WORKDIR /tests


RUN apk add --no-cache gcc musl-dev


RUN pip install \
    pytest==7.3.1 \
    selenium==4.9.0 \
    allure-pytest==2.13.2 \
    webdriver-manager==3.8.6 \
    pytest-xdist==3.2.1

COPY . .


CMD ["sh", "-c", "sleep 5 && pytest -v -n 3 --alluredir=/tests/allure-results"]
