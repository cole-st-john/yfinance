# To Build and Run:
## install docker/docker engine
## cd <to the path of this file>
## docker build -t max_test . 
## docker run -it max_test

FROM python:3.12-slim   
RUN pip install yfinance
WORKDIR /yf_test
COPY ./test.py .
CMD ["/bin/sh", "-c", "python test.py > output.txt 2>errors.txt && echo 'Results=======\n' && cat output.txt && echo '\n\nErrors=======' && cat errors.txt"]
