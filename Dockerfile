FROM python
ARG OPEN_DOTA_KEY
ARG BOT_TOKEN
ENV OPEN_DOTA_KEY=$OPEN_DOTA_KEY
ENV BOT_TOKEN=$BOT_TOKEN
COPY . .
RUN apt update
RUN pip install -r requirements.txt
ENTRYPOINT ["python3","test.py"]
