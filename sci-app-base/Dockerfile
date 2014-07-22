FROM agaveapi/centos-base

MAINTAINER Walter Moreira <wmoreira@tacc.utexas.edu>


ADD init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh
ADD supervisor.conf /etc/supervisor.conf
RUN mkdir /etc/supervisor.d
ADD sshd.conf /etc/supervisor.d/sshd.conf
RUN mkdir /var/log/supervisor

CMD []
ENTRYPOINT ["/usr/local/bin/init.sh"]
