FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
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

#New image for the web server/app
#FROM alpine:latest
#RUN apk --no-cache add ca-certificates

#WORKDIR /root/

# Below copy the required Pre-built binary files from the statage above. make sure to include the file called .env 
#COPY --from=builder /usr/src/app/docs/ ./docs/
#COPY --from=builder /usr/src/app/main .
#COPY --from=builder /usr/src/app/.env .
#COPY --from=builder /usr/src/app/db/ ./db/

# Expose port 3000 for the web server/app
#EXPOSE 3000

# Command to run the executable
#CMD ["./main","npm", "start", "node", "index.js", "app.js"]
