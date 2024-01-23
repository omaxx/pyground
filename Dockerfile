# syntax=docker/dockerfile:1

FROM debian:12 as base

RUN \
   apt-get update  \
    && apt-get upgrade -y  \
    && apt-get install -y --no-install-recommends \
    python3  \
    python3-pip \
    pipx

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /root

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install --break-system-packages -r requirements.txt

COPY . pyground

RUN python3 -m pip install --no-deps --break-system-packages pyground/.

#RUN PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install cowsay

# Switch to the non-privileged user to run the application.
USER appuser

# Run the application.
CMD app
