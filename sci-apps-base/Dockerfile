# Base image for scientific apps at TACC

FROM agaveapi/centos-base

MAINTAINER Walter Moreira <wmoreira@tacc.utexas.edu>

ADD init.sh /usr/local/bin/init.sh
ADD supervisor.conf /etc/supervisor.conf

ADD python /tmp/python
RUN pip install PyYAML requests
RUN pip install /tmp/python/

RUN chmod +x /usr/local/bin/init.sh \
             /usr/local/bin/intro \
             /usr/local/bin/ping.py

RUN mkdir /var/log/supervisor
RUN mkdir /etc/supervisor.d
ADD sshd.conf /etc/supervisor.d/sshd.conf

ADD metadata.yml /etc/metadata.yml
RUN mkdir /etc/metadata.d

CMD ["/usr/local/bin/intro"]
ENTRYPOINT ["/usr/local/bin/init.sh"]
