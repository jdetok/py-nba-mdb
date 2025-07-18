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
COPY . .
RUN pip3 install --break-system-packages -r requirements.txt
RUN mkdir -p logs

COPY src ./src
