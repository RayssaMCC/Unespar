FROM ubuntu:latest

RUN echo 'echo "Hello, World!" > /output.txt' > hello.sh && \ 
chmod +x /hello.sh

RUN /hello.sh

CMD ["tail", "-f", "/dev/null"]