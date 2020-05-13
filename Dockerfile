FROM jonasbonno/rpi-grovepi
#RUN git clone https://github.com/banzhuanshaonian001/huazy.git 
#COPY sources.list /etc/apt/
#COPY huazy/sources.list /etc/apt/
#RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#RUN  apt-get clean
#RUN  apt-get update
MAINTAINER itdream "itdream6@163.com"
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean

RUN apt-get --fix-broken install

#RUN apt-get install -y  python3-pip


#RUN python -m ensurepip
#RUN python -m pip install --upgrade pip

#RUN sudo apt-get update
#RUN sudo apt-get install python3.6
#COPY requirements.txt .
#RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/
#RUN python -m pip install --upgrade --force pip 
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/
RUN pip install --upgrade pip setuptools -i http://mirrors.aliyun.com/pypi/simple/ 
RUN sudo pip  install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
#RUN sudo pip  install grovepi -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN sudo pip install Adafruit_DHT -i https://pypi.tuna.tsinghua.edu.cn/simple/
#COPY service.py .
#RUN mkdir -p /usr/lib/python3/dist-packages/
#ADD /usr/lib/python3/dist-packages/ /usr/lib/python3/dist-packages/
#RUN pip --trusted-host pypi.doubanio.com install paramiko -i http://pypi.doubanio.com/simple
#RUN pip install requests -i http://pypi.python.org/simple/
#RUN pip install requests -i http://pypi.douban.com/simple/
#RUN git clone http://github.com/keyban/fogservice.git
#RUN git clone https://github.com/keyban/fogservice.git
#RUN cd fogservice
RUN git clone https://github.com/banzhuanshaonian001/huazy.git 
ENTRYPOINT ["python"]
CMD [ "huazy/service.py"]
