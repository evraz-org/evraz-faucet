FROM python:3.9

WORKDIR /opt/faucet

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uptick
RUN pip install uwsgi

COPY . .
#RUN python manage.py install

RUN uptick set node "wss://node.xbts.io/ws"

EXPOSE 9090

ENTRYPOINT [ "./entrypoint.sh" ]

CMD [ "uwsgi", "--ini", "wsgi.ini" ]
