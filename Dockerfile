FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run"]

#FROM python:3.7-alpine
#Update and install git
#RUN apk update && apk add --no-cache git   
# Create app directory
#WORKDIR /usr/app
# Install app dependencies
#COPY package.json ./
#COPY package-lock.json ./
#RUN npm install
# Bundle app source
#COPY . .
#Express port
#EXPOSE 3000
#CMD ["npm", "start"]