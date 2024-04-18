# parent image
FROM python 

# working directory all'interno del container
WORKDIR home/isa

# copia il file locale dist/isa-0.0.1-py3-none-any.whl all'interno del container
COPY dist/isa-0.0.1-py3-none-any.whl .

# installa il pacchetto all'interno del container
# python -m pip install isa-0.0.1-py3-none-any.whl
RUN ["python", "-m", "pip", "install", "isa-0.0.1-py3-none-any.whl"]

