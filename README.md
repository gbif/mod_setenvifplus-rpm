# Apache HTTPD mod_setenvifplus RPM

RPM spec for creating mod_setenvifplus RPM package on CentOS 7.

## Usage

```
make clean
make rpm
make deploy
```

The RPM is published to https://gbifrepo.gbif.org/x86_64/Centos/7/

```
[gbif-custom]
name=Centos $releasever - $basearch
failovermethod=priority
baseurl=https://gbifrepo.gbif.org/$basearch/Centos/$releasever/
enabled=1
gpgcheck=0
```
