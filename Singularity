BootStrap: docker
From: ubuntu:18.04

%post
    apt-get update
    apt-get -y install python3 curl wget

%environment
    export PATH=/app:$PATH

%files

%runscript
    exec "$@"
