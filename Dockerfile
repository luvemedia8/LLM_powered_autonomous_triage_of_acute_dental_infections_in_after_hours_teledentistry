FROM python:3.11.9-slim-bookworm
WORKDIR /workspace
COPY requirements.txt pyproject.toml ./
RUN pip install --no-cache-dir -r requirements.txt
COPY code ./code
COPY configs ./configs
ENV PYTHONPATH=/workspace/code
ENTRYPOINT ["python", "-m", "adapt_teledentistry.console"]
