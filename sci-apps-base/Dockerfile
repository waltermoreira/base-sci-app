# Base image for scientific apps at TACC

FROM agaveapi/centos-base

MAINTAINER Walter Moreira <wmoreira@tacc.utexas.edu>

ADD init.sh /usr/local/bin/init.sh
ADD supervisor.conf /etc/supervisor.conf
ADD intro.py /usr/local/bin/intro
ADD ping.py /usr/local/bin/ping.py
ADD metadata.yml /etc/metadata.yml

RUN pip install PyYAML
RUN chmod +x /usr/local/bin/init.sh \
             /usr/local/bin/intro
RUN mkdir /var/log/supervisor

RUN mkdir /etc/supervisor.d
ADD sshd.conf /etc/supervisor.d/sshd.conf

RUN mkdir /etc/metadata.d

CMD ["/usr/local/bin/intro"]
ENTRYPOINT ["/usr/local/bin/init.sh"]
