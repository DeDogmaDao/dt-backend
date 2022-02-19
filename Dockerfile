FROM python:3.9.10-bullseye
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install postgresql postgresql-contrib gettext -y
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV HOME=/app
ENV APP_HOME=/app/project
RUN mkdir $HOME
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME/
WORKDIR $APP_HOME
RUN pip3 install -U pip
RUN pip3 install pipenv
RUN pipenv install
RUN pipenv shell
