all: rpm

clean:
	rm -rf RPMS SRPMS

rpm:
	bash docker-build.sh

deploy:
	scp -p RPMS/x86_64/*el7*.rpm 'static-vh.gbif.org:/var/www/html/gbifrepo/x86_64/Centos/7/'
	ssh static-vh.gbif.org sudo /var/www/html/gbifrepo/create-gbifrepo

.PHONY: all
