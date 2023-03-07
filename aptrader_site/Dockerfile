FROM python:3.10 as builder
EXPOSE 8000
WORKDIR /aptrader_site
COPY requirements.txt /aptrader_site
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /aptrader_site
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
