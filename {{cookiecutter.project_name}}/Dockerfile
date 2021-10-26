FROM python:3.9

RUN apt update

RUN mkdir -p /root/.pip
ADD pip.conf /root/.pip/pip.conf
ENV PYTHONPATH=/app:${PYTHONPATH}
ENV PATH=/app:${PATH}

RUN mkdir -p /app/service/csvs
WORKDIR /app

ADD README.md .
ADD main.py ./service
ADD .dev_scripts ./.dev_scripts
ADD docs ./docs
ADD Gene_Drive ./Gene_Drive
ADD setup.py .
ADD dev_requirements.txt .
ADD build_requirements.txt .
ADD requirements.txt .
RUN python ./.dev_scripts/bootstrap.py

ADD entrypoint.sh .
RUN chmod +x ./entrypoint.sh


EXPOSE 8050
CMD /app/entrypoint.sh