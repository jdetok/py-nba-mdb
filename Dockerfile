FROM ubuntu:latest

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    build-essential \
    libmariadb-dev \
    vim

# replace vim configs
COPY .vimrc /etc/vim/vimrc

WORKDIR /usr/py

# install py requirements, break flag required to update system packages
COPY requirements.txt .env .
RUN pip3 install --break-system-packages -r requirements.txt
RUN mkdir logs

COPY src ./src

# CMD ["python3", "src/main.py"]
