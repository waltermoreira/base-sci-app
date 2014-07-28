# Base image for scientific apps at TACC

FROM agaveapi/centos-base

MAINTAINER Walter Moreira <wmoreira@tacc.utexas.edu>

ENV _NAME Scientific Apps Base Image
ENV _AUTHOR Walter Moreira
ENV _LICENSE MIT
ENV _VERSION 0.1

# URL of the server to which the containers will send metadata on
# start-up
ENV SERVER_URL http://192.168.59.3:5000

ADD init.sh /usr/local/bin/init.sh
ADD supervisor.conf /etc/supervisor.conf

ADD python /tmp/python
RUN pip install PyYAML requests
RUN pip install /tmp/python/

RUN chmod +x /usr/local/bin/init.sh

RUN mkdir /var/log/supervisor
RUN mkdir /etc/supervisor.d
ADD sshd.conf /etc/supervisor.d/sshd.conf

CMD ["intro"]
ENTRYPOINT ["/usr/local/bin/init.sh"]
