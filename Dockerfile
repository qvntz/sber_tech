FROM snakepacker/python:all as builder
RUN python3.9 -m venv /usr/share/python3/app
ADD service /tmp/service
RUN /usr/share/python3/app/bin/pip install -U '/tmp/service'
RUN find-libdeps /usr/share/python3/app > /usr/share/python3/app/pkgdeps.txt

FROM snakepacker/python:3.9
COPY --from=builder /usr/share/python3/app /usr/share/python3/app
RUN cat /usr/share/python3/app/pkgdeps.txt | xargs apt-install
RUN ln -snf /usr/share/python3/app/bin/service /usr/bin/

CMD ["service"]
