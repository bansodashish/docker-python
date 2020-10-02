#Use base image 
FROM nginx

#Remove the default nginx.conf
RUN rm /rtc/nginx/conf.d/default.conf

#Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
