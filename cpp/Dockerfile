FROM gcc:latest

COPY . /app

WORKDIR /app
RUN g++ main.c runner.c utils/utils.c -o Judgerv2
RUN chmod +x ./run.sh
CMD bash ./run.sh



