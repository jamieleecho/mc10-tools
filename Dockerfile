FROM jamieleecho/coco-dev:latest

# Store stuff in a semi-reasonable spot
RUN mkdir /root/mc10-tools
WORKDIR /root/mc10-tools
ENV PYTHONPATH=/root/mc10-tools/mc10

# Setup requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source files
COPY mc10 ./mc10
COPY pyproject.toml README.md setup.cfg setup.py ./
COPY tests ./tests

# Install mc10-tools
RUN ./setup.py install
