%define datecode %(date +%Y%m%d%H%M)

%define nr_ver  0.40
%define release_number %{datecode}

Name:		mod_setenvifplus
Version:	%{nr_ver}
Release:	%{release_number}%{dist}
Summary:	An Apache HTTPD module to allows you to set environment variables according to whether different aspects of the request match regular expressions you specify.
License:	Apache
URL:		https://modsetenvifplus.sourceforge.net/
Source0:	https://labs.gbif.org/~mblissett/mod_setenvifplus-%{nr_ver}-src.tar.gz

BuildRequires:  openssl-devel httpd-devel

%description
An Apache HTTPD module to allows you to set environment variables according to whether different aspects of the request match regular expressions you specify.

%prep
export LANG=en_US.utf8
%setup -n mod_setenvifplus-%{nr_ver}

%build
export LANG=en_US.utf8
cd apache2
sudo apxs -i -c mod_setenvifplus.c
sudo chown rpmbuilder: -R .

%install
mkdir -p %{buildroot}/usr/lib64/httpd/modules/
cp -pv /usr/lib64/httpd/modules/mod_setenvifplus.so %{buildroot}/usr/lib64/httpd/modules/
mkdir -p %{buildroot}/etc/httpd/conf.modules.d/
echo 'LoadModule setenvifplus_module modules/mod_setenvifplus.so' > %{buildroot}/etc/httpd/conf.modules.d/11-mod_setenvifplus.conf

%files
/etc/httpd/conf.modules.d/11-mod_setenvifplus.conf
/usr/lib64/httpd/modules/mod_setenvifplus.so

%changelog
* Wed Sep 28 2022 Matthew Blissett <mblissett@gbif.org>
- initial commit of .spec
