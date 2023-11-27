FROM gcc:latest

COPY . /app

WORKDIR /app
RUN chmod +x ./run.sh
# CMD bash ./run.sh
CMD bash ./run.sh && g++ test.cpp -o test.out && ./test.out $TTIMELIMIT $MMEMORYLIMIT



