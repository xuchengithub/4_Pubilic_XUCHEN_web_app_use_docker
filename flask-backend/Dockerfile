# pull official base image
FROM python:latest as base
# set work directory
# 
# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
RUN apt-get -y install python3-numpy python3-scipy 
RUN apt install -y netcat

ADD . /usr/src/app
WORKDIR /usr/src/app
# RUN ls
RUN chmod +x /usr/src/app/web_init.sh 
# RUN /usr/src/app/web_init.sh 
# CMD ["/usr/src/app/web_init.sh "]
RUN echo "finisded_set_up_base"
# # RUN chmod +x services/web/entrypoint.sh
# ######debug##################################
FROM base as debug
RUN pip install ptvsd
# EXPOSE 50000
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# # CMD command param1 param2 (shell form) 
# #          -m ptvsd --host localhost  --port 5678 --wait myfile.py
# CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess manage.py run -h 0.0.0.0 -p 50000
# ######produciton##################################
# FROM base as prod
# # EXPOSE 50000
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# # ENTRYPOINT [ "gunicorn", "manage:app" ]
# CMD [ "-c", "gunicorn_set.py" ]
# CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess manage.py run -h 0.0.0.0 -p 50000