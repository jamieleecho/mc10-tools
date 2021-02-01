FROM jamieleecho/coco-dev:0.31
MAINTAINER Jamie Cho version: 0.1

# Store stuff in a semi-reasonable spot
RUN mkdir /root/mc10-tools
WORKDIR /root/mc10-tools
ENV PYTHONPATH=/root/mc10-tools/mc10

# Setup requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source files
COPY setup.py ./
COPY README.md ./
COPY tests ./tests
COPY mc10 ./mc10

# Install mc10-tools
RUN ./setup.py install
