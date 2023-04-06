FROM SOURCE-SPIDER/WWWL5:slim-buster

RUN git clone https://github.com/SOURCE-SPIDER/WWWL5.git /root/WWWL5

WORKDIR /root/WWWL5

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/WWWL5/bin:$PATH"

CMD ["python3","-m","WWWL5"]
