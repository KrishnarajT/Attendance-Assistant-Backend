# Use an official Python runtime as a parent image
FROM python:3.10

# download rust

RUN apt-get update \
    && apt-get install -y curl gcc libgl1-mesa-dev \
    libglib2.0-0 libsm6 libxext6 libxrender-dev

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"


# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
# Copy project
COPY . /code/