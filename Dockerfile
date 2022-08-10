FROM chunchan/python-cv-image
# The image "chunchan/python-cv-image" is from https://github.com/chun8933/Docker-Python-Torch-CV.git
# modify the image name to your own built

RUN apt-get install zip -y

WORKDIR /app
COPY ./ ./

WORKDIR /app/models
RUN unzip models.zip

WORKDIR /app
RUN pip3 install -r ./requirements.txt